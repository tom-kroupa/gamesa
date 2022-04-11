from traceback import print_tb
import pygame

print('Hello world')


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False

    pygame.quit()

