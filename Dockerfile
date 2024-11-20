FROM python:3.12.6

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .env /app/.env
COPY . .

CMD ["python", "app.py"]