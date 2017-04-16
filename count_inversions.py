nbrs = []

with open('QuickSort.txt', 'r') as infile:
    for line in infile:
        nbrs.append(int(line.strip()))

tst = [3,2,8,5,1,4,7,6]

def quick_sort(a,l,r):
    p = a[l]
    i = l + 1
    comps = 0
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
        if l < i-2:
            comps += quick_sort(a,l,i-2)
        if i < r:
            comps += quick_sort(a,i,r)
        return comps

def quick_sortb(a,l,r):
    p = a[r]
    i = l
    comps = 0
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
        if l < i-1:
            comps += quick_sortb(a,l,i-1)
        if i+1 < r:
            comps += quick_sortb(a,i+1,r)
        return comps

#print(nbrs[:10])
print(tst)

print(quick_sortb(tst,0,len(tst)-1))
print(quick_sortb(nbrs,0,len(nbrs)-1))
print(tst)

print(nbrs[:20])