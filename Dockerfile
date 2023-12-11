(Improved for Multi-Stage Builds)

# Dockerfile

# Build stage
FROM python:3.13.0a2-slim-bullseye as build
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Final stage
FROM python:3.13.0a2-slim-bullseye
WORKDIR /app
COPY --from=build /app /app
COPY . .
EXPOSE 8000
CMD ["python", "creodamo.py"]
