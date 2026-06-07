FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para iniciar la aplicación en Railway
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]