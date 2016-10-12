def findPath(treelist):
    #For leaf nodes return height and path values zero, this is recursion terminating condition
    if treelist == []:
        return [0,0]

    else:
        #left and right list stores height and path information.
        left = findPath(treelist[0])
        right = findPath(treelist[2])

        #Max of height of left , right subtree + node height (1) is the Final height of the tree
        height = max(left[0], right[0]) + 1

        #Max of left tree path, right tree path , sum of left tree height and right tree height is the Final longest path
        path = max(left[0] + right[0], max(left[1],right[1]))

        return [height,path]

def longest(treelist):
    pathval = findPath(treelist)
    return max([pathval[0]-1,pathval[1]])












