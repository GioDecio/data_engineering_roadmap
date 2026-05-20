# pgsql-lab

A local PostgreSQL playground powered by Docker and managed via Make.

## Requirements

- [Docker](https://www.docker.com/) with the Compose plugin
- `make`
- (Optional) [uv](https://docs.astral.sh/uv/) — only if you want to run Python
  code from `src/pgsql_lab/` against the database

## Usage

| Command | Description |
|---|---|
| `make start` | Start the Postgres container in the background |
| `make stop` | Stop and remove containers |
| `make reset` | Wipe the database volume and start fresh |

## Connecting

Once the DB is running, connect with any Postgres client using:

| Parameter | Value |
|---|---|
| Host | `localhost` |
| Port | `5432` |
| User | `lab_user` |
| Password | `lab_password` |
| Database | `lab_db` |

```bash
psql -h localhost -U lab_user -d lab_db
```

## Python environment (optional)

The repo ships with a `pyproject.toml` and `psycopg2-binary` as a dependency,
so you can write Python scripts under `src/pgsql_lab/` to query the database.

```bash
uv sync
uv run python src/pgsql_lab/<your_script>.py
```

The Python CLI entry point (`uv run pgsql-lab ...`) is currently not used —
see `TROUBLESHOOTING.md` for the reason.
