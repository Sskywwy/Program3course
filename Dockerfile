FROM python:3.14-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install build dependencies (required for some Python packages)
# RUN apt-get update \
# 	&& apt-get install -y --no-install-recommends build-essential git \
# 	&& rm -rf /var/lib/apt/lists/*

# Copy dependency descriptors first (optimizes Docker layer caching)
COPY pyproject.toml ./
COPY poetry.lock ./

# Upgrade pip and install dependencies.
# If `requirements.txt` exists, install from it; otherwise try to install the project
# (via `pyproject.toml`) and ensure `uvicorn` is available as a fallback.
RUN apt-get update && apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/*
ENV POETRY_HOME="/opt/poetry"
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:${PATH}"


RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi
# Copy application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Default command: run Uvicorn serving the FastAPI app in `main.py` as `app`.
# Adjust `main:app` to match your module and app variable if different.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
