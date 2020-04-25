fhandle = open('input.txt', 'r', encoding='utf-8')
weekend = set()
strikes = set()
count = 0
year = 0
for line in fhandle:
    if count == 0:
        year = int(line.split()[0])
        for i in range(6, year + 1, 7):
            weekend.add(i)
            if i + 1 < int(line.split()[0]):
                weekend.add(i + 1)
        count += 1
    else:
        strikes |= set(range(int(line.split()[0]),
                             year + 1, int(line.split()[1])))


print(len(strikes - weekend))
