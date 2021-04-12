import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill((0,0,0))
pygame.display.set_caption("Ghost Ngayang")
clock = pygame.time.Clock()

score = 0
x_rkt = 900
y_rkt = 500
x_obj = 25
y_obj = 430
lompat = False
jumpCount = 10

music = pygame.mixer.music.load('asset/music.mp3')
pygame.mixer.music.play()

bg = pygame.image.load('asset/bg.jpg')
bg = pygame.transform.scale(bg, (800,600))

objek = pygame.image.load('asset/objek.png')
objek = pygame.transform.scale(objek, (150,150))

roket = pygame.image.load('asset/roket.png')
roket = pygame.transform.scale(roket, (100,60))

api = pygame.image.load('asset/api.png')
api = pygame.transform.scale(api, (180,230))

go = pygame.image.load('asset/go.png')
go = pygame.transform.scale(go, (400,250))

font = pygame.font.SysFont('comicsans',30,True)

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    keys = pygame.key.get_pressed()
    if not(lompat):
        if keys [pygame.K_SPACE]:
            lompat = True
    else:
        if jumpCount >= -10:
            oy = 1
            if jumpCount < 0:
                oy = -1
            y_obj -= (jumpCount ** 2) * oy
            jumpCount -= 1
        else:
            lompat = False
            jumpCount = 10

    gameDisplay.blit(bg, (0,0))    
    gameDisplay.blit(roket, (x_rkt,y_rkt))
    gameDisplay.blit(objek, (x_obj,y_obj))
    
    text = font.render('Score: %d'%(score),1,(0,0,0))
    gameDisplay.blit(text, (680,15))
               
    x_rkt -= 15
    if x_rkt < -90:
        x_rkt = 900
        y_rkt = 500
        score += 1
        

    if x_rkt < 140 and y_obj >= 430:
        lompat = False
        x_rkt = 50
        y_rkt = 500
        gameDisplay.blit(go, (200,170))
        gameDisplay.blit(api, (5,360))
              
    pygame.display.update()
    clock.tick(30)
     
pygame.quit() 
