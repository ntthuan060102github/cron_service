FROM python:3.9.5-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       default-libmysqlclient-dev gcc pkg-config supervisor \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /usr/src/app

EXPOSE 80

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]