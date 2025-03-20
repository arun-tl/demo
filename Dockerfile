FROM python:3.10-slim

WORKDIR /app

COPY reqirements.txt .

RUN pip install --upgrade pip && pip install -r reqirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
