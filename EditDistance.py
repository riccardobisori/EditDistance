import numpy as np

# COP = "Copy"
# DEL = "Delete"
# INS = "Insert"
# REP = "Replace"
# TWI = "Twiddle"


def editDistance(X, Y):
    m = len(X)
    n = len(Y)

    c = np.zeros([m + 1, n + 1], dtype=int)

    for i in range(1, m + 1):
        j = 0
        c[i, j] = i

    for j in range(1, n + 1):
        i = 0
        c[i, j] = j
        # op = np.empty([m, n], dtype=basestring)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i, j] = max(m + 1, n + 1) + 100
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 0
                # op[i, j] = COP
            if X[i - 1] is not Y[j - 1] and (c[i - 1, j - 1] + 1) < c[i, j]:
                c[i, j] = c[i - 1, j - 1] + 1
                # op[i, j] = REP
            if i >= 2 and j >= 2 and X[i - 1] is Y[j - 2] and X[i - 2] == Y[j - 1] and (c[i - 2, j - 2] + 2) < c[i, j]:
                c[i, j] = c[i - 2, j - 2] + 2
                # op[i, j] = TWI
            if (c[i - 1, j] + 1) < c[i, j]:
                c[i, j] = c[i - 1, j] + 1
                # op[i, j] = DEL
            if (c[i, j - 1] + 1) < c[i, j]:
                c[i, j] = c[i, j - 1] + 1
                # op[i, j] = INS

    return c[len(X)][len(Y)]  # and op

