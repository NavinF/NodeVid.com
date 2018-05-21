# wblankenship/webtorrent
#
# Contains webtorrent-hybrid in a stable envoriment
#
# wrtc is super touchy and fragile, this is an attempt to make running
# webtorrent on wrtc predicatable by containing it and all of its deps in
# a Docker image.
FROM nodesource/node:0.10

MAINTAINER william.jblankenship@gmail.com


RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs

# wrtc deps
RUN apt-get update \
  && apt-get install -y --force-yes --no-install-recommends \
        python2.7 \
        git-all \
        pkg-config \
        libncurses5-dev \
        libssl-dev \
        libnss3-dev \
        libexpat-dev \
 && rm -rf /var/lib/apt/lists/*;

RUN apt-get update
RUN apt-get install -y xvfb
RUN apt-get install -y libgtk2.0
RUN apt-get install -y libXtst-dev

# Install webtorrent-hybrid
RUN git clone --recursive https://github.com/NavinF/webtorrent-hybrid \
 && cd webtorrent-hybrid \
 && npm install \
 && npm link

# Serve files out of /srv to be a good linux citizen
RUN mkdir -p /srv/webtorrent
WORKDIR /srv/webtorrent

CMD ["webtorrent-hybrid", "-q","--verbose","seed","/srv/webtorrent"]
