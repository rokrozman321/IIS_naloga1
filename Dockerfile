FROM python:3.9-slim

WORKDIR /app

# Install dependencies for building and running the application
RUN apt-get update && \
    apt-get install -y curl build-essential && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Install Poetry dependencies
COPY pyproject.toml poetry.lock ./
RUN /root/.poetry/bin/poetry install --no-root

COPY src/ models/ ./

CMD ["/root/.poetry/bin/poetry", "run", "python", "./src/serve/app.py"]