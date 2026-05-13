# Setup fixes — maggio 2026

## Problema principale
`uv run pyspark_playground/_XX.py` funzionava a volte e falliva altre volte con
`ModuleNotFoundError: No module named 'pyspark_playground'` o errori di import su `pyspark`/`py4j`.

---

## Cause trovate

### 1. Venv corrotto da crash della JVM
Quando Spark crasha durante l'avvio (es. porta non ancora liberata dal run precedente),
Python scrive `.pyc` parziali nella `__pycache__` di `pyspark` o `py4j`.
I run successivi caricano questi file corrotti e falliscono anche se il venv è intatto.

**Fix**: aspettare almeno 30 secondi tra un run e l'altro di script PySpark.
Se il venv è già corrotto: `rm -rf .venv && uv sync`

### 2. pyproject.toml mancante di build-system (risolto poi con pythonpath)
Senza `[build-system]` e `[tool.uv] package = true`, uv non installava
`pyspark_playground` come pacchetto editable, quindi non era importabile.
Abbiamo provato questa strada ma si rivelava fragile (pytest-cov interferiva).

**Soluzione finale adottata**: niente editable install — si usa `PYTHONPATH` implicito.

### 3. Import di `utils` ambiguo
Alcuni file usavano `from pyspark_playground.utils import show`,
altri `from utils import show`.

- `from utils import show` funziona con `uv run script.py` perché Python aggiunge
  automaticamente la directory dello script (`pyspark_playground/`) a `sys.path`.
- `from pyspark_playground.utils import show` funziona con pytest ma non con
  `uv run script.py` senza l'editable install.

**Fix**: usare `from utils import show` in tutti i file + aggiungere `pyspark_playground`
al `pythonpath` di pytest nel `pyproject.toml`.

---

## Configurazione finale

### pyproject.toml
```toml
[tool.pytest.ini_options]
pythonpath = [".", "pyspark_playground"]
```

### pyspark_playground/__init__.py
Popolato con import relativi da tutti i moduli:
```python
from ._1_e_load_and_transform_data import *
# ... tutti gli altri moduli
```

### Import da usare in ogni script
```python
from utils import show
```

---

## Regole operative

- Tra un `uv run` PySpark e l'altro, aspettare almeno 30 secondi.
- Se compaiono errori `cannot import name X from pyspark` o `partially initialized module py4j`:
  il venv è corrotto. Soluzione: `rm -rf .venv && uv sync`
- Non usare `from pyspark_playground.utils import show` negli script — rompe `uv run`.
