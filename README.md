# Trade Opportunities API

A FastAPI-based service that analyzes Indian market sectors and generates structured markdown trade opportunity reports using real-time news data and Google's Gemini AI.

## Setup

pip install -r requirements.txt
uvicorn app.main:app --reload

## Auth Token

python -c "from app.core.auth import create_token; print(create_token('testuser'))"

## Endpoint

GET /analyze/{sector}
