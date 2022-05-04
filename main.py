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
VEL = 7
bomber_width, bomber_height = (99, 72)
kubis_vel = 4



# letadlo obrázek, velikost a otočení
aircraft_image = pygame.image.load(os.path.join("images", "plane.png"))
aircraft_image = pygame.transform.rotate(pygame.transform.scale(aircraft_image, (150, 150)), 270)

background = pygame.image.load(os.path.join("images", "background.jpg"))
les_img = pygame.image.load(os.path.join("images", "forest.png"))
kubis_img = pygame.image.load(os.path.join("images", "kubis.png"))





def draw_window(bomber, les, kubis_list): #vykreslí věci ve hře
    WIN.blit(background, (0, 0))
    WIN.blit(les_img, (les.x, les.y))
    WIN.blit(aircraft_image, (bomber.x, bomber.y))
    for kubis in kubis_list:
        WIN.blit(kubis_img, (kubis.x, kubis.y))
    pygame.display.update()

def bomber_movement(key_pressed, bomber):       #pohybu bomberu
    if key_pressed[pygame.K_a] and bomber.x - VEL > -10:  # Left
        bomber.x -= VEL
    if key_pressed[pygame.K_d] and bomber.x + VEL + bomber_width < 860:  # Right
        bomber.x += VEL
    if key_pressed[pygame.K_w] and bomber.y - VEL > 0:  # UP
        bomber.y -= VEL
    if key_pressed[pygame.K_s] and bomber.y + VEL + bomber_height < 430:  # Down
        bomber.y += VEL

def les_move(les):
    les.x = les.x - 4
    if les.x < -150:
        les.x = 900


def main():
    pygame.init()
    bomber = pygame.Rect(100, 150, bomber_width, bomber_height)
    les = pygame.Rect(600, 375, 200, 200)
    kubis_list = []
    clock = pygame.time.Clock()


    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE :
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    kubis = pygame.Rect(bomber.x, bomber.y, 2, 2)
                    kubis_list.append(kubis)



        key_pressed = pygame.key.get_pressed() #proměná pro další funkci

        bomber_movement(key_pressed, bomber)   #volání pohybu bomberu

        for kubis in kubis_list:
            kubis.y = kubis.y + kubis_vel
            kubis.x = kubis.x + kubis_vel / 2

        les_move(les)
        draw_window(bomber, les, kubis_list)




if __name__ ==  "__main__":
    main()


