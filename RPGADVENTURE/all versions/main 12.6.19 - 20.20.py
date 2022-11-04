import pygame
import random
import sys
import time

#Inicio de tudo
pygame.init()
tamanho = Largura, altura = 800, 600
display = pygame.display.set_mode (tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("TADS Adventure")# (virgula) icone do titulo

#-------------------------------O B J E T O S - BLIT-SPRITES ----------------------

#Coisas com sprite

#Over
mulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

#batalha
campoBatalha = pygame.image.load("telaDeBatalha.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")
mucegu = pygame.image.load("mucegu.png")
rato = pygame.image.load("Rato.png")
slimeBatalha = pygame.image.load("slime 0.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")

#Dados
dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]

'''
#Itens
Espada = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png")]
         
Escudo = [pygame.image.load(" "),pygame.image.load(" "),
         pygame.image.load(" ")]

Poção = [pygame.image.load(" "),pygame.image.load(" "),
         pygame.image.load(" ")]
'''

#------------------------------- O B J E T O S - C O R D E N A D A S -----------------------------------
#coordenadas das coisas com sprite

slimeX, slimeY = 680,401
mulequeOverX, mulequeOverY = 36, 215
mulequeOverXY=(0,0)

#Cordenadas do boy
boyX,boyY=36,215

#Cordenadas das coisa na batalha
campoBatalhaX, campoBatalhaY = 100, 10
slimeBatalhaX, slimeBatalhaY = 638, 260
mulequeBatalhaX, mulequeBatalhaY =  177, 229


#-------------------------------- F U N Ç Õ E -----------------------------------------------------

#batalha função:
def batalha():
    global display,campoBatalha, campoBatalhaX, campoBatalhaY, slimeBatalhaX, slimeBatalhaY ,mulequeBatalha, mulequeBatalhaX, mulequeBatalhaY

    display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
    display.blit(slimeBatalha, (slimeBatalhaX, slimeBatalhaY))
    display.blit(mulequeBatalha, (mulequeBatalhaX, mulequeBatalhaY))
    

#Evento função

randon=0
def evento():
    global display, randon 
    from random import randrange
    randon=randrange(0, 5)
    if radon == 1:
        batalha()
    
'''

#Lojinha função

def lojinha1():
    

    
def lojinha2():
    

    
def lojinha3():

    
'''


#Dado função:
dado=0

def girar():
    global display, dados, dado
    from random import randrange
    dado=randrange(0, 5)
    display.blit(dados[dado], (661, 462))
    dado += 1
    

#mover-se função
def mover():
    global mulequeOverX,mulequeOverY,dado
    print(dado)
    for i in range(dado):
        #Chamar as funções de lojinha aqui
        '''
        if mulequeOverX == 358 and mulequeOverY == 215:
            (função lojinha1)
            
        if mulequeOverX == 358 and mulequeOverY == 307:
            (função lojinha2)
            
        if mulequeOverX == 542 and mulequeOverY == 399:
            (função lojinha3)
        
        '''
        #primeira casa
        if mulequeOverX == 634 and mulequeOverY == 399:
            mulequeOverX = 634
            mulequeOverY = 399
        
        elif mulequeOverX == 36 and mulequeOverY == 215:
            mulequeOverX += (46)
        
        elif mulequeOverY == 399:
            mulequeOverX += (46)
        
        elif mulequeOverX == 36:
            mulequeOverY += (46)

        elif mulequeOverY == 307:
            mulequeOverX -= (46)

        elif mulequeOverX == 726:
            mulequeOverY += (46)
        
        elif mulequeOverY == 215:
            mulequeOverX += (46)
            
        elif mulequeOverX == 634 and mulequeOverY == 399:
            mulequeOverX = 634
            mulequeOverY = 399

        else:
            print("Faiou")



#jogo em ato
while True:

    
    #obejetos in overword
    display.blit(mapa, (0, 0))
    display.blit(mulequeOver, (mulequeOverX, mulequeOverY))
    display.blit(slime, (slimeX, slimeY))
    
    
    
    fps.tick(5)#25
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        
	    # ele imprime os eventos para a visualização
            print(event)
            
            
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                pygame.quit()
                quit()
                sys.exit()
                   
            
  
            #movimentando o Boy:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mulequeOverX += 46
                if event.key == pygame.K_LEFT:
                    mulequeOverX -= 46
                if event.key == pygame.K_UP:
                    mulequeOverY -= 46
                if event.key == pygame.K_DOWN:
                    mulequeOverY += 46
                if event.key == pygame.K_SPACE:
                    mulequeOverXY=(mulequeOverX, mulequeOverY)
                    girar()
                    mover()
                    mulequeOverXY=(mulequeOverX, mulequeOverY)
                    '''
                    evento()
                    '''
                    

                
                    
            print(mulequeOverXY)


    

    print(pygame.mouse.get_pos())
    pygame.display.flip()
