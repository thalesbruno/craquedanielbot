FROM python:3.8-alpine

WORKDIR /app
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]

VOLUME ["/app/bot/data"]

ENTRYPOINT ["python3", "bot/bot.py"]
