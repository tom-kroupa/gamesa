from traceback import print_tb
import sys
import os
import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Anthropos')

font = pygame.font.SysFont("Verdana", 40)

WHITE = (255, 255, 255)
SKY_BLUE = (50, 153, 204)
GREEN = (0, 164, 0)
FPS = 60
VEL = 7
bomber_width, bomber_height = (99, 72)
kubis_vel = 4
max_kubis = 2
vydadek = pygame.USEREVENT + 1
bullet_vel = 10
les_vel = 6

# letadlo obrázek, velikost a otočení
aircraft_image = pygame.image.load(os.path.join("images", "plane.png"))
aircraft_image = pygame.transform.rotate(pygame.transform.scale(aircraft_image, (150, 150)), 270)
background = pygame.image.load(os.path.join("images", "background.jpg"))
les_img = pygame.image.load(os.path.join("images", "forest.png"))
les_img = pygame.transform.scale(les_img, (250, 250))
kubis_img = pygame.image.load(os.path.join("images", "kubis.png"))
kubis_img = pygame.transform.scale(kubis_img, (100, 100))
bullet_img = pygame.image.load(os.path.join("images", "bullets.png"))
bullet_img = pygame.transform.rotate(pygame.transform.scale(bullet_img, (45, 45)), 180)


def draw_window(bomber, les, kubis_list, score, bullet): #vykreslí věci ve hře
    WIN.blit(background, (0, 0))
    WIN.blit(les_img, (les.x, les.y))
    WIN.blit(bullet_img, (bullet.x, bullet.y))
    score_text = font.render("Score" + str(score), 1, GREEN)
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
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
    les.x = les.x - les_vel
    if les.x < -250:
        les.x = 1100

def bullet_move(bullet):
    bullet.x = bullet.x + bullet_vel
    if bullet.x > 900:
        bullet.y = random.randrange(10, 320)
        bullet.x = -100

def kubis_handle(kubis_list, les):
    for kubis in kubis_list:
        kubis.y = kubis.y + kubis_vel
        kubis.x = kubis.x - kubis_vel / 3
        if les.colliderect(kubis):
            pygame.event.post(pygame.event.Event(vydadek))
            kubis_list.remove(kubis)
        elif kubis.y > 500:
            kubis_list.remove(kubis)

def handle_bullet(bullet, bomber):
    if bullet.colliderect(bomber):
        draw_end("Game Over")
        main()

def draw_end(text):
    draw_text = font.render(text, 1, GREEN)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_width()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    pygame.init()
    bomber = pygame.Rect(100, 150, bomber_width, bomber_height)
    les = pygame.Rect(1000, 320, 250, 250)
    kubis_list = []
    score = 0
    bullet = pygame.Rect(-300, random.randrange(10, 320), 15, 45)

    clock = pygame.time.Clock()


    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE :
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(kubis_list) < max_kubis:
                    kubis = pygame.Rect(bomber.x, bomber.y, 2, 2)
                    kubis_list.append(kubis)

            if event.type == vydadek:
                score = score + 1


        key_pressed = pygame.key.get_pressed() #proměná pro další funkci
        bomber_movement(key_pressed, bomber)   #volání pohybu bomberu
        kubis_handle(kubis_list, les)
        bullet_move(bullet)
        les_move(les)
        handle_bullet(bullet, bomber)
        draw_window(bomber, les, kubis_list, score, bullet)


if __name__ ==  "__main__":
    main()


