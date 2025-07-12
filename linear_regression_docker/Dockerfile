# Use an official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy files into the container
COPY requirements.txt .
COPY model.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the model script
CMD ["python", "model.py"]
