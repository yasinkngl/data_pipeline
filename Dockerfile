# Use an official lightweight Python image.
FROM python:3.12.8

# Set the working directory in the container.
WORKDIR /app

# Copy requirements file and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Specify the default command (adjust as needed, e.g., to run a particular script).
CMD ["python","-m", "unittest", "discover","tests"]