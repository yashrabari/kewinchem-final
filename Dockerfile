# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install django pandas pillow

# Copy the entire Django project into the container
COPY . /app/

# Expose the port on which the Django app will run
EXPOSE 8000

# Run Django's development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
