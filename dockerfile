FROM python:3.8

ENV PYTHONUNBUFFERED True

COPY src /app/src
WORKDIR /app/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/* \ 
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc build-essential

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "1", "--threads", "4", "App:app"]
