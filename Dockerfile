# Use an official Python runtime as the base image
FROM python:3.11.2

# Set environment variables for the Docker image
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the Docker image
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY ./backend .

# Expose the port that the Django application will run on
EXPOSE 8080

# Run the Django development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]