# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your Python app runs on (e.g., 5000)
EXPOSE 5000

# Define the command to run the Python application
CMD ["python", "weather_app.py"]
