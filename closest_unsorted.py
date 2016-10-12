from random import randint
from copy import deepcopy

def diff_list(a,xsrch):
    if a == []:
        return []
    else:
        return [abs(a[0]-xsrch)] + diff_list(a[1:],xsrch)

def random_qselect(a, p, q, e):
    if a == []:
        return []
    else:
        # Generate random number
        random_pivot = randint(p, q)

        # To implement randomized qselect, swap last number in array with pivot
        a[random_pivot], a[q] = a[q], a[random_pivot]
        # partition the table and get pivot index
        pivot = partition(a, p, q)
        if (e == (pivot + 1)):
            return a
        elif e < (pivot + 1):
            return random_qselect(a, p, pivot - 1, e)
        else:
            return random_qselect(a, pivot + 1, q, e)

def partition(a, p, q):
    pivot = a[q]
    i = p
    for x in range(p, q):
        if a[x] <= pivot:
            # swap (a, i, x)
            a[i], a[x] = a[x], a[i]
            i = i + 1

    a[i], a[q] = a[q], a[i]
    return i

def find(a,xsrch,k):
    if k > len(a) or k ==0:
        return []
    sublist = diff_list(a, xsrch)
    originallist =  deepcopy(sublist)
#apply qselect logic to find k closest elements
    finallist= random_qselect(sublist,0,len(a)-1,k)
    fl = []
    temp = finallist[:k]

    for i, x in enumerate (temp):
        fl.append(a[originallist.index(x)])
    return fl



