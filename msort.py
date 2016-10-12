#main function
def mergesort(a):
    if a == []:
        return []
    if(len(a)==1):
        return a
    else:
        if len(a) > 2:
            mid = len(a)/2
            left = mergesort(a[:mid+1])
            right = mergesort(a[mid+1:])
            return merge(left, right)

        else:
            if a[0] > a[1]:
                a[1],a[0] = a[0],a[1]

        return a

#This functions has central logic, it does the actual sort
def merge (left, right):
    i=0
    j=0
    l = len(left)
    r = len(right)
    mergelist = []
    while(i < l and j < r):
        if left[i] <= right[j]:
            mergelist.append(left[i])
            i = i + 1
        else:
            mergelist.append(right[j])
            j = j + 1

    if i < l:
        mergelist = mergelist + left[i:]

    if j < r:
        mergelist = mergelist + right[j:]

    return mergelist;




