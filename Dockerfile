FROM node:15

ENV HUGO_VERSION=0.82.1 \
    HUGO_SITE=/app/hugo
ENV HUGO_BINARY=hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz

RUN apt-get update && apt-get install -y wget git
RUN wget -O hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.deb
RUN dpkg -i hugo.deb
RUN rm hugo.deb


WORKDIR ${HUGO_SITE}
EXPOSE 1313
