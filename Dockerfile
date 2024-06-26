FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Copy the startup script
COPY startup.sh /app/startup.sh

# Make the startup script executable
RUN chmod +x /app/startup.sh

# Set the entry point to the startup script
ENTRYPOINT ["/app/startup.sh"]