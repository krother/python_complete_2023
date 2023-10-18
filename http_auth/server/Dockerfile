# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
# (a text files with all the libraries you want to install)
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
