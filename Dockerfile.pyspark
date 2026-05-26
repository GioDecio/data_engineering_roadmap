FROM ghcr.io/astral-sh/uv:debian-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    openjdk-21-jre-headless \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_PYTHON=python3

COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --group pyspark

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

WORKDIR /app
