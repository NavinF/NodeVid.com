FROM nginx
RUN apt-get -y update && apt-get -y install python3-pip
RUN pip3 install django uwsgi
RUN rm /etc/nginx/conf.d/default.conf
COPY website/nginx/nginx.conf /etc/nginx/nginx.conf
COPY website/nginx/website.conf /etc/nginx/conf.d/website.conf
COPY . /mysrc
#Leak keys: COPY . /usr/share/nginx/html
RUN python3 /mysrc/website/manage.py migrate
CMD uwsgi --single-interpreter --master --enable-threads --close-on-exec --strict --uid=nginx -s /tmp/uwsgi.sock \
    --chdir=/mysrc/website --module=website.wsgi:application & nginx -g 'daemon off;'