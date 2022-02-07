#!/bin/sh
sleep 10 &&
alembic upgrade head &&
python  /usr/src/app/app/initial_data.py &&
poetry run uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000