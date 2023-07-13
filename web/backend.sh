#!/bin/bash
cd /home/eric/DocumentBorder/backend
source /home/eric/DocumentBorder/backend/venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 4001