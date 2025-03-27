import pygame

fopen = open("dane.txt", "r")
W, H, S = [int(x) for x in str(fopen.readline()).split()]
arr = [[0 for _ in range(W)] for _ in range(H)]


def conv(c):
    if c == "#":
        return -1
    if c == "0":
        return 2
    if (c == "."):
        return 0
    if (c == "*"):
        return 1

global cat_pos
cat_pos = [0, 0]
for i in range(H):
    l = str(fopen.readline())
    for j in range(W):
        if l[j] == "O":
            cat_pos = i, j
        arr[i][j] = conv(l[j])
print(*arr, sep="\n")

print(cat_pos)

pygame.init()

win_size = 35
WIDTH, HEIGHT = W * win_size, H * win_size

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plansza w Pygame")
cat_img = pygame.image.load("cat_blue.png")
cat_img = pygame.transform.scale(cat_img, (win_size, win_size))



def draw_grid():

    for x in range(W):
        pygame.draw.line(display, BLACK, (win_size * x, 0), (win_size * x, HEIGHT))
    for y in range(H):
        pygame.draw.line(display, BLACK, (0, win_size * y), (WIDTH, win_size*y))

def draw_rect(display, i, j, col):
    pygame.draw.rect(display, col, (i * win_size, j * win_size, win_size, win_size))


def move_cat(pos, move_type):
    global cat_pos
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    x, y = pos
    arr[x][y] = 2
    x += moves[move_type][0]
    y += moves[move_type][1]

    while arr[x][y] != -1 and arr[x][y] != 2:
        arr[x][y] = 2
        x, y = x + moves[move_type][0], y + moves[move_type][1]

    cat_pos = x - moves[move_type][0], y - moves[move_type][1]

running = True
while running:

    display.fill(WHITE)
    draw_rect(display, cat_pos[1], cat_pos[0], BLUE)
    for i in range(H):
        for j in range(W):
            if i == cat_pos[0] and j == cat_pos[1]:
                display.blit(cat_img, (cat_pos[1] * win_size, cat_pos[0] * win_size))
            elif arr[i][j] == -1:
                draw_rect(display, j, i, BLACK)
            elif arr[i][j] == 1:
                draw_rect(display, j, i, RED)
            elif arr[i][j] == 2:
                draw_rect(display, j, i, BLUE)

    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_cat(cat_pos, 1)
            if event.key == pygame.K_s:
                move_cat(cat_pos, 0)
            if event.key == pygame.K_a:
                move_cat(cat_pos, 3)
            if event.key == pygame.K_d:
                move_cat(cat_pos, 2)

    pygame.display.flip()

pygame.quit()
