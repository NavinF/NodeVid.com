FROM nginx:latest
RUN apt-get -y update && apt-get -y install python3-pip
RUN pip3 install django uwsgi
COPY . /mysrc
COPY . /usr/share/nginx/html