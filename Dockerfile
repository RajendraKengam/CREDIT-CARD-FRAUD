# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Initialize the database and train the model during build (for simplicity)
# In production, DB init usually happens in an entrypoint script
RUN python train_model.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches using Gunicorn for production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
