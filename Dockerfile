FROM python:3.11

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
RUN /bin/sh -c set -eux;  \
    apt-get update;  \
    apt-get install -y --no-install-recommends memcached sudo;  \
    rm -rf /var/lib/apt/lists/*

RUN sudo service memcached start

COPY . /app

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
