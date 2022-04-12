arr = []
sz = []

def inition(N):
    i = 0
    while i < N:
        arr.append(i)
        i+=1
        sz.append(1)
    #print(sz,arr)
    return arr

def root(i):
    while i != arr[i]:
        i = arr[i]
    return i

def connected(p,q):
    return root(p) == root(q)

def union(p,q):
    i = root(p)
    j = root(q)
    if i == j:
        return arr
    if sz[i] < sz[j]:
        arr[i] = j
        sz[i] += sz[j]
    else:
        arr[j] = i
        sz[j] += sz[i]
    return arr