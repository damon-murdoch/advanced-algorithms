import sys
import numpy as np

def lcs(x,y):

    m = len(x)
    n = len(y)

    L = [[None] * (n + 1) for i in range(m + 1)]
    R = []

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                R.append([i, j])
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[m][n],R

if __name__ == '__main__':
    x = "AGGTAB"
    y = "GXTXAYB"

    "GTAB"

    ldat,R = lcs(x,y)

    print("Lengt h of LCS is ",ldat)
    
    print(R)

    for i in R[len(x)-ldat:]:
        print(i[0],x[i[0]-1])