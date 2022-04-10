import quick_union

inFile = open('number.txt', 'r', encoding='utf8')
QU = quick_union
N = int(inFile.readline().strip())
arr = QU.inition(N)
#print(arr)
for line in inFile:
    line = line.strip().split(' ')
    p=int(line[0])
    q=int(line[1])

    if QU.connected(p,q) is False:
        arr = QU.union(p,q)
        #print(p, ' ', q)
print(arr)

inFile.close()
