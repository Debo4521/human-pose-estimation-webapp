#!/bin/bash

uvicorn app.api:app --host 0.0.0.0 --port 8000 &

streamlit run frontend/streamlit_app.py --server.address=0.0.0.0 --server.port=8501