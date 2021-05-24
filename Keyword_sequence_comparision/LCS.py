def lcs(a, b):
    tbl = [[0 for B in range(len(b) + 1)] for A in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            tbl[i + 1][j + 1] = tbl[i][j] + 1 if x == y else max(
                tbl[i + 1][j], tbl[i][j + 1])
    res = []
    i, j = len(a), len(b)
    while i and j:
        if tbl[i][j] == tbl[i - 1][j]:
            i -= 1
        elif tbl[i][j] == tbl[i][j - 1]:
            j -= 1
        else:
            res.append(a[i - 1])
            i -= 1
            j -= 1
    return res[::-1]
    
