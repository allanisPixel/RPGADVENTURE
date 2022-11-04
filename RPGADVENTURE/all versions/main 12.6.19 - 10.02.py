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

#-------------------------------O B J E T O S - BLIT-SPRITES ----------------------

#Coisas com sprite

#Over
MulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

#batalha
campoBatalha = pygame.image.load("telaDeBatalha.png")
Muleque = pygame.image.load("mulekeloco.png")
Mucegu = pygame.image.load("mucegu.png")
Rato = pygame.image.load("Rato.png")
Slime = pygame.image.load("slime 0.png")

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

#-------------------------------O B J E T O S - C O R D E N A D A S -----------------------------------
#coordenadas das coisas com sprite

SlimeX, SlimeY = 680,401
MulequeOverX, MulequeOverY = 36, 215
MulequeOverXY=(0,0)
#Cordenadas do boy
boyX,boyY=36,215

#Cordenadas das coisa na batalha
campoBatalhaX, campoBatalhaY = 10,10


#--------------------------------F U N Ç Õ E -----------------------------------------------------

#batalha função:
def batalha():
    global campoBatalha, campoBatalhaX, campoBatalhaY
    display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
    


'''
#Evento função
def evento():
    global 
    batalha()
'''    
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
    global MulequeOverX,MulequeOverY,dado
    print(dado)
    for i in range(dado):
        #Chamar as funções de lojinha aqui
        '''
        if MulequeOverX == 358 and MulequeOverY == 215:
            (função lojinha1)
            
        if MulequeOverX == 358 and MulequeOverY == 307:
            (função lojinha2)
            
        if MulequeOverX == 542 and MulequeOverY == 399:
            (função lojinha3)
        
        '''
        #primeira casa
        if MulequeOverX == 634 and MulequeOverY == 399:
            MulequeOverX = 634
            MulequeOverY = 399
        
        elif MulequeOverX == 36 and MulequeOverY == 215:
            MulequeOverX += (46)
        
        elif MulequeOverY == 399:
            MulequeOverX += (46)
        
        elif MulequeOverX == 36:
            MulequeOverY += (46)

        elif MulequeOverY == 307:
            MulequeOverX -= (46)

        elif MulequeOverX == 726:
            MulequeOverY += (46)
        
        elif MulequeOverY == 215:
            MulequeOverX += (46)
            
        elif MulequeOverX == 634 and MulequeOverY == 399:
            MulequeOverX = 634
            MulequeOverY = 399

        else:
            print("Faiou")



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
                    MulequeOverXY=(MulequeOverX, MulequeOverY)
                    girar()
                    mover()
                    MulequeOverXY=(MulequeOverX, MulequeOverY)
                    '''
                    evento()
                    '''
                    batalha()
                    
            print(MulequeOverXY)


            #Tentando Eventos:
            

                        
    

        #obejetos in overword
    display.blit(slime, (SlimeX, SlimeY))
    display.blit(MulequeOver, (MulequeOverX, MulequeOverY))

    

    print(pygame.mouse.get_pos())
    pygame.display.flip()
