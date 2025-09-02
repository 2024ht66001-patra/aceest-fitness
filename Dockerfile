# Base image: small, secure, and up-to-date
FROM python:3.11-slim

# Always good practice for Python containers
ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     PIP_NO_CACHE_DIR=1

# Workdir inside the image
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose Flask default port
EXPOSE 5000

# Start the app
# If your entry script is named differently, change ACEest_Fitness.py accordingly.
CMD ["python", "ACEest_Fitness.py"]
