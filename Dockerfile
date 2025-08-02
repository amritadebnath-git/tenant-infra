FROM python:3.11-slim

WORKDIR /app

# Copy all app files directly
COPY app/Test_app.py .
COPY app/users.db .
COPY app/templates ./templates
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]


