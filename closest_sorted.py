from bisect import bisect

def find(a,xsrch,k):
    count = 0
    finlist = []
    if a == [] or k > len(a):
        return "Either array is empty or K is greater than array length"
    else:
        lastIndex = len(a)
        # if elemtent to be searched is greater than last elem then return k element from right
        if xsrch >= a[lastIndex - 1]:
            return a[(lastIndex - k):]

        #if elemtent to be searched is less than first elem then return k element from left
        if xsrch <= a[0]:
            return a[:k]

        right = bisect(a, xsrch)
        left = right - 1
        #if left is less than right element then add left element
        while (count < k and left >=0 and right <len(a)):
            rvalue = abs(a[right] - xsrch)
            lvalue = abs(a[left] - xsrch)

            if (lvalue <= rvalue):
                finlist.insert(0,a[left])
                left = left - 1
            else:
                finlist.append(a[right])
                right = right + 1
            count = count + 1

        #if left goes to less than zero or right goes to more than list size then simply add remaining element from list
        if count<k:
            finlist=a[left-(k-len(finlist))+1:left+1]+finlist
            finlist=finlist+a[right:right+2]


    return finlist


