# Plan — Esercizi DSA

Esercizi raccolti dalla conversazione. Ordine: dal più semplice al più
strutturato. Non passare al successivo finché non hai completato i livelli
1-3 (a parole / esempio / pseudocodice in italiano) **prima** di scrivere
codice.

---

## Metodo (vale per tutti gli esercizi)

Per ogni problema, prima di toccare la tastiera:

1. **Cosa entra / cosa esce** — input e output, in una riga ciascuno.
2. **Esempio a mano** — scegli un input piccolissimo e fai *tu* cosa
   farebbe il programma. Cerchia, sottolinea, traccia con la matita.
3. **Pseudocodice in italiano** — frasi normali, niente `for`, niente
   `return`. Una persona non programmatrice deve poterlo seguire.
4. **Solo ora**: scrivi il Python.

Test del passaggio 3: se nello pseudocodice ci sono parole come "indice",
"array", "loop", "return" → è codice mascherato, riscrivilo.

---

## Esercizio 1 — Almeno un pari

**Problema:** data una lista di numeri, dimmi se contiene almeno un numero
pari.

**Esempio fatto in conversazione (per riferimento, non copiare):**
- Cosa entra: una lista di numeri
- Cosa esce: vero / falso
- Pseudocodice:
  ```
  Per ogni numero nella lista:
      Se il numero è pari:
          Rispondi "sì" e fermati
  Se sono arrivato qui senza fermarmi:
      Rispondi "no"
  ```

Questo è già stato discusso — usalo come *modello* di cosa significa
pseudocodice in italiano vero. Non come soluzione da copiare.

---

## Esercizio 2 — Conta le 'a'

**Problema:** data una stringa, contami quante volte appare la lettera 'a'.

**Da fare:**
- Cosa entra / cosa esce
- Esempio a mano (es. con la stringa "banana")
- Pseudocodice in italiano
- Solo dopo: codice Python

**Domande da farsi dopo:**
- Funziona con la stringa vuota?
- Funziona se la 'a' non c'è?
- Dovrebbe contare anche le 'A' maiuscole? (Il problema non lo dice — è
  un'ambiguità da notare.)

---

## Esercizio 3 — Elemento in comune

**Problema:** date due liste, dimmi se hanno almeno un elemento in comune.

**Da fare:** stessa procedura (1-4).

**Domande da farsi dopo:**
- Quante volte stai scorrendo gli elementi? Se per ogni elemento di lista A
  scorri tutta lista B → quanto è il costo? (Pensa O grande.)
- Esiste un modo più furbo? Indizio: cosa succede se trasformi una delle
  due liste in qualcosa di diverso (non una lista)?
- Questo è un caso in cui "la prima soluzione che funziona" potrebbe
  essere O(n²) e ce n'è una O(n). Prima fai funzionare quella semplice,
  poi pensa a migliorare.

---

## Esercizio 4 — Riconoscere quando si applica binary search

Per ognuna di queste tre situazioni, ragiona a parole (no codice) se la
binary search si applica e perché sì o perché no:

1. Lista **ordinata** di numeri, vuoi sapere se contiene un numero negativo.
2. Lista **non ordinata** di numeri, vuoi trovare il massimo.
3. Lista **ordinata** di parole (ordine alfabetico), vuoi sapere se
   contiene la parola "casa".

**Criterio da applicare:**
- I dati sono ordinati rispetto alla proprietà che cerchi?
- Sapere com'è un elemento "in mezzo" ti permette di scartare metà dello
  spazio di ricerca?

Se entrambi sì → binary search si applica.
Se anche solo uno è no → no.

---

## Dopo aver finito

Per ogni esercizio risolto, prima di passare al successivo, rispondi a
queste due domande **per iscritto** (anche solo una riga):

1. **Che pattern ho usato?** Dagli un nome tuo.
   (Es: "scorri-e-fermati appena trovi", "conta-occorrenze",
   "intersezione-tra-insiemi".)
2. **Cosa ho imparato che non sapevo prima?**
   Non il codice — il *pensiero*. Es: "ho capito che se devo solo dire
   sì/no posso fermarmi al primo match invece di scorrere tutto."

Questa è la parte che quasi nessuno fa ed è dove sta tutto l'apprendimento.