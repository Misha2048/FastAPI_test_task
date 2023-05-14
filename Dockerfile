FROM python:3.11.3-alpine3.18
COPY . /app
WORKDIR /app
RUN apk update &&\
    apk upgrade &&\
    python3 -m pip install --upgrade pip &&\
    pip3 install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "index:app", "--port", "8000", "--host", "0.0.0.0"]