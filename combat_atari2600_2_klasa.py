import pygame
import math
import random
import time


def main():

    #start z bazowymi parametrami
    pygame.init()

    #zegar gry 1 (nie włączać przed fazą alfa)
    # clock= pygame.time.Clock()

    #wymiary okna
    szerokosc_okna= 1000
    wysokosc_okna= 720

    #tworzenie okna
    screen = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))

    #nazwyanie okna \
    pygame.display.set_caption('COMBAT')

    #generowanie czolgu
    x_pos = 100
    y_pos= 350
    czolg= pygame.Rect(x_pos, y_pos, 50,50)
    #ile pkiseli na klatkę (nieużywane)


    pixel= 12
    #przeszkoda
    przeszkoda= pygame.Rect(500,350,300,300)

    #główna pętla programu, chodzii w nieskończonosc
    running = True

    while running:
        for event in pygame.event.get():
            #stopuje jesli użytkownik zamknął okno
            if event.type == pygame.QUIT:
                running = False

        #zegar gry 2
        # clock.tick(30) (nie włączać przed fazą alfa)

        #RENDER CZOŁGU I PRZESZKODY
        screen.fill((30,30,30))
        pygame.draw.rect(screen,(255,255,255),czolg)
        pygame.draw.rect(screen,(255,0,0),przeszkoda)

        # RUCH
        #predkosc ruchu
        speed_x = 1
        speed_y = 1

        #prędkośc ujemna odejmowana w trakcie  kolizji
        antyspeed_x= 1
        antyspeed_y= 1

        if pygame.key.get_pressed()[pygame.K_UP]:
            speed_y*= -1
            czolg.y += speed_y

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            speed_y*= 1
            czolg.y += speed_y

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            speed_x*= 1
            czolg.x += speed_x

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            speed_x*= -1
            czolg.x += speed_x

        #detekcja kolizj
        #kolizja potrzebuje zabezpiecznia
        tolerancja= 10
        if czolg.colliderect(przeszkoda):
              #dla osi x
              if speed_x > 0:
                  if (przeszkoda.left - czolg.right) < tolerancja:
                      czolg.x -= speed_x
              elif speed_x < 0:
                  if (przeszkoda.right -czolg.left) < tolerancja:
                      czolg.x += speed_x *-1

              #dla osi y
              if speed_y < 0:
                  if (przeszkoda.bottom- czolg.top) < tolerancja:
                      czolg.y += speed_y *-1
              elif speed_y > 0:
                  if (przeszkoda.top- czolg.bottom) < tolerancja:
                      czolg.y -= speed_y

        #GRANICE
        if czolg.right == szerokosc_okna:
            czolg.x -= speed_x
        if czolg.left == 0:
            czolg.x += speed_x *-1
        if czolg.top == 0:
             czolg.y += speed_y *-1
        if czolg.bottom == wysokosc_okna:
            czolg.y -= speed_y



        #odświeżanie ekranu
        pygame.display.flip()
main()
pygame.quit()
#ładowanie tła
# map=pygame.image.load('tlo_2.jpg')
# background_colour = (234, 212, 252)




# screen.blit(map, (50,50))


#ruszajacy się kwadrat



#przeszkoda dla czolgu


#ładowanie spirite
# image= pygame.image.load("tank_icon.jpg")
# screen.blit(image, (900,350))


# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#
#     screen.fill((30,30,30))
#     pygame.draw.rect(screen,(255,255,255),czolg)
#     pygame.draw.rect(screen,(255,0,0),przeszkoda)
#
#     # ruch w klasie
#     poziomy= Ruch()
#     piony= Ruch()
#
#     if pygame.key.get_pressed()[pygame.K_s]:
#         poziomy.granice_boki(x_pos)
#         piony.granice_gora_dol(y_pos)



    #ruch czolgu
    # czolg.x += x_speed
    # czolg.y += y_speed



    #RUCH

    # if pygame.key.get_pressed()[pygame.K_UP]:
    #     czolg.y += -1
    #
    # if pygame.key.get_pressed()[pygame.K_DOWN]:
    #     czolg.y += 1
    #
    # if pygame.key.get_pressed()[pygame.K_RIGHT]:
    #     czolg.x += 1
    #
    # if pygame.key.get_pressed()[pygame.K_LEFT]:
    #     czolg.x -=1

    # #granice ruchu
    # if czolg.right >= szerokosc_okna:
    #     czolg.x
    #
    # elif czolg.left <= 0:
    #     x_speed = 0
    #
    # if czolg.bottom >= wysokosc_okna:
    #     y_speed = 0
    # elif czolg.top <= 0:
    #     y_speed = 0

    #detekcja kolizji pomiedzy obiektami
    # if czolg.colliderect(przeszkoda):
    #     czolg.y += 0
    #     czolg.x += 0
