# Dockerfile

# Build stage
FROM python:3.13.0a2-slim-bullseye as build
WORKDIR /app

# Install fixed zlib version
RUN apt-get update && apt-get install -y zlib1g=1:1.2.13.dfsg-2+deb11u3

COPY requirements.txt .

# Now install Python dependencies
RUN pip install -r requirements.txt

# Final stage
FROM python:3.13.0a2-slim-bullseye
WORKDIR /app
COPY --from=build /app /app
COPY . .

# Install latest dependencies (if needed)
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "creodamo.py"]
