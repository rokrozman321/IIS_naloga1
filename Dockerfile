FROM python:3.9-slim

WORKDIR /app

# Install dependencies for building and running the application
RUN pip install poetry

# Install Poetry dependencies
COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-dev

COPY . /app

COPY src/serve/app.py /app/src/serve

EXPOSE 5000

WORKDIR /app/src/serve/

# Start the application
CMD ["poetry", "run", "python", "app.py"]

# CMD ["poetry", "run", "python", "src/serve/app.py"]