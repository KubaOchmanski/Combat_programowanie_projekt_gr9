import pygame
import math
import random
import time
import os


def main():

    #start z bazowymi parametrami
    pygame.init()

    #zegar gry 1 (nie włączać przed fazą alfa)
    # clock= pygame.time.Clock()

    #wymiary okna
    szerokosc_okna= 800
    wysokosc_okna= 600

    #tworzenie okna
    screen = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))

    #nazwyanie okna \
    pygame.display.set_caption('COMBAT')
    licznik_strzelanie=0
    strzelanie = False

    #ikony czołgów
    czolg1obraz = pygame.image.load('czerwony.png')
    czolg1 = pygame.transform.rotate(pygame.transform.scale(
        czolg1obraz, (50,50)), 270)

    czolg22obraz = pygame.image.load('niebieski.png')
    czolg22 = pygame.transform.rotate(pygame.transform.scale(
        czolg22obraz, (50,50)), 90)

    #generowanie czolgu
    x_pos = 19
    y_pos= 360
    czolg= pygame.Rect(x_pos, y_pos, 50,50)
    #ile pkiseli na klatkę (nieużywane)

    #generowanie czolgu 2
    x_pos2= 721
    y_pos2= 310
    czolg2= pygame.Rect(x_pos2, y_pos2, 50,50)




    # generowanie przeszkody
    przeszkoda= pygame.Rect(100,120,120,60)
    przeszkoda1= pygame.Rect(580,120,120,60)
    przeszkoda2= pygame.Rect(340,220,120,20)
    przeszkoda3= pygame.Rect(340,480,120,20)
    przeszkoda4= pygame.Rect(340,240,20,20)
    przeszkoda5= pygame.Rect(440,240,20,20)
    przeszkoda6= pygame.Rect(340,460,20,20)
    przeszkoda7= pygame.Rect(440,460,20,20)
    przeszkoda8= pygame.Rect(100,260,20,200)
    przeszkoda9= pygame.Rect(680,260,20,200)
    przeszkoda10= pygame.Rect(80,260,20,20)
    przeszkoda11= pygame.Rect(80,440,20,20)
    przeszkoda12= pygame.Rect(700,260,20,20)
    przeszkoda13= pygame.Rect(700,440,20,20)
    przeszkoda14= pygame.Rect(200,320,40,80)
    przeszkoda15= pygame.Rect(560,320,40,80)
    przeszkoda16= pygame.Rect(100,540,120,60)
    przeszkoda17= pygame.Rect(580,540,120,60)

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
        pygame.draw.rect(screen,(255,0,0),przeszkoda)
        pygame.draw.rect(screen,(255,0,0),przeszkoda1)
        pygame.draw.rect(screen,(255,0,0),przeszkoda2)
        pygame.draw.rect(screen,(255,0,0),przeszkoda3)
        pygame.draw.rect(screen,(255,0,0),przeszkoda4)
        pygame.draw.rect(screen,(255,0,0),przeszkoda5)
        pygame.draw.rect(screen,(255,0,0),przeszkoda6)
        pygame.draw.rect(screen,(255,0,0),przeszkoda7)
        pygame.draw.rect(screen,(255,0,0),przeszkoda8)
        pygame.draw.rect(screen,(255,0,0),przeszkoda9)
        pygame.draw.rect(screen,(255,0,0),przeszkoda10)
        pygame.draw.rect(screen,(255,0,0),przeszkoda11)
        pygame.draw.rect(screen,(255,0,0),przeszkoda12)
        pygame.draw.rect(screen,(255,0,0),przeszkoda13)
        pygame.draw.rect(screen,(255,0,0),przeszkoda14)
        pygame.draw.rect(screen,(255,0,0),przeszkoda15)
        pygame.draw.rect(screen,(255,0,0),przeszkoda16)
        pygame.draw.rect(screen,(255,0,0),przeszkoda17)


        #rysowanie czołgów na ekranie
        screen.blit(czolg1, (czolg.x, czolg.y))
        screen.blit(czolg22, (czolg2.x, czolg2.y))

        # !!!RUCH!!! (klasa czołg, def ruch)
        #predkosc ruchu
        speed_x = 1
        speed_y = 1

        #prędkośc ujemna odejmowana w trakcie  kolizji
        antyspeed_x= 1
        antyspeed_y= 1

        #ruchy pierwszego czołgu
        orientacjaczolgu = 3
        if pygame.key.get_pressed()[pygame.K_UP]:
            orientacjaczolgu = 12
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 0)
            speed_y*= -1
            czolg.y += speed_y

        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            orientacjaczolgu = 6
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 180)
            speed_y*= 1
            czolg.y += speed_y

        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            orientacjaczolgu = 3
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 270)
            speed_x*= 1
            czolg.x += speed_x

        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            orientacjaczolgu = 9
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 90)
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

        if czolg.colliderect(przeszkoda1):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda1.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda1.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda1.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda1.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda2):
              #dla osi x
              if speed_x > 0:
                  if (przeszkoda2.left - czolg.right) < tolerancja:
                      czolg.x -= speed_x
              elif speed_x < 0:
                  if (przeszkoda2.right - czolg.left) < tolerancja:
                      czolg.x += speed_x *-1
              #dla osi y
              if speed_y < 0:
                  if (przeszkoda2.bottom- czolg.top) < tolerancja:
                      czolg.y += speed_y *-1
              elif speed_y > 0:
                  if (przeszkoda2.top- czolg.bottom) < tolerancja:
                      czolg.y -= speed_y

        if czolg.colliderect(przeszkoda3):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda3.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda3.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda3.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda3.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda4):
              #dla osi x
              if speed_x > 0:
                  if (przeszkoda4.left - czolg.right) < tolerancja:
                      czolg.x -= speed_x
              elif speed_x < 0:
                  if (przeszkoda4.right - czolg.left) < tolerancja:
                      czolg.x += speed_x *-1
              #dla osi y
              if speed_y < 0:
                  if (przeszkoda4.bottom- czolg.top) < tolerancja:
                      czolg.y += speed_y *-1
              elif speed_y > 0:
                  if (przeszkoda4.top- czolg.bottom) < tolerancja:
                      czolg.y -= speed_y

        if czolg.colliderect(przeszkoda5):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda5.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda5.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda5.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda5.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda6):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda6.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda6.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda6.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda6.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda7):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda7.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda7.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda7.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda7.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda8):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda8.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda8.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda8.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda8.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda9):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda9.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda9.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda9.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda9.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda10):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda10.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda10.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda10.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda10.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda11):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda11.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda11.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda11.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda11.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda12):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda12.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda12.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda12.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda12.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda13):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda13.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda13.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda13.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda13.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda14):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda14.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda14.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda14.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda14.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda15):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda15.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda15.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda15.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda15.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda16):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda16.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda16.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda16.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda16.top- czolg.bottom) < tolerancja:
                    czolg.y -= speed_y

        if czolg.colliderect(przeszkoda17):
              #dla osi x
            if speed_x > 0:
                if (przeszkoda17.left - czolg.right) < tolerancja:
                    czolg.x -= speed_x
            elif speed_x < 0:
                if (przeszkoda17.right - czolg.left) < tolerancja:
                        czolg.x += speed_x *-1

              #dla osi y
            if speed_y < 0:
                if (przeszkoda17.bottom- czolg.top) < tolerancja:
                    czolg.y += speed_y *-1
            elif speed_y > 0:
                if (przeszkoda17.top- czolg.bottom) < tolerancja:
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
            if strzal.colliderect(przeszkoda1):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda2):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda3):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda4):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda5):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda6):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda7):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda8):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda9):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda10):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda11):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda12):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda13):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda14):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda15):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda16):
                strzelanie= False
                licznik_strzelanie = 0
            if strzal.colliderect(przeszkoda17):
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
