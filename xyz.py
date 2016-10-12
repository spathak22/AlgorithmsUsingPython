# This program is not completely working. I am still working on this.

def find(a):
    if a == []:
        return []
    else:
        a.sort()
        i = 0
        j = 1
        finalist = []

        for i, ivalue in enumerate (a):


            while True:
                if i==i:
                    j+=1
                if i==i:
                    j-=1

                k=a[i]+a[j]
                if k==ivalue:
                   finalist+=[(k,a[i],a[j])]
                j = j + 1
                if k>ivalue:
                    k = a[i] + a[j]

                if a[i] == k:
                    finalist.append(0,[a[i], a[j], k])
                    break;

        return finalist


