FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 8501

CMD uvicorn app.api:app --host 0.0.0.0 --port 8000 & streamlit run frontend/streamlit_app.py --server.address=0.0.0.0 --server.port=8501