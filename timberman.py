import pygame
import os
import sys
import random
import math
import time
 
from pygame.constants import K_LEFT, K_RIGHT, SCRAP_CLIPBOARD, WINDOWHITTEST
from pygame.event import post
 
pygame.init()
pygame.display.set_caption("Timberman")
WIDTH, HEIGHT = 1920, 1080
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
 
def zdjecie(nazwa):
      return pygame.image.load(os.path.join("assets", nazwa))
 
def szerokosc(x):
      return round(WIDTH * x / 1920)
 
def wysokosc(x):
      return round(HEIGHT * x / 1080)
 
BACKGROUND = pygame.transform.scale(zdjecie("background.jpg"), (WIDTH, HEIGHT))
DRZEWO = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Dzewo.png")), (szerokosc(200), wysokosc(200)))
DRZEWO_LEWO = pygame.transform.scale(zdjecie("Dzewo2.png"),(szerokosc(200) , wysokosc(200)))
DRZEWO_PRAWO = pygame.transform.scale(zdjecie("Dzewo1.png"), (szerokosc(200) , wysokosc(200)))
PIEN = pygame.transform.scale(zdjecie("pien.png"),(szerokosc(200), wysokosc(30)))
PINGWIN_LEWO = pygame.transform.scale(zdjecie("pingwinLewoSiekiera.png"),(szerokosc(250),wysokosc(250)))
PINGWIN_PRAWO = pygame.transform.scale(zdjecie("pingwinPrawoSiekiera.png"),(szerokosc(250),wysokosc(250)))
PINGWIN_LEWO_IDLE = pygame.transform.scale(zdjecie("pingwinLewoIdle.png"),(szerokosc(250),wysokosc(250)))
PINGWIN_PRAWO_IDLE = pygame.transform.scale(zdjecie("pingwinPrawoIdle.png"),(szerokosc(250),wysokosc(250)))
PINGWIN_DEAD = pygame.transform.scale(zdjecie("pingwinDead.png"),(szerokosc(250),wysokosc(250)))
score_font = pygame.font.Font(os.path.join("assets", "Minecraft.ttf"), 60)
timber_font = pygame.font.Font(os.path.join("assets", "font.otf"), 200)
space_font = pygame.font.Font(os.path.join("assets", "font.otf"), 50)
scoreMenu_font = pygame.font.Font(os.path.join("assets", "font.otf"), 40)
drzewa = []
czas_animacji = 3
 
def menu(score):
      run = True
      FPS = 60
      clock = pygame.time.Clock()      
      if score != -1:   
            score_label = scoreMenu_font.render(f"Score: {score}", 1, (0,0,0))
      while run:
            clock.tick(FPS)
            window.blit(BACKGROUND, (0, 0))
            if score != -1:
                  window.blit(score_label, (WIDTH / 2 - score_label.get_width() / 2, HEIGHT / 2 + wysokosc(150)))
            timberText = timber_font.render(f"Timber", 1, (0,0,0))
            window.blit(timberText, (WIDTH / 2 - timberText.get_width() / 2, HEIGHT/2 - timberText.get_height()/2 + math.sin(time.time()*5)*5 - 25))
            spaceText = space_font.render(f"SPACE TO START", 1, (0,0,0))
            window.blit(spaceText, (WIDTH / 2 - spaceText.get_width() / 2, HEIGHT/2 + wysokosc(80)))
            pygame.display.update()
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        quit()
                  if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_SPACE:
                                    run = False
      main()

def dodaj_drzewo():
      if (drzewa[-1]) == 1:
            drzewa.append(random.choice([0,0,1]))
      elif (drzewa[-1] == 2):
            drzewa.append(random.choice([0,0,2]))
      else:
            drzewa.append(random.randint(1,2))

def main():
      run = True
      FPS = 60
      clock = pygame.time.Clock()
      postac = 0
      animacja = 0
      game_over = False
      czas_na_ruch = 0
      start = False
      score = 0
      drzewa.clear()
      sciete = []
      drzewa.append(0)
      for i in range(9):
            dodaj_drzewo()
 
      def redraw_window(window):
            window.blit(BACKGROUND, (0, 0))
            for i in range(10):
                  if drzewa[i] == 0:
                        window.blit(DRZEWO, (WIDTH / 2 - szerokosc(100), HEIGHT - (wysokosc(163) * (i + 1)) - wysokosc(30)))
                  if drzewa[i] == 1:
                        window.blit(DRZEWO_LEWO, (WIDTH / 2 - szerokosc(100), HEIGHT - (wysokosc(163) * (i + 1)) - wysokosc(30)))
                  if drzewa[i] == 2:
                        window.blit(DRZEWO_PRAWO, (WIDTH / 2 - szerokosc(100), HEIGHT - (wysokosc(163) * (i + 1)) - wysokosc(30)))
 
            window.blit(PIEN, (WIDTH / 2 - szerokosc(100), HEIGHT - wysokosc(30)))
            if postac == 0:
                  window.blit(PINGWIN_LEWO_IDLE, (WIDTH / 2 - szerokosc(250), HEIGHT - wysokosc(290)))
            if postac == 1:
                  window.blit(PINGWIN_PRAWO_IDLE, (WIDTH / 2, HEIGHT - wysokosc(290)))
            if postac == 2:
                  window.blit(PINGWIN_PRAWO, (WIDTH / 2 - szerokosc(250), HEIGHT - wysokosc(290)))
            if postac == 3:
                  window.blit(PINGWIN_LEWO, (WIDTH / 2, HEIGHT - wysokosc(290)))
            if postac == 4:
                  window.blit(PINGWIN_DEAD, (WIDTH / 2 - szerokosc(250), HEIGHT - wysokosc(290)))      
            if postac == 5:
                  window.blit(PINGWIN_DEAD, (WIDTH / 2, HEIGHT - wysokosc(290)))      
            score_label = score_font.render(f"Score: {score}", 1, (0,0,0))
            window.blit(score_label, (szerokosc(60), wysokosc(60)))
            pygame.display.update()
 
      while run:
            clock.tick(FPS)
            redraw_window(window)
 
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        quit()
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                              postac = 2
                              sciete.append([100, 1])
                              start = True
                              czas_na_ruch = 100
                              animacja = czas_animacji
                              score += 1
                              if drzewa[1] == 1 or drzewa[0] == 1:
                                    if (drzewa[1] == 1 and drzewa[0] != 1):
                                          drzewa.pop(0)
                                          dodaj_drzewo()
                                    run = False
                              else:
                                    drzewa.pop(0)
                                    dodaj_drzewo()
                        if event.key == pygame.K_RIGHT:
                              postac = 3
                              sciete.append([100, 1])
                              start = True
                              czas_na_ruch = 100
                              animacja = czas_animacji
                              score += 1
                              if drzewa[1] == 2 or drzewa[0] == 2:
                                    if (drzewa[1] == 2 and drzewa[0] != 2):
                                          drzewa.pop(0)
                                          dodaj_drzewo()
                                    run = False
                              else:
                                    drzewa.pop(0)
                                    dodaj_drzewo()
            if start:
                  if czas_na_ruch == 1:
                        break
                  czas_na_ruch -= 1
            if animacja > 1:
                  animacja -= 1
            elif animacja == 1:
                  if postac == 2:
                        postac = 0
                  elif postac == 3:
                        postac = 1
                  animacja -= 1
      if postac == 2:
            postac = 4
      if postac == 3:
            postac = 5
      redraw_window(window)
      pygame.time.delay(1000)
      menu(score)
 
menu(-1)
 