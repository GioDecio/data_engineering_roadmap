def find_needle(n, h):
    if len(h) < len(n):
        return False

    for idx in range(len(h) - len(n) + 1):
        if n == h[idx : idx + len(n)]:
            return True

    return False


