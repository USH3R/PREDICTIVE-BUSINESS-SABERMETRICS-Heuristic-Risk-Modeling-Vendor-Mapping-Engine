#!/bin/bash
# run.sh — installs dependencies and launches the dashboard

pip install -r requirements.txt
streamlit run app.py
