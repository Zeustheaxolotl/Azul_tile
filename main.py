# coding=utf-8
# This is a sample Python script.
import pygame
import sys
from dataclasses.tilebag import Tilebag
from dataclasses.tilecircle import TileCircle

# from random import sample

# ran = random.sample(range(0, 99), 36)
# print(ran)
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# tile_bag = []
# total_tiles = []
# colors = ['red', 'black', 'blue', 'teal', 'yellow']
# rnums = []
# turn = 0
# round = 0
# row = False


# for y in colors:
# for x in range(0, 20, 1):
# new_tile = Tile("tile bag", y)
#  total_tiles.append(new_tile)

# for x in range(0, 100, 1):
# total_tiles[x].re_tile_bag()

# print(tile_bag)
# TileCircles = []
# TileCircle_1= TileCircle()
# TileCircle_1.calc_tiles()
# TileCircle_1.show()
tile_bag = Tilebag()
tile_bag.make_tiles()
tile_circle = TileCircle(tile_bag)
pygame.init()
display = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Azul')
while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tile_circle.show(display, 100, 50)
    pygame.display.update()
