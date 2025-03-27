import copy


def brute_force(E, k, v, n, act_k, chosen):
    if act_k > k:
        return False
    if v == n:
        if act_k < k:
            return False
        if act_k == k:
            for (v1, v2) in E:
                if not chosen[v1] and not chosen[v2]:
                    return False
            print([int(x) for x in chosen])
            return True
    dont_take = brute_force(E, k, v + 1, n, act_k, chosen)
    if dont_take:
        return True
    chosen_copied = copy.deepcopy(chosen)
    chosen_copied[v] = True
    return brute_force(E, k, v + 1, n, act_k + 1, chosen_copied)


global ops1

def recursion_with_returns(E, k, act_e, act_k, chosen):
    global ops1
    ops1 += 1
    #print(ops)
    if act_k > k:
        return False
    if act_e == len(E):
        print([int(x) for x in chosen])
        return True
    start = act_e
    v, w = -1, -1
    while True:
        if act_e == len(E):
            print([int(x) for x in chosen])
            return True
        v, w = E[act_e]
        if not chosen[v] and not chosen[w]:
            break
        act_e += 1
    v, w = E[act_e]
    chosen_copied = copy.deepcopy(chosen)
    chosen[v] = True
    take_left = recursion_with_returns(E, k, act_e + 1, act_k + 1, chosen)
    if take_left:
        return True
    chosen_copied[w] = True
    return recursion_with_returns(E, k, act_e + 1, act_k + 1, chosen_copied)


def get_neighbours_list(E, n):
    neigh = [[] for _ in range(n)]
    for (v, w) in E:
        neigh[v].append(w)
        neigh[w].append(v)
    return neigh

def rec_returns_better(E, k, act_k, forbid, chosen):
    global ops1


V = 8
edges = [(1, 2), (0, 2), (2, 3), (3, 4), (3, 5), (5, 6), (5, 7)]
outer_k = 3
ch = [False] * V
forb = [False] * V
print(brute_force(edges, outer_k, 0, V, 0, ch))
ops1 = 0
print(recursion_with_returns(edges, outer_k, 0, 0, ch))
print(ops1)
ops1 = 0
print(rec_returns_better(edges, outer_k, 0, forb, ch))
