FROM python:3

MAINTAINER Marc Durocher

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY echowebserver.py .

EXPOSE 8888

CMD [ "python", "./echowebserver.py" ]
