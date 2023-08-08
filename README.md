# Generate Podcast Notes using ChatGPT/GPT-3

Have you ever wanted to generate podcast notes using AI? Well, now you can! You no longer need to listen to the entire podcast to get the notes. This is a simple script to generate podcast notes (or any YouTube video) using [ChatGPT](https://openai.com/blog/chatgpt/) and OpenAI's [API](https://openai.com/api/).

![main_image](./public/podcast_notes_main_screen.png)

Due to unavailability of ChatGPT's official API, the workaround [pyChatGPT](https://github.com/terry3041/pyChatGPT) library was used; however, it may only work on your local machine with Chrome installed. Due to the nature of the library, it is not possible to run this script on a server. That is why, I have used OpenAI's API to generate the notes, and it is hosted on Streamlit.

## Demo (GPT-3 Note Creator)

Link to the demo: [https://podcast-notes-gpt.streamlit.app/](https://podcast-notes-gpt.streamlit.app/)

## Demo (ChatGPT Note Creator)

1. Clone the repository
2. Install the requirements
3. Run the script using `streamlit run mainChatGPT.py`
4. Go to `localhost:8501` on your browser

## To run using Docker:

1. Make sure that Docker is [installed](https://docs.docker.com/engine/install/) into your system.
2. Run ```docker build -t podcast .``` in the project main directory to build the image of project
3. Finally, to run the built image, run ```docker run -d -p 8501:8501 --name pylint podcast```
4. Go to `localhost:8501` in your browser.
