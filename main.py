from traceback import print_tb
import sys
import os
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bayraktar')


WHITE = (255, 255, 255)
SKY_BLUE = (50, 153, 204)
FPS = 60
VEL = 5


aircraft_image = pygame.image.load(os.path.join("images", "aircraft.png"))
aircraft_image = pygame.transform.rotate(pygame.transform.scale(aircraft_image, (99, 72)), 270)

def draw_window(bomber):
    WIN.fill(SKY_BLUE)
    WIN.blit(aircraft_image, (bomber.x, bomber.y))
    pygame.display.update()

def main():
    pygame.init()

    bomber = pygame.Rect(100, 150, 99, 72)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]: #Left
            bomber.x -= VEL
        draw_window(bomber)
        if key_pressed[pygame.K_d]: #Right
            bomber.x += VEL
        draw_window(bomber)
        if key_pressed[pygame.K_w]: #UP
            bomber.y -= VEL
        draw_window(bomber)
        if key_pressed[pygame.K_s]: #Down
            bomber.y += VEL

        draw_window(bomber)





if __name__ ==  "__main__":
    main()


