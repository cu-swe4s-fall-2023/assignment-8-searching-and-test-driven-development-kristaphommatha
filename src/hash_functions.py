def get_index(key, N, p=53, m=2**64):
    '''Polynomial Rolling'''
    if N == 0 or m == 0:
        return None
    if type(key) != str:
        return None
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N
