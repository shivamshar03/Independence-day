import pygame.display
from maam import massage
import pygame
import time

pygame.init()
scr = pygame.display.set_mode((600, 500))
look_1 = pygame.image.load('coderbyzlogo.jpg')
look_1 = pygame.transform.scale(look_1, (600, 500))
scr.blit(look_1, (0, 0))
pygame.display.update()
done = True

while done:
    x = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                from sketchpy import library

                object = library.flag()
                object.draw()

                time.sleep(1.5)

                scr2 = pygame.display.set_mode((800, 650))
                look_1 = pygame.image.load('WISH.png')
                look_1 = pygame.transform.scale(look_1, (800, 650))
                scr2.blit(look_1, (0, 0))
                pygame.display.update()
                massage(40, (250, 100, 0), scr2, '', "by coder_byz.exe ", 300, 585)
                pygame.display.update()

            if event.key == pygame.K_1:
                scr1 = pygame.display.set_mode((800, 650))
                look_1 = pygame.image.load('tiranga2.jpg')
                look_1 = pygame.transform.scale(look_1, (800, 650))
                scr1.blit(look_1, (0, 0))
                pygame.display.update()
                massage(40, (50, 100, 255), scr1, '', " PRESENTED BY :- coder_byz.exe", 250, 600)
                massage(65, (255, 125, 35), scr1, "Cooper Black", "ON THE OCCASSION ", 50, 200)
                massage(65, (255, 255, 255), scr1, 'Cooper Black', "OF 75TH ", 250, 275)
                massage(65, (0, 255, 50), scr1, 'Cooper Black', "INDEPENDENCE DAY", 50, 350)
                pygame.display.update()

            if event.key == pygame.K_3:
                massage(80, (255, 0, 0), pygame.display.set_mode((800, 700)), '', "THANK YOU ", 200, 250)
                pygame.display.update()

pygame.quit()
