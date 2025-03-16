# # Use an official Python runtime as a parent image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install required dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose the port Flask runs on
# EXPOSE 5000

# # Run the command to start the Flask app
# CMD ["python", "app.py"]
FROM python:3.9-slim AS builder
RUN apt-get update && apt-get install -y build-essential
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]