# 392 - Is Subsequence

**Problema:** data una stringa `s` e una stringa `t`, restituire `True` se `s` è una sottosequenza di `t`.

Una sottosequenza mantiene l'ordine dei caratteri ma non richiede che siano contigui.
`"ace"` è sottosequenza di `"abcde"`, `"aec"` non lo è.

---

## Soluzione: due puntatori (two pointers)

```python
def isSubsequenceWhile(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```

### Idea

Due indici scorrono le due stringhe in parallelo:
- `i` punta al carattere di `s` che stai cercando
- `j` scorre `t` da sinistra a destra

La regola è semplice:
- `j` avanza **sempre**
- `i` avanza **solo** quando `s[i] == t[j]`, cioè quando hai trovato il carattere che cercavi

Alla fine, se `i` ha attraversato tutta `s` (`i == len(s)`), hai trovato tutti i caratteri nell'ordine giusto.

### Esempio: `s = "abc"`, `t = "ahbgdc"`

| j | t[j] | i | s[i] | match? | avanza |
|---|------|---|------|--------|--------|
| 0 | `a`  | 0 | `a`  | si     | i e j  |
| 1 | `h`  | 1 | `b`  | no     | solo j |
| 2 | `b`  | 1 | `b`  | si     | i e j  |
| 3 | `g`  | 2 | `c`  | no     | solo j |
| 4 | `d`  | 2 | `c`  | no     | solo j |
| 5 | `c`  | 2 | `c`  | si     | i e j  |

Fine: `i == 3 == len("abc")` → `True`

### Perché `and` e non `or`?

Il loop continua solo se **entrambe** le condizioni sono vere. Non appena una diventa falsa, si ferma.

Con `or` continueresti ad accedere a una stringa già esaurita → `IndexError`.

Python usa la **short-circuit evaluation**: con `and`, appena trova una condizione `False` smette di valutare le successive. Quindi quando `i == len(s)`, Python vede `False and ...` e non entra più nel loop senza nemmeno controllare `j`.

Nota: `i == len(s)` non viene mai eseguito *dentro* il loop — viene solo controllato come condizione di uscita prima di ogni iterazione.

### Complessità

- **Tempo:** O(n) dove n = len(t) — scorri `t` una volta sola
- **Spazio:** O(1) — solo due indici
