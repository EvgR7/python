import Union_find
inFile = open('number.txt', 'r', encoding='utf8')
UF = Union_find
N = int(inFile.readline().strip())
arr = UF.inition(N)
#print(arr)
for line in inFile:
    line = line.strip().split(' ')
    p=int(line[0])
    q=int(line[1])

    if UF.connected(arr,p,q) is False:
        arr = UF.union(arr,p,q)
        #print(p, ' ', q)
print(arr)

inFile.close()
