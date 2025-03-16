FROM python:3.9-slim

WORKDIR /app

COPY requiremnts.txt .
RUN pip install --no-cache-dir -r requiremnts.txt

COPY producer.py .

CMD ["python", "producer.py"]
