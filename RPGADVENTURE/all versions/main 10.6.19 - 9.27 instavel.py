import pygame
import random
import sys
import time

'''
ACHAR POSIÇÃO DO SPRITE
display.blit(variaveldospriteaqui, (pygame.mouse.get_pos()))
print(pygame.mouse.get_pos())
'''
#Inicio de tudo
pygame.init()
tamanho = Largura, altura = 800, 600
display = pygame.display.set_mode (tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("TADS Adventure")# (virgula) icone do titulo


#Coisas com sprite

MulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]
#-------------------------------O B J E T O S-----------------------------------------------------
#coordenadas das coisas com sprite

SlimeX, SlimeY = 680,401
MulequeOverX, MulequeOverY = 36, 215
MulequeOverXY=(MulequeOverX, MulequeOverY)

#Cordenadas do boy
boyX,boyY=36,215






#--------------------------------F U N Ç Õ E -----------------------------------------------------

#Dado função:
dado=0

def girar():
    global display, dados, dado
    from random import randrange
    print(randrange(0, 6))
    display.blit(dados[randrange(0, 6)], (661, 462))
    dado=randrange
    

#mover-se função
def mover():
    MulequeOverX += 46







    

#jogo em ato
while True:

    
    fps.tick(5)#25
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        
	    # ele imprime os eventos para a visualização
            print(event)
            
            
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                pygame.quit()
                quit()
                sys.exit()
                   
            display.blit(mapa, (0, 0))
  
            #movimentando o Boy:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    MulequeOverX += 46
                if event.key == pygame.K_LEFT:
                    MulequeOverX -= 46
                if event.key == pygame.K_UP:
                    MulequeOverY -= 46
                if event.key == pygame.K_DOWN:
                    MulequeOverY += 46
                if event.key == pygame.K_SPACE:
                    girar()
                    print(dado)
                    mover(dado)
                       
            print(MulequeOverXY)
                        
            #Tentando Eventos:
            

                        
    

        #obejetos in overword
    display.blit(slime, (SlimeX, SlimeY))
    display.blit(MulequeOver, (MulequeOverX, MulequeOverY))

    

    print(pygame.mouse.get_pos())
    pygame.display.flip()
