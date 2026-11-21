FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask==3.0.0 gunicorn==21.2.0

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "bulutli_t_2:app"]
