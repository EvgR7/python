def inition(N):
    arr = []
    i = 0
    while i < N:
        arr.append(i)
        i+=1
    return arr

def union(arr,p,q):
    pid = arr[p]
    qid = arr[q]
    i = 0
    while i < len(arr):
        if arr[i] == pid:
            arr[i] = qid
        i+=1
    return arr

def connected(arr,p,q):
    return arr[p] == arr[q]

def find(p):
    return 0

def count():
    return 0

