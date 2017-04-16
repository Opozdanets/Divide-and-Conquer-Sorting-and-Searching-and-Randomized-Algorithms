nbrs = []

with open('QuickSort.txt', 'r') as infile:
    for line in infile:
        nbrs.append(int(line.strip()))

#test array
tst = [3,2,8,5,1,4,7,6]

def quick_sort(a,l,r):
    #Key subroutine for quick sort where most left element is chosen as a pivot
    p = a[l]
    i = l + 1
    comps = 0
    #Basic case to exit recursion
    if r == l + 1:
        comps += 1
        if a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
        return comps
    else:
        comps += r - l
        for j in range(l+1,r+1):
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[l], a[i-1] = a[i-1], a[l]
        #Recursion call for the part less then the pivot
        if l < i-2:
            comps += quick_sort(a,l,i-2)
        # Recursion call for the part bigger then the pivot
        if i < r:
            comps += quick_sort(a,i,r)
        return comps

def quick_sortb(a,l,r):
    # Key subroutine for quick sort where most right element is chosen as a pivot
    p = a[r]
    i = l
    comps = 0
    # Basic case to exit recursion
    if r == l + 1:
        comps += 1
        if a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
        return comps
    else:
        comps += r - l
        for j in range(l,r):
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[r], a[i] = a[i], a[r]
        # Recursion call for the part less then the pivot
        if l < i-1:
            comps += quick_sortb(a,l,i-1)
        # Recursion call for the part bigger then the pivot
        if i+1 < r:
            comps += quick_sortb(a,i+1,r)
        return comps

def quick_sortm(a,l,r):
    # Key subroutine for quick sort where most right element is chosen as a pivot
    comps = 0
    # Basic case to exit recursion
    if r == l + 1:
        comps += 1
        if a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
        return comps
    else:
        #Choosing "median" elenet as a pivot
        q = l + ((r - l) // 2)
        if (a[l] < a[q] and a[q] < a[r]) or (a[l] > a[q] and a[q] > a[r]):
            p = a[q]
            a[l], a[q] = a[q], a[l]
        elif (a[l] < a[q] and a[r] < a[l]) or (a[l] > a[q] and a[r] > a[l]):
            p = a[l]
        elif (a[l] < a[r] and a[r] < a[q]) or (a[l] > a[r] and a[r] > a[q]):
            p = a[r]
            a[l], a[r] = a[r], a[l]
        i = l + 1
        comps += r - l
        for j in range(l+1,r+1):
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[l], a[i-1] = a[i-1], a[l]
        # Recursion call for the part less then the pivot
        if l < i-2:
            comps += quick_sortm(a,l,i-2)
        # Recursion call for the part bigger then the pivot
        if i < r:
            comps += quick_sortm(a,i,r)
        return comps

print('Num of invers with a left pivot =', quick_sort(nbrs,0,len(nbrs)-1))

#Reload initial array
nbrs.clear()
with open('QuickSort.txt', 'r') as infile:
    for line in infile:
        nbrs.append(int(line.strip()))

print('Num of invers with a right pivot =', quick_sortb(nbrs,0,len(nbrs)-1))

#Reload initial array
nbrs.clear()
with open('QuickSort.txt', 'r') as infile:
    for line in infile:
        nbrs.append(int(line.strip()))

print('Num of invers with a median pivot =', quick_sortm(nbrs,0,len(nbrs)-1))