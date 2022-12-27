# Pull base image
FROM python:3.8

# Setting ports
EXPOSE 8501

# Set environmental variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy Project
COPY . /code/

# Start project
ENTRYPOINT ["streamlit", "run", "mainChatGPT.py", "--server.port=8501", "--server.address=0.0.0.0"]
