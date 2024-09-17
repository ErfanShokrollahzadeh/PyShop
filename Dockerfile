# Use python:3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Expose port 8000
EXPOSE 8000

# Run the Django development server on port 8000
CMD ["python", "fruit_shop/manage.py", "runserver", "0.0.0.0:8000"]