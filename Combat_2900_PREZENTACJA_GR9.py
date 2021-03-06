import pygame
import math
import random
import time
import os

textX = 50
textY = 10



def main():

    #start z bazowymi parametrami
    pygame.init()
    pygame.mixer.init()

    #zegar gry 1 (nie włączać przed fazą alfa)
    clock= pygame.time.Clock()

    #wymiary okna
    szerokosc_okna= 800
    wysokosc_okna= 600

    #tworzenie okna
    screen = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))


    ziemia = pygame.image.load('ziemia1.png')
    trawa = pygame.image.load('trawa.jpeg')
    trawa1 = pygame.transform.scale(trawa, (120,60))
    trawa2 = pygame.transform.scale(trawa, (120,20))
    trawa3 = pygame.transform.scale(trawa, (20,20))
    trawa4 = pygame.transform.scale(trawa, (20,200))
    trawa5 = pygame.transform.scale(trawa, (40,80))
    # screen.blit(ziemia,(0,0))

    #dźwięk
    wybuch = pygame.mixer.Sound(os.path.join('wybuch.mp3'))
    wybuch.set_volume(0.3)
    muzyka = pygame.mixer.music.load(os.path.join('projektcichszy.mp3'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)

    #nazwyanie okna
    pygame.display.set_caption('COMBAT')


    licznik_strzelanie=0
    strzelanie = False

    #PUNKTACJA - wyswietlanie
    punkty1 = 0
    font = pygame.font.Font('28dayslater.ttf', 32)
    textX = 50
    textY = 10

    punkt = font.render("Trafiony!", True, (120, 190, 99))

    font_k = pygame.font.Font('28dayslater.ttf', 80)

    #generowanie czolgu
    x_pos = 19
    y_pos= 360
    czolg= pygame.Rect(x_pos, y_pos, 50,50)


    czolg1obraz = pygame.image.load('czerwony.png')
    czolg1 = pygame.transform.rotate(pygame.transform.scale(
        czolg1obraz, (50,50)), 270)

    #generowanie czolgu 2
    x_pos2= 721
    y_pos2= 310
    czolg2= pygame.Rect(x_pos2, y_pos2, 50,50)

    czolg22obraz = pygame.image.load('zolty.png')
    czolg22 = pygame.transform.rotate(pygame.transform.scale(
        czolg22obraz, (50,50)), 90)

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



    #!!!główna pętla programu, chodzii w nieskończonosc!!!
    running = True

    while running:
        for event in pygame.event.get():
            #stopuje jesli użytkownik zamknął okno
            if event.type == pygame.QUIT:
                running = False


        # zegar gry 2
        clock.tick(30)



        #RENDER CZOŁGU I PRZESZKODY
        screen.fill((98,52,18))

        screen.blit(trawa1,(przeszkoda.x, przeszkoda.y))
        screen.blit(trawa1,(przeszkoda1.x, przeszkoda1.y))
        screen.blit(trawa1,(przeszkoda16.x, przeszkoda16.y))
        screen.blit(trawa1,(przeszkoda17.x, przeszkoda17.y))

        screen.blit(trawa2,(przeszkoda2.x, przeszkoda2.y))
        screen.blit(trawa2,(przeszkoda3.x, przeszkoda3.y))

        screen.blit(trawa3,(przeszkoda4.x, przeszkoda4.y))
        screen.blit(trawa3,(przeszkoda5.x, przeszkoda5.y))
        screen.blit(trawa3,(przeszkoda6.x, przeszkoda6.y))
        screen.blit(trawa3,(przeszkoda7.x, przeszkoda7.y))
        screen.blit(trawa3,(przeszkoda10.x, przeszkoda10.y))
        screen.blit(trawa3,(przeszkoda11.x, przeszkoda11.y))
        screen.blit(trawa3,(przeszkoda12.x, przeszkoda12.y))
        screen.blit(trawa3,(przeszkoda13.x, przeszkoda13.y))

        screen.blit(trawa4,(przeszkoda8.x, przeszkoda8.y))
        screen.blit(trawa4,(przeszkoda9.x, przeszkoda9.y))

        screen.blit(trawa5,(przeszkoda14.x, przeszkoda14.y))
        screen.blit(trawa5,(przeszkoda15.x, przeszkoda15.y))

        #rysowanie czołgów na ekranie
        screen.blit(czolg1, (czolg.x, czolg.y))
        screen.blit(czolg22, (czolg2.x, czolg2.y))


        #rysowanie czołgów na ekranie
        screen.blit(czolg1, (czolg.x, czolg.y))
        screen.blit(czolg22, (czolg2.x, czolg2.y))

        # !!!RUCH!!! (klasa czołg, def ruch)
        #predkosc ruchu
        speed_x = 1
        speed_y = 1


        #ruchy pierwszego czołgu
        if pygame.key.get_pressed()[pygame.K_UP]:
            orientacjaczolgu = 12
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 0)
            speed_y*= -1
            czolg.y += speed_y

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            orientacjaczolgu = 6
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 180)
            speed_y*= 1
            czolg.y += speed_y

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            orientacjaczolgu = 3
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 270)
            speed_x*= 1
            czolg.x += speed_x

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            orientacjaczolgu = 9
            czolg1 = pygame.transform.rotate(
                pygame.transform.scale(czolg1obraz, (50,50)), 90)
            speed_x*= -1
            czolg.x += speed_x





        if pygame.key.get_pressed()[pygame.K_w]:
            orientacjaczolgu = 12
            czolg22 = pygame.transform.rotate(
                pygame.transform.scale(czolg22obraz, (50,50)), 0)
            speed_y*= -1
            czolg2.y += speed_y

        if pygame.key.get_pressed()[pygame.K_s]:
            orientacjaczolgu = 6
            czolg22 = pygame.transform.rotate(
                pygame.transform.scale(czolg22obraz, (50,50)), 180)
            speed_y*= 1
            czolg2.y += speed_y

        if pygame.key.get_pressed()[pygame.K_d]:
            orientacjaczolgu = 3
            czolg22 = pygame.transform.rotate(
                pygame.transform.scale(czolg22obraz, (50,50)), 270)
            speed_x*= 1
            czolg2.x += speed_x

        if pygame.key.get_pressed()[pygame.K_a]:
            orientacjaczolgu = 9
            czolg22 = pygame.transform.rotate(
                pygame.transform.scale(czolg22obraz, (50,50)), 90)
            speed_x*= -1
            czolg2.x += speed_x




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

        #!!!GRANICE!!!!
        if czolg.right == szerokosc_okna:
            czolg.x -= speed_x
        if czolg.left == 0:
            czolg.x += speed_x *-1
        if czolg.top == 0:
            czolg.y += speed_y *-1
        if czolg.bottom == wysokosc_okna:
            czolg.y -= speed_y





        #!!!STRZELANIE!!!
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            strzelanie= True
            if orientacjaczolgu == 3:
                strzal= pygame.Rect(czolg.x+50, czolg.y+21, 9, 9)
            if orientacjaczolgu == 6:
                strzal= pygame.Rect(czolg.x+20, czolg.y+50, 9, 9)
            if orientacjaczolgu == 9:
                strzal= pygame.Rect(czolg.x, czolg.y+20, 9, 9)
            if orientacjaczolgu == 12:
                strzal= pygame.Rect(czolg.x+21, czolg.y, 9, 9)

        if strzelanie:

            if orientacjaczolgu == 3:
                pygame.draw.rect(screen,(255,255,240),strzal)
                strzal.x += 30
                licznik_strzelanie += 1
            if orientacjaczolgu == 6:
                pygame.draw.rect(screen,(255,255,240),strzal)
                strzal.y += 30
                licznik_strzelanie += 1
            if orientacjaczolgu == 9:
                pygame.draw.rect(screen,(255,255,240),strzal)
                strzal.x -= 30
                licznik_strzelanie += 1
            if orientacjaczolgu == 12:
                pygame.draw.rect(screen,(255,255,240),strzal)
                strzal.y -= 30
                licznik_strzelanie += 1

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
                strzelanie = False
                licznik_strzelanie = 0
                pygame.mixer.Sound.play(wybuch)
                screen.blit(punkt,( 60, 60))
                punkty1 += 1


        if licznik_strzelanie >= szerokosc_okna:
            strzelanie = False
            licznik_strzelanie = 0

        #koniecGry
        font_k = pygame.font.Font('28dayslater.ttf', 80)

        if punkty1==3:
            koniec = font_k.render("KONIEC. /n Wygrałeś!", True, (120, 190, 99))
            screen.blit(koniec, (60, 60))
            break


        #odświeżanie ekranu
        pygame.display.flip()

def tablica_punktow(x,y):
    score = font.render("Punkty: " + str(punkty1), True, (0,0,0))
    screen.blit(score, (x, y))

main()
tablica_punktow(textX, textY)
pygame.quit()
