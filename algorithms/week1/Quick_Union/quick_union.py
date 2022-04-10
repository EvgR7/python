arr = []

def inition(N):
    i = 0
    while i < N:
        arr.append(i)
        i+=1
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
    arr[i] = j
    return arr


