# Dockerfile

# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . .

# Set environment variables to avoid Python buffering
ENV PYTHONUNBUFFERED 1

# Expose the port that the Django application will run on
EXPOSE 8000

# Run database migrations and collect static files (if needed)
# RUN python manage.py migrate && python manage.py collectstatic --noinput

# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]