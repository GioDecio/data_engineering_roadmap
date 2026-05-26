FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

RUN uv sync --no-dev

CMD ["uv", "run", "pgsql-lab"]
