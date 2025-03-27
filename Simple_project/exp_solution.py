import copy, sys
sys.setrecursionlimit(10 * 1000)
W, H, S = [int(x) for x in str(input()).split(' ')]
arr = [[0 for _ in range(W)] for _ in range(H)]

global rec_count
rec_count = 0
global found
found = False

def print_arr(arr):
    for i in range (len(arr)):
        print(arr[i])

def conv(c):
    if(c == "#" or c == "O"):
        return 1
    if(c == "."):
        return 0
    if(c == "*"):
        return 2

def conv_move(move):
    moves_arr = ["D", "G", "P", "L"]
    return moves_arr[move]

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def solve(act_arr, pos, prev_move, act_score, seq):
    global rec_count, found

    if(found):
        return
    rec_count += 1
    x, y = pos
    res = 0
    for i in range(4):
        temp_seq = seq
        temp_x, temp_y = x + moves[i][0], y + moves[i][1]
        if i == prev_move or act_arr[temp_x][temp_y] == 1:
            continue
        temp_seq += conv_move(i)
        arr_copied = copy.deepcopy(act_arr)
        act_res = 0
        while(arr_copied[temp_x][temp_y] != 1):
            if(found):
                return
            if arr_copied[temp_x][temp_y] == 2:
                act_res += 1
            arr_copied[temp_x][temp_y] = 1
            temp_x, temp_y = temp_x + moves[i][0], temp_y + moves[i][1]
        if(act_score + act_res >= S):
            found = True
            print(temp_seq)
            return 
        solve(arr_copied, (temp_x - moves[i][0], temp_y - moves[i][1]), i, act_score + act_res, temp_seq)

    return res

start = [0, 0]
for i in range(H):
    l = str(input())
    for j in range(W):
        if l[j] == "O":
            start[0], start[1] = i, j
        arr[i][j] = conv(l[j])

solve(arr, start, -1, 0, "")

#print(found)
