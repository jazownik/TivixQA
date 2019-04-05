FROM python:3.6-alpine3.7

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

RUN apk update
RUN apk add chromium chromium-chromedriver
RUN pip install selenium pytest
COPY tests /tests
CMD [ "pytest /tests" ]