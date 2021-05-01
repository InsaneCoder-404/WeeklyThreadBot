FROM python:3
WORKDIR /app
COPY . .
RUN pip3 install praw
RUN echo %client_id%
CMD ["python3", "main.py"]
