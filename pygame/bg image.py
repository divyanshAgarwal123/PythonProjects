
import pygame 
pygame.init() 
white=(255,255,255)
display_surface = pygame.display.set_mode((1280,720 )) 

pygame.display.set_caption('Image') 

bgimage = pygame.image.load('7.jpg') 

while True :
        display_surface.fill(white) 
        display_surface.blit(bgimage, (0, 0))  
        for event in pygame.event.get() :
                if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                pygame.display.update() 