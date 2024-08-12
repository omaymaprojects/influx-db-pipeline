# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR # Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "your_project_name/main.py"]



# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "influxdb/main.py"]
