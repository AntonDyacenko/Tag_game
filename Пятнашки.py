import pygame
import random

pygame.init()
size0 = width, height = 801, 801
screen = pygame.display.set_mode(size0)
running = True
num_move = 0

first = True

elem1 = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (3, 0): 4, (0, 1): 5, (1, 1): 6, (2, 1): 7, (3, 1): 8, (0, 2): 9, (1, 2): 10,
         (2, 2): 11, (3, 2): 12, (0, 3): 13, (1, 3): 14, (2, 3): 15, (3, 3): 0}


def search_name(name):
    for i in elem1:
        if elem1[i] == name:
            return i
    return False


def draw_table():
    for x in range(5):
        pygame.draw.line(screen, (255, 255, 255), ((width - 1) / 4 * x, 0), ((width - 1) / 4 * x, width - 1))
    for y in range(5):
        pygame.draw.line(screen, (255, 255, 255), (0, (height - 1) / 4 * y), (height - 1, (height - 1) / 4 * y))


def search_coordinate(pos):
    return (pos[0] * 4 // width, pos[1] * 4 // height)


def convert_coordinate(pos):
    return (pos[0] * (width // 4) + 2, pos[1] * (height // 4) + 2)


def draw_15():
    for i in elem1:
        if elem1[i] != 0:
            p = convert_coordinate(i)
            pygame.draw.rect(screen, (0, 100, 100), (p[0], p[1], 198, 198))
            t = str(elem1[i])
            f1 = pygame.font.Font(None, 100)
            text1 = f1.render(t, 1, (255, 255, 0))
            place = text1.get_rect(center=(p[0] + width // 8, p[1] + height // 8))
            text2 = f1.render(t, 1, (100, 100, 0))
            place2 = text1.get_rect(center=((p[0]) + width // 8 + 3, p[1] + height // 8 + 3))
            screen.blit(text2, place2)
            screen.blit(text1, place)


def new_pos(pos):
    if elem1[pos] != 0:
        pos_0 = search_name(0)
        pos_name = elem1[pos]
        if pos == (pos_0[0] - 1, pos_0[1]) or pos == (pos_0[0], pos_0[1] - 1) or pos == (
                pos_0[0], pos_0[1] + 1) or pos == (pos_0[0] + 1, pos_0[1]):
            elem1[pos] = 0
            elem1[pos_0] = pos_name


def search_win():
    if num_move != 0:
        if elem1 == {(0, 0): 1, (1, 0): 2, (2, 0): 3, (3, 0): 4, (0, 1): 5, (1, 1): 6, (2, 1): 7, (3, 1): 8, (0, 2): 9,
                     (1, 2): 10,
                     (2, 2): 11, (3, 2): 12, (0, 3): 13, (1, 3): 14, (2, 3): 15, (3, 3): 0}:
            t = 'You win!'
            f1 = pygame.font.Font(None, 100)
            text1 = f1.render(t, 1, (255, 100, 0))
            place = text1.get_rect(center=(width // 2, height // 2))
            text2 = f1.render(t, 1, (100, 0, 0))
            place2 = text1.get_rect(center=((width + 5) // 2, (height + 5) // 2))
            screen.blit(text2, place2)
            screen.blit(text1, place)


def search_near(pos_0):
    sp = []
    for pos in elem1:
        if pos == (pos_0[0] - 1, pos_0[1]) or pos == (pos_0[0], pos_0[1] - 1) or pos == (
                pos_0[0], pos_0[1] + 1) or pos == (pos_0[0] + 1, pos_0[1]):
            sp.append(pos)
    return sp


def mixing():
    a = random.randint(300, 500)
    while a != 0:
        pos_0 = search_name(0)
        sp = search_near(pos_0)
        new_pos(random.choice(sp))
        a -= 1


while running:
    if first:
        mixing()
        first = False
    screen.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_pos(search_coordinate(event.pos))
            num_move += 1
    draw_table()
    draw_15()
    search_win()
    pygame.display.flip()
