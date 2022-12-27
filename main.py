import streamlit as st
from pyChatGPT import ChatGPT
from youtube_transcript_api import YouTubeTranscriptApi

st.header("Get podcast notes using AI")

# uncomment if want to use session token
# session_token = st.text_input('Session token from ChatGPT')

st.write('Enter your ChatGPT credentials below. If you don\'t have an account, you can sign up for free at https://openai.com/blog/chatgpt/')
email = st.text_input('Email')
password = st.text_input('Password', type="password")

st.markdown("""---""")

yt_id = st.text_input('YouTube video ID')

bpm = st.slider('Choose # of bullet points/minute', 1, 5)

if st.button('Get notes'):
    result = YouTubeTranscriptApi.get_transcript(yt_id)

    api = ChatGPT(auth_type='openai', email=email, password=password)  # auth with email and password

    # uncomment if want to use session token
    # api = ChatGPT(session_token)

    curr_time = 0
    interval = 1
    text = []
    curr_text = ""
    for obj in result:
        curr_text += obj['text']
        curr_time = obj['start']
        if curr_time > interval * 600:
            text.append(curr_text)
            curr_text = ""
            interval += 1

    notes = ""
    prompt = f"Based on the following YouTube transcript provide a {5*bpm} bullet point summary in complete sentences: \n"

    st.write('Number of note blocks: ' + str(len(text)))

    for i in range(len(text)):
        print('test')
        res = api.send_message(prompt + text[i])['message'] + "\n"
        st.write('Block ' + str(i+1) + '/' + str(len(text)) + ':')
        st.write(res)
        notes += res

    api.reset_conversation()  # reset the conversation
    api.refresh_chat_page()  # refresh the chat page