# 1 - Import library
import pygame
import os
import sys
import random
import logging
import time

from Tile import *


def random_chooser():
    path = './img'
    if len(sys.argv) == 2:
        path = sys.argv[1]

    files = os.listdir(path)
    random_fold = random.choice(files)
    logging.warning(random_fold)
    return random_fold


# Initialize the game
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False, False]
playerpos = [100, 100]

logic_map = Map(x=3, y=2)

# Load images
background = pygame.image.load("resources/puzzle_background.jpg")
background = pygame.transform.scale(background, (800, 600))

random_choose = random_chooser()

# carica le immagini dei pezzi
img_piece1 = pygame.image.load("img/"+random_choose+"/1.jpg")
img_piece2 = pygame.image.load("img/"+random_choose+"/2.jpg")
img_piece3 = pygame.image.load("img/"+random_choose+"/3.jpg")
img_piece4 = pygame.image.load("img/"+random_choose+"/4.jpg")
img_piece5 = pygame.image.load("img/"+random_choose+"/5.jpg")
img_piece6 = pygame.image.load("img/"+random_choose+"/6.jpg")
img_completed = pygame.image.load("finito.png")


# Crea thumbnail dell'immagine completa
full_img = pygame.image.load("img/"+random_choose+"/"+random_choose+".jpg")
full_img = pygame.transform.scale(full_img, (150, 125))

# scala immagini a 200x200 px
square_piece_size = 200
img_piece1 = pygame.transform.scale(img_piece1, (square_piece_size, square_piece_size))
img_piece2 = pygame.transform.scale(img_piece2, (square_piece_size, square_piece_size))
img_piece3 = pygame.transform.scale(img_piece3, (square_piece_size, square_piece_size))
img_piece4 = pygame.transform.scale(img_piece4, (square_piece_size, square_piece_size))
img_piece5 = pygame.transform.scale(img_piece5, (square_piece_size, square_piece_size))
img_piece6 = pygame.transform.scale(img_piece6, (square_piece_size, square_piece_size))
img_completed = pygame.transform.scale(img_completed, (200, 200))

placed_tile = [False, True, False, False, False, False, False]


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.draw.rect(screen, BLUE, (200, 150, 0, 0))

# default tile 5 set as occuped and finished
logic_map.tiles5.set_finish()
logic_map.tiles5.set_occupation()

pos_x = 100
pos_y = 100
actual_active_tile = 2
record_pos = [[0, 0], [pos_x, pos_y]]
# 4 - keep looping through


def reset_all(x, y, placed, active_tile, record_position):
    x = 100
    y = 100
    placed = placed_tile = [False, True, False, False, False, False, False]
    active_tile = 2
    record_position = [[0, 0], [pos_x, pos_y]]


while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    # 6 - draw the screen elements
    screen.blit(background, (0, 0))
    screen.blit(full_img, (25, 650))
    # screen.blit(img_piece6, (logic_map.tiles6.get_tile_origin_x(), logic_map.tiles6.get_tile_origin_y()))

    screen.blit(img_piece1, (500, 300))
    if not placed_tile[2]:
        screen.blit(img_piece2, (pos_x, pos_y))
    elif not placed_tile[3]:
        screen.blit(img_piece3, (pos_x, pos_y))
    elif not placed_tile[4]:
        screen.blit(img_piece4, (pos_x, pos_y))
    elif not placed_tile[5]:
        screen.blit(img_piece5, (pos_x, pos_y))
    elif not placed_tile[6]:
        screen.blit(img_piece6, (pos_x, pos_y))

    if placed_tile[2]:
        screen.blit(img_piece2, (record_pos[2], record_pos[2]))
    if placed_tile[3]:
        screen.blit(img_piece3, (record_pos[3], record_pos[3]))
    if placed_tile[4]:
        screen.blit(img_piece4, (record_pos[4], record_pos[4]))
    if placed_tile[5]:
        screen.blit(img_piece5, (record_pos[5], record_pos[5]))
    if placed_tile[6]:
        screen.blit(img_piece6, (record_pos[6], record_pos[6]))
        screen.blit(img_completed, (400, 200))
        time.sleep(3)

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True
            elif event.key == pygame.K_g:
                keys[4] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
            elif event.key == pygame.K_g:
                keys[4] = False

    # 9 - Move player
    if keys[0]:
        pos_y -= square_piece_size
        playerpos[1] -= 5
        time.sleep(0.5)
    elif keys[2]:
        pos_y += square_piece_size
        playerpos[1] += 5
        time.sleep(0.5)
    if keys[1]:
        pos_x -= square_piece_size
        playerpos[0] -= 5
        time.sleep(0.5)
    elif keys[3]:
        pos_x += square_piece_size
        playerpos[0] += 5
        time.sleep(0.5)
    if keys[4]:
        placed_tile[actual_active_tile] = True
        actual_active_tile += 1
        record_pos.append([pos_x, pos_y])
        pos_x = 100
        pos_y = 100
        time.sleep(0.5)


# todo aggiungere immagini
# todo aggiungere bottoni reset e nuovo
