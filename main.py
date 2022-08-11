# coding=utf-8
# This is a sample Python script.
import pygame
from dataclasses.game import Game

screen_dim = (1200, 800)
pygame.init()
display = pygame.display.set_mode(screen_dim)
pygame.display.set_caption('Azul')
game = Game(display, screen_dim)

while True:  # main game loop
    game.listen()
    # tile_circle.draw_tiles_from_bag(4)
    # tile_circle.show(display, 100, 50)
    game.show()
    pygame.display.update()
