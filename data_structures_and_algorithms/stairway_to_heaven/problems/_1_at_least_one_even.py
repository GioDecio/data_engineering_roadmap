# Per ogni numero nella lista:
#     Se il numero è pari:
#         Rispondi "sì" e fermati
# Se sono arrivato qui senza fermarmi:
#     Rispondi "no"


def at_least_one_even(nums):
    for n in nums:
        if n % 2 == 0:
            return True
    return False
