import pygame
import random
import math
pygame.init()
win = pygame.display.set_mode((800,600 )) 
Bg=pygame.image.load("2352.jpg")
Bgx=800
Bgy=600
#Player
player=pygame.image.load("rocket.png")
playerx=370
playery=510
playerx_change=0
#Alien
alien=pygame.image.load("aien1.png")
alienx =random.randint(0,735)
alieny =random.randint(190,250) 
alienx_change=2
alieny_change=20
#Ship
ship=pygame.image.load("ufo.png")
shipx = 310
shipy = 0
#Laser
laser=pygame.image.load("laser.png")
laserx =0
lasery = 510
laserx_change=0
lasery_change=3
laser_state = "ready"

score=0
#Collision
def isCollision(alienx,alieny,laserx,lasery):
    distance= math.sqrt((math.pow(alienx-laserx,2))+(math.pow(alieny-lasery,2)))
    if distance<27:
        return True
    else:
        return False
#Images
def UFO():
    win.blit(ship,(shipx,shipy))
def Player(x,y):
    win.blit(player,(x,y))   
def Alien():
    win.blit(alien,(alienx,alieny))
def Laser(x,y):
    global laser_state
    laser_state = "fire"
    win.blit(laser,(x + 10, y + 16))

#Game loop
run=True
while run:
    for event in pygame.event.get():
#Quit Loop
        if event.type==pygame.QUIT:
                pygame.quit()
                run=False
#Player Movements
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                playerx_change=-2;
                
            if(event.key==pygame.K_RIGHT):
                playerx_change=2;
#Laser
            if event.key==pygame.K_SPACE:
                if laser_state == "ready":
                    laserbeam=pygame.mixer.music.load("Lasersound.mp3")
                    pygame.mixer.music.play()
                    laserx=playerx
                    Laser(laserx,lasery)
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT): 
                playerx_change=0
                
    win.fill((0,0,0))  
    win.blit(Bg,(0,0))
#Player settings     
    playerx+=playerx_change
    if(playerx>=736):
        playerx=736;
    if(playerx<=0):
        playerx=0;
#Alien Settings
    alienx+=alienx_change
    if (alienx>=736):
        alienx_change=-2
        alieny+=alieny_change
    elif(alienx<=0):
        alienx_change=2
        alieny+=alieny_change
#Laser Movements
    if lasery <= 0:
        lasery = 510
        laser_state = "ready"
    if laser_state == "fire":
        Laser(laserx,lasery)
        lasery-=lasery_change
#Collision loop
    collision=isCollision(alienx,alieny,laserx,lasery)
    if collision:
        lasery=510
        laser_state="ready"
        score+=1
        print(score)
        alienx =random.randint(0,735)
        alieny =random.randint(190,250) 
#Functions    
    Player(playerx,playery)
    UFO()
    Alien()
    pygame.display.update()      