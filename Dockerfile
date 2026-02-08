# Use official Python image
FROM python:3.12-slim

#Set working directory
WORKDIR /app

#Install system dependencies fro Playwright
RUN apt-get update && apt-get install -y \
     wget \
     gnupg \
     && rm -rf /var/lib/apt/lists/*

# Copy requirments and install
COPY requirements.txt  .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps chromium

#Copy the rest of the code
COPY . .

# Default command to run tests
CMD ["pytest", "-v"]