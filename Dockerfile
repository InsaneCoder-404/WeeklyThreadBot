FROM python:3
WORKDIR /app
COPY . .
RUN pip3 install praw
CMD ["python3", "main.py"]
