def simmetr(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)