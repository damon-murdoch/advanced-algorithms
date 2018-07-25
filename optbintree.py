import numpy as np
import sys



def find_optimal_search_tree(values,weights):

    T = np.zeros([len(values),len(values)])
    R = np.zeros([len(values),len(values)])

    for i in range(0,len(T)):
        T[i][i]=weights[i]

    for l in range(2,len(values)+1):
        for i in range(0,len(values)-l+1):

            j = i + l - 1

            T[i][j] = sys.maxsize

            sum = get_sum(weights,i,j)

            for k in range(i,j+1):

                val = sum

                if k-1 >= i:
                    val += T[i][k-1]

                if k+1 <= j:
                    val += T[k+1][j]

                if val < T[i][j]:
                    T[i][j] = val
                    R[i][j] = k

    return T[0][len(values)-1],R

def get_sum(freq,i,j):

    sum = 0

    for x in range(i,j+1):
        sum += freq[x]

    return sum

if __name__ == '__main__':

    values = [10,12,20]
    weights = [34,8,50]

    T,R = find_optimal_search_tree(values,weights)

    print(T)
    print(R)