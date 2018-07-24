from sys import maxsize as INT_MAX

def get_highest_index(list):
    gt=-1
    index=-1
    for i in range(len(list)):
        if list[i]>gt:
            index=i
            gt=list[i]
    return index

def get_lowest_index(list):
    gt=INT_MAX
    index=-1
    for i in range(len(list)):
        if list[i]<gt:
            index=i
            gt=list[i]
    return index

def get_pivot_row(tableau,col):
    lval=INT_MAX
    lrow=-1
    for i in range(len(tableau)-1):
        rval = tableau[i][-1] / tableau[i][col]
        if rval < lval:
            lval = rval
            lrow = i
    return lrow

def divide_list_by_index(list,col):
    copy=list
    pivot=list[col]
    for i in range(len(copy)):
        copy[i] /= pivot
    return copy

def is_optimal(tableau):
    for i in tableau[-1]:
        if i < 0:
            return 0
    return 1

def unit_operation(tableau,unit_row,unit_col):
    copy = tableau
    pivot = copy[unit_row][unit_col]
    for i in range(len(copy)):
        if i == unit_row:
            continue
        unit = copy[i][unit_col] / pivot
        for j in range(len(copy[i])):
            copy[i][j] -= copy[unit_row][j]*unit
    return copy

def simplex(tableau):
    copy = tableau
    while not is_optimal(copy):
        col = get_lowest_index(copy[-1])
        row = get_pivot_row(copy,col)
        copy[row] = divide_list_by_index(copy[row],col)
        copy = unit_operation(copy,row,col)
    return copy

if __name__ == '__main__':
    tableau = [[2,1,1,0,0,180],[1,3,0,1,0,300],[-1,-6/5,0,0,1,0]]
    print(tableau)
    opt = simplex(tableau)
    print(opt)