# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:06:12 2020

@author: divya
"""

import pygame
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game of Squares")
bluex = 100
bluey = 100
redX = 300
redY = 300
bluevel = 6
redVel = 4
run = True

def drawGame():
     win.fill((0, 0, 0))
     pygame.draw.rect(win, (0, 0, 255), (bluex, bluey, 20, 20))
     pygame.draw.rect(win, (255, 0, 0), (redX, redY, 40, 40))
     pygame.display.update()

while run:
      pygame.time.delay(50)

      if redX < bluex - 10:
          redX = redX + redVel 
          drawGame() 
      elif redX > bluex + 10:
          drawGame()
          redX = redX - redVel
      elif redY < bluey - 10: 
          redY = redY + redVel 
      elif redY > bluey + 10:
          redY = redY - redVel
      else:
          run = False
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()
      
      if keys[pygame.K_SPACE]:
          bluevel=10
      else:
         bluevel=6
      if keys[pygame.K_LEFT]:
            bluex -= bluevel

      if keys[pygame.K_RIGHT]:
            bluex += bluevel
      
      if keys[pygame.K_UP]:
            bluey -= bluevel
      
      if keys[pygame.K_DOWN]:
            bluey += bluevel
      
      drawGame()
          
pygame.quit()  

