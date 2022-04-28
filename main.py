from traceback import print_tb
import sys
import os
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Anthropos')


WHITE = (255, 255, 255)
SKY_BLUE = (50, 153, 204)
FPS = 60
VEL = 8
bomber_width, bomber_height = (99, 72)
kubis_vel = 5



# letadlo obrázek, velikost a otočení
aircraft_image = pygame.image.load(os.path.join("images", "aircraft.png"))
aircraft_image = pygame.transform.rotate(pygame.transform.scale(aircraft_image, (99, 72)), 270)

background = pygame.image.load(os.path.join("images", "background.png"))
les_img = pygame.image.load(os.path.join("images", "forest.png"))


def draw_window(bomber, les): #vykreslí věci ve hře
    WIN.blit(background, (0, 0))
    WIN.blit(les_img, (les.x, les.y))
    WIN.blit(aircraft_image, (bomber.x, bomber.y))
    pygame.display.update()

def bomber_movement(key_pressed, bomber):       #pohybu bomberu
    if key_pressed[pygame.K_a] and bomber.x - VEL > 0:  # Left
        bomber.x -= VEL
    if key_pressed[pygame.K_d] and bomber.x + VEL + bomber_width < 900:  # Right
        bomber.x += VEL
    if key_pressed[pygame.K_w] and bomber.y - VEL > 0:  # UP
        bomber.y -= VEL
    if key_pressed[pygame.K_s] and bomber.y + VEL + bomber_height < 500 - 25:  # Down
        bomber.y += VEL

def les_move(les):
    les.x = les.x - 4
    if les.x < -150:
        les.x = 900

def main():
    pygame.init()
    bomber = pygame.Rect(100, 150, bomber_width, bomber_height)
    les = pygame.Rect(600, 375, 200, 200)
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        key_pressed = pygame.key.get_pressed() #proměná pro další funkci
        bomber_movement(key_pressed, bomber)   #volání pohybu bomberu

        les_move(les)
        draw_window(bomber, les)






if __name__ ==  "__main__":
    main()


