FROM python:3.8-slim

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

EXPOSE 5000

ENV MODEL_PATH=/app/best_model.json
ENV GUNICORN_CMD_ARGS="--workers=1 --threads=1 -b 0.0.0.0:5000"


CMD ["gunicorn", "app:app"]
