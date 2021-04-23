FROM python:3.8

COPY . /app/server

WORKDIR /app/server

RUN pip install -r requirements.txt

ENTRYPOINT ["python","twitbot.py"]
