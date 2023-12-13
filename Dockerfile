# Dockerfile

# Build stage
FROM python:3.13-slim-bullseye as build

# Install build dependencies 
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev zlib1g cargo

# Install Rust
RUN curl -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="$PATH:/root/.cargo/bin"

# Copy poetry files
COPY pyproject.toml poetry.lock /app/

# Install cryptography and its dependencies
RUN poetry install

# Final stage  
FROM python:3.13-slim-bullseye

# Copy application
COPY --from=build /app/site-packages /app/site-packages
COPY . /app

# Set environment variables
ENV ENV_VAR_NAME=value

# Expose port
EXPOSE 8000 

# Set working directory
WORKDIR /app

# Run migrations  
RUN python manage.py migrate

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Add labels
LABEL maintainer="Jacque Antoine DeGraff<jacquedegraff@creodamo.com>" \
      version="1.0" \
      description="Dockerfile for CreoDAMO"
