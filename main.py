import pygame
import sys
import traceback

pygame.init()
pygame.mixer.init()

background_size = width, height = 480, 700
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption("Aircraft Battle_GG")

background = pygame.image.load()
