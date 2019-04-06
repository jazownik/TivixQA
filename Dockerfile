FROM python:3.6-alpine3.9

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.9/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.9/community" >> /etc/apk/repositories

RUN apk update
RUN apk add chromium chromium-chromedriver
RUN pip install selenium pytest allure-pytest
COPY tests /tests
RUN mkdir /results
CMD [ "pytest /tests/test_careers_page.py" ]