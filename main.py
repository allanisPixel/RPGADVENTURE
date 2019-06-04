import pygame
import random
import sys
'''
ACHAR POSIÇÃO DO SPRITE
display.blit(variaveldospriteaqui, (pygame.mouse.get_pos()))
print(pygame.mouse.get_pos())
'''
pygame.init()
tamanho = Largura, altura = 800, 600
display = pygame.display.set_mode (tamanho)
fps = pygame.time.Clock()
#coisas com sprite
x=0

MulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]

#coordenadas das coisas com sprite

SlimeX, SlimeY = 680,401
MulequeOverX, MulequeOverY = 36, 215
dadon=0

#jogo em ato
while True:
    #o programa e baseado em eventos!
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
	    # ele impre os eventos para a visualização
            print(event)
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
            #movimentando o quadrinho
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                        MulequeOverX += 46
                if event.key == pygame.K_LEFT:

                        MulequeOverX -= 46
                if event.key == pygame.K_UP:

                        MulequeOverY -= 46
                if event.key == pygame.K_DOWN:

                        MulequeOverY += 46
    display.blit(mapa, (0, 0))

        #obejetos in overword
    display.blit(slime, (SlimeX, SlimeY))
    display.blit(MulequeOver, (MulequeOverX, MulequeOverY))
    
        #Alterar os dados do retangulo
        

    
    display.blit(dados[dadon], (690, 490))
    

    print(pygame.mouse.get_pos())
    pygame.display.flip()
