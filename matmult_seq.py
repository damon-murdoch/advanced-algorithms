import sys
import numpy as np

def matrix_chain_mult(p):

    n = len(p)

    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for i in range(1,n):
        m[i][i] = 0

    for L in range(2,n):
        for i in range(1,n-L+1):

            j = i + L - 1

            m[i][j] = sys.maxsize

            for k in range(i,j):

                print(i,j,k,L)

                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]

                if cost < m[i][j]:

                    m[i][j] = cost
                    s[i][j] = k
    return m,s

def print_optimal_parenthesization(s):
    inAResult = [False for x in range(len(s))]
    print_opt_parenthesis(s,0,len(s)-1,inAResult)

def print_opt_parenthesis(s,i,j,res):

    if i != j:
        print_opt_parenthesis(s,i,s[i][j],res)
        print_opt_parenthesis(s,s[i][j]+1,j,res)
        #istr = res[i] = res[i] ? "_result " : " "

        istr,jstr=0,0

        if res[i]:
            istr = "_result "
        else:
            istr = " "

        if res[j]:
            jstr = "_result "
        else:
            jstr = " "

        print(" A_",i,istr,"* A_",j,jstr)

        res[i]=True
        res[j]=True

if __name__ == '__main__':
    m,s = matrix_chain_mult([1,2,3,4])

    print(m)
    print(s)

    print_optimal_parenthesization(s)