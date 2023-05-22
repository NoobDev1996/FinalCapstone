# Use the official Python base image with the desired Python version
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the working directory
COPY . .

# Expose the port on which your Django app will run
EXPOSE 8000

# Run the Django development server using the 'manage.py' script
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]