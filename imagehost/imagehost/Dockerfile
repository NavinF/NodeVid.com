FROM cellofellow/ffmpeg:latest
EXPOSE 5000
VOLUME static
RUN apt update 
RUN apt install -y python3
RUN apt install -y python-pip python-dev build-essential 
RUN pip install --upgrade pip 
RUN pip install --upgrade virtualenv 
RUN pip install flask
RUN pip install ffmpy
RUN pip install requests
COPY . .
ENTRYPOINT python main.py

