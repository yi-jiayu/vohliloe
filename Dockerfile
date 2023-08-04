FROM python:3.11.4-slim

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8080
ENV PORT=8080
ENTRYPOINT ["gunicorn", "hello:app"]
