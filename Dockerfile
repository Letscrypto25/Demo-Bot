# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Fly.io needs (default for HTTP services)
EXPOSE 8080

# Run the bot script
CMD ["python", "bot.py"]
