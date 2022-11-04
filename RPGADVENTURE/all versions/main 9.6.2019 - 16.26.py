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



pygame.display.set_caption("TADS Adventure")


#Coisas com sprite

MulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]

#Dado donis função
def girar():
    global display, dados, dado
    from random import randrange
    print(randrange(0, 6))
    display.blit(dados[randrange(0, 6)], (661, 462))
    dado=randrange
    
dado=0   

#coordenadas das coisas com sprite

SlimeX, SlimeY = 680,401
MulequeOverX, MulequeOverY = 36, 215

#Cordenadas do boy

boyX,boyY=36,215



#jogo em ato
while True:
    
    fps.tick(5)#25
    #o programa e baseado em eventos!
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        
        
	    # ele imprime os eventos para a visualização
            print(event)
            
            
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
                
            display.blit(mapa, (0, 0))
            #donis dado

  
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
                       
                    
                        
            #Tentando Eventos:
            

                        
    

        #obejetos in overword
    display.blit(slime, (SlimeX, SlimeY))
    display.blit(MulequeOver, (MulequeOverX, MulequeOverY))

    

    print(pygame.mouse.get_pos())
    pygame.display.flip()
