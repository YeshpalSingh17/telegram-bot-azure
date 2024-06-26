#!/bin/bash

# Set the number of worker processes and threads
WORKERS=4
THREADS=2

# Start Gunicorn with the specified configuration
gunicorn --bind=0.0.0.0:8080 --workers=$WORKERS --threads=$THREADS bot:app

