#Buggy qsort
def qsort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [qsort(left)] + [pivot] + [qsort(right)]

#To sort the tree inorder
def sort(treelist):
    if treelist == []:
        return []
    else:
        print treelist
        return sort(treelist[0]) + [treelist[1]] + sort(treelist[2])

#To search an element in tree
def search(treelist, e):
    if treelist == []:
        return False
    else:
        if e == treelist or e == treelist[1]:
            return True
        return search(treelist[0],e) or search(treelist[2],e)

# To insert an element in a tree




