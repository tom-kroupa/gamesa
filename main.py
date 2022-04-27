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

# kubis = pygame.image.load(os.path.join(("images", "kubis.png")))


background = pygame.image.load(os.path.join("images", "background.png"))


def draw_window(bomber): #vykreslí věci ve hře
    WIN.blit(background, (0, 0))
    WIN.blit(aircraft_image, (bomber.x, bomber.y))
    pygame.display.update()

def main():
    pygame.init()

    bomber = pygame.Rect(100, 150, bomber_width, bomber_height)
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         kubis = pygame.Rect(bomber.x + bomber.width, bomber.y + bomber.height, 20, 20)




        key_pressed = pygame.key.get_pressed() #pohyb bomber a hranice kam může
        if key_pressed[pygame.K_a] and bomber.x - VEL > 0:  #Left
            bomber.x -= VEL
        draw_window(bomber)
        if key_pressed[pygame.K_d] and bomber.x + VEL + bomber_width < 900: #Right
            bomber.x += VEL
        draw_window(bomber)
        if key_pressed[pygame.K_w] and bomber.y - VEL > 0: #UP
            bomber.y -= VEL
        draw_window(bomber)
        if key_pressed[pygame.K_s]and bomber.y + VEL + bomber_height < 500 - 25: #Down
            bomber.y += VEL

        draw_window(bomber)





if __name__ ==  "__main__":
    main()


