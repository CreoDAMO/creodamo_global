# Dockerfile

# Build stage
FROM python:3.13.0a2-slim-bullseye as build

# Set working directory
WORKDIR /app

# Install fixed zlib version and dependencies for python-ldap
RUN apt-get update && apt-get install -y \
    zlib1g=1:1.2.13.dfsg-2+deb11u3 \
    gcc \
    libc6-dev \
    libldap2-dev \
    libsasl2-dev \
    python3-dev

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Final stage
FROM python:3.13.0a2-slim-bullseye

# Set working directory
WORKDIR /app

# Copy the built files from the build stage to the final stage
COPY --from=build /app /app

# Copy the current directory to the working directory in the final stage
COPY . .

# Set environment variables for configuration
ENV ENV_VAR_NAME=value

# Add labels for better maintainability
LABEL maintainer="Jacque Antoine DeGraff<jacquedegraff@creodamo.com>"
LABEL version="1.0"
LABEL description="Dockerfile for the application"

# Specify the command to run when the container starts
CMD ["python", "creodamo.py"]
