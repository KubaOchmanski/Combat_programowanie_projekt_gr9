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
    licznik_strzelanie=0
    strzelanie = False
    #generowanie czolgu
    x_pos = 100
    y_pos= 350
    czolg= pygame.Rect(x_pos, y_pos, 50,50)
    #ile pkiseli na klatkę (nieużywane)

    #generowanie czolgu 2
    x_pos2= 900
    y_pos2= 350
    czolg2= pygame.Rect(x_pos2, y_pos2, 50,50)


    # generowanie przeszkody
    przeszkoda= pygame.Rect(500,350,300,300)


    # strzal z stalej pozycji rusza się, ale nie podąża za czołgiem
    # strzal= pygame.Rect(czolg.x, czolg.y, 10,10)

    #!!!główna pętla programu, chodzii w nieskończonosc!!!
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
        pygame.draw.rect(screen,(255,0,255),czolg2)
        pygame.draw.rect(screen,(255,0,0),przeszkoda)

        # !!!RUCH!!! (klasa czołg, def ruch)
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



        #!!!DETEKCJA KOLIZJI!!! (klasa Poziom, def kolizja) (czołg się ślizga)
        #kolizja potrzebuje zabezpiecznia
        tolerancja= 10
        if czolg.colliderect(przeszkoda):
              #dla osi x
              if speed_x > 0:
                  if (przeszkoda.left - czolg.right) < tolerancja:
                      czolg.x -= speed_x
              elif speed_x < 0:
                  if (przeszkoda.right - czolg.left) < tolerancja:
                      czolg.x += speed_x *-1

              #dla osi y
              if speed_y < 0:
                  if (przeszkoda.bottom- czolg.top) < tolerancja:
                      czolg.y += speed_y *-1
              elif speed_y > 0:
                  if (przeszkoda.top- czolg.bottom) < tolerancja:
                      czolg.y -= speed_y


    #!!!GRANICE!!!! (czołg się nie ślizga)
        if czolg.right == szerokosc_okna:
            czolg.x -= speed_x
        if czolg.left == 0:
            czolg.x += speed_x *-1
        if czolg.top == 0:
            czolg.y += speed_y *-1
        if czolg.bottom == wysokosc_okna:
            czolg.y -= speed_y

        #!!!STRZELANIE!!! nie chce się odczepic od czołgu
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            strzelanie= True
            strzal= pygame.Rect(czolg.x, czolg.y, 10,10)

        if strzelanie:
            pygame.draw.rect(screen,(0,255,0),strzal)
            strzal.x += 2
            licznik_strzelanie+=1
            if strzal.colliderect(przeszkoda):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(czolg2):
                strzelanie= False
                licznik_strzelanie = 0
                print("trafiony")

        if licznik_strzelanie >= szerokosc_okna:
            strzelanie = False
            licznik_strzelanie = 0




        #odświeżanie ekranu
        pygame.display.flip()
main()
pygame.quit()
