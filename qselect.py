from random import randint

def random_qselect(a,p,q,e):

        if a == []:
            return []
        else:
            # Generate random number
            random_pivot = randint(p, q)

            #To implement randomized qselect, swap last number in array with pivot
            a[random_pivot],a[q] = a[q], a[random_pivot]
            # partition the table and get pivot index
            pivot = partition(a,p,q)
            if (e == (pivot+1)):
                return a[pivot]
            elif e < (pivot+1):
                return random_qselect(a,p,pivot-1,e)
            else:
                return random_qselect(a,pivot+1, q,e)

def qselect(e,a):
       if e>len(a):
           return None

       return random_qselect(a, 0, len(a) - 1, e)

def partition(a,p,q):
    pivot = a[q]
    i = p
    for x in range(p,q):
        if a[x] <= pivot:
            #swap (a, i, x)
            a[i],a[x] = a[x], a[i]
            i = i + 1

    a[i],a[q] = a[q], a[i]
    return i














