kol_seleniy = int(input())
selo_input = list(map(int, input().split()))
selo_do_nachla = []
for i in range(len(selo_input)):
    selo_do_nachla.append((selo_input[i], i + 1))
selo_do_nachla.sort()
kol_bomb = int(input())
bomb_input = list(map(int, input().split()))
bomb_do_nachla = []
for i in range(len(bomb_input)):
    bomb_do_nachla.append((bomb_input[i], i + 1))
bomb_do_nachla.sort()


def blijnee(rast, list_bomb, ind):
    close_so_far = abs(rast - list_bomb[ind][0])
    tul_of_bomb = list_bomb[0]
    ind_next = ind
    for k in range(ind + 1, len(list_bomb)):
        if close_so_far > abs(rast - list_bomb[k][0]):
            close_so_far = abs(rast - list_bomb[k][0])
            tul_of_bomb = list_bomb[k]
            ind_next = k - 1
        else:
            break
    return tul_of_bomb, ind_next


nxt = 0
rslt = dict()
for selo in selo_do_nachla:
    bomb = (selo[1], blijnee(selo[0], bomb_do_nachla, nxt))
    nxt = bomb[1][1]
    rslt[selo[1]] = bomb[1][0][1]
for xz in range(1, len(rslt) + 1):
    print(rslt.get(xz), end=' ')
