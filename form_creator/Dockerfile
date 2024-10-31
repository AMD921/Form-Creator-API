FROM python:3.12.6-slim

WORKDIR /app

RUN pip install gunicorn

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "bash", "entrypoint.sh" ]
