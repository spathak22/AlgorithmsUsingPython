inversion_count = 0
# intermediate merge sort logic used to count the inversions
def msort(a):
    if a == []:
        return []
    if(len(a)==1):
        return a
    else:
        if len(a) > 2:
            mid = len(a)/2
            left = msort(a[:mid+1])
            right = msort(a[mid+1:])
            return merge(left, right)

        else:
            if a[0] > a[1]:
                a[1],a[0] = a[0],a[1]
                global inversion_count
                inversion_count += 1

        return a

# Helper merge function
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
            global inversion_count
            inversion_count = inversion_count + len(left[i:])

    if i < l:
        mergelist = mergelist + left[i:]

    if j < r:
        mergelist = mergelist + right[j:]


    return mergelist;

def num_inversions(a):
    msort(a)
    return inversion_count


