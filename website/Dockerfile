FROM nginx
RUN apt-get -y update && apt-get -y install python3-pip
RUN pip3 install django uwsgi
COPY . /mysrc
COPY . /usr/share/nginx/html
RUN python3 /mysrc/website/manage.py migrate
CMD uwsgi --http :80 --chdir=/mysrc/website --module=website.wsgi:application