FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache netcat-openbsd

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "wsgi.py"]
