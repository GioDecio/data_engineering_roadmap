# Troubleshooting

## `uv run pgsql-lab` → `ModuleNotFoundError: No module named 'pgsql_lab'`

### Symptom
With a uv-managed project that declares an entry point under `[project.scripts]`,
running `uv run pgsql-lab <cmd>` works the first time after `uv sync` but fails
on later invocations with:

```
ModuleNotFoundError: No module named 'pgsql_lab'
```

### Root cause
Bug in **uv 0.11.7**: the editable `.pth` files generated in the venv
(`_editable_impl_<pkg>.pth` with hatchling, `__editable__.<pkg>.pth` with
setuptools) are written **without a trailing newline**. Python silently ignores
`.pth` lines that do not end with `\n`, so the package is never added to
`sys.path`.

Reproducible with both build backends (hatchling and setuptools), because the
bug is in uv itself, not in the backend. `uv run` performs an implicit sync on
every invocation and flips between states, which explains the "first command
works, second fails" pattern.

### Quick diagnosis
```bash
xxd .venv/lib/python*/site-packages/__editable__*.pth | tail -1
xxd .venv/lib/python*/site-packages/_editable_impl_*.pth | tail -1
```
If the last byte is not `0a` (newline), this bug is the culprit.

```bash
uv run python -c "import sys; print('\n'.join(sys.path))"
```
If the package source directory (e.g. `src/`) is missing from the output, the
bug is confirmed.

### Things that did NOT fix it
- Pinning `requires-python = ">=3.13,<3.14"` — bug also occurs on 3.13.
- Switching from `src/` layout to flat layout — same bug.
- `uv sync --no-editable` — uv ignores the flag on the next `uv run` and
  reinstalls in editable mode.
- Switching build backend from `hatchling` to `setuptools` — both produce
  newline-less `.pth` files via uv.
- `uv pip install --no-deps .` (non-editable) + `.venv/bin/pgsql-lab` works,
  but `uv run` converts the install back to editable on next use.

### Workaround chosen for this project
Avoid the Python CLI entirely. The container lifecycle is now driven by
`make start | stop | reset`, which calls `docker compose` directly. No
editable install, no `uv run` involved — nothing to break.

The Python package under `src/pgsql_lab/` and `pyproject.toml` are kept for
writing scripts that connect to the database (using `psycopg2-binary`), which
can be run with `uv run python src/pgsql_lab/<script>.py` without depending on
an installed entry point.

### Alternative (not adopted)
Downgrade uv to a version before the regression:
```bash
brew uninstall uv
curl -LsSf https://astral.sh/uv/0.5.11/install.sh | sh
```

## Side notes from the investigation
- On macOS, system `python3` (3.9.6) ≠ brew's `python3.13`. Normal: brew does
  not override `python3`; it only installs versioned binaries like `python3.13`.
- `python@3.13` cannot be uninstalled via brew because `poetry` and `vim` depend
  on it.
- A `VIRTUAL_ENV` value inherited from a parent shell can produce misleading
  warnings; opening a fresh terminal clears it.
