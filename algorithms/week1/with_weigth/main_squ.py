import super_quick_union

inFile = open('number.txt', 'r', encoding='utf8')
SQU = super_quick_union
N = int(inFile.readline().strip())
arr = SQU.inition(N)
#print(arr)
for line in inFile:
    line = line.strip().split(' ')
    p=int(line[0])
    q=int(line[1])

    if SQU.connected(p,q) is False:
        arr = SQU.union(p,q)
        #print(p, ' ', q)
print(arr)

inFile.close()