from traceback import print_tb
import pygame

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False

    pygame.quit()