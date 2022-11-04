import pygame
import random
import sys
import time
#sons MP#
#efeitos WAV
#Inicio de tudo
pygame.init()
tamanho = Largura, altura = 800, 600
display = pygame.display.set_mode (tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("TADS Adventure")# (virgula) icone do titulo
fonte = pygame.font.SysFont("AsepriteFont.ttf",25)
#------------------------------- O B J E T O S - BLIT-SPRITES ----------------------

#Coisas com sprite

#Over
mulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

#menus over
menu = pygame.image.load("menu.png")
inventario = pygame.image.load("inventario.png")

#lojinha
lojinha = pygame.image.load("lojinha.png")



#batalha
campoBatalha = pygame.image.load("telaDeBatalha.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")
mucegu = pygame.image.load("mucegu.png")
rato = pygame.image.load("Rato.png")
slimeBatalha = pygame.image.load("slime 0.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")

#Dado
dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]

#Itens
espada = [pygame.image.load("espada lv0.png"),pygame.image.load("espada lv1.png"),
          pygame.image.load("espada lv2.png"),pygame.image.load("espada lv3.png")]
         
escudo = [pygame.image.load("escudo lv0.png"),pygame.image.load("escudo lv1.png"),
          pygame.image.load("escudo lv2.png"),pygame.image.load("espada lv3.png")]

poção = [pygame.image.load("poção lv0.png"),pygame.image.load("poção lv1.png"),
         pygame.image.load("poção lv2.png"),pygame.image.load("poção lv3.png")]


#------------------------------- O B J E T O S - C O R D E N A D A S -----------------------------
#coordenadas das coisas com sprite

#Over
slimeX, slimeY = 680,401
mulequeOverX, mulequeOverY = 36, 215
mulequeOverXY=(0,0)

#Cordenadas do boy
boyX, boyY=36, 215

#menus over
menuX, menuY = 435, 25
inventarioX, inventarioY = 34, 468

#Cordenadas das coisa na batalha
campoBatalhaX, campoBatalhaY = 100, 10
slimeBatalhaX, slimeBatalhaY = 638, 260
mulequeBatalhaX, mulequeBatalhaY =  177, 229

#cordenadas das coisas da lojinha

lojinhaX, lojinhaY = 284,168
espadaX, espadaY = 300,215
escudoX, escudoY = 300,265
poçãoX, poçãoY = 300,315



#-------------------------------- F U N Ç Õ E -----------------------------------------------------
#Função Especial para textos
#Obs.: aqui tem um monte de variaveis a serem criadas
def texto(textoAqui, corTexto, textoX, textoY):
    msg = font.render(textoAqui, True, corTexto)
    superfice.blit(msg,[textoX, textoY])
    

#Dados do minino
HP = 100
DEF = 0
ATC = 0
DIN = 1000 #mude isso despues




#Dados atributos dos ITENS ====== Real
# +HP
escudolv1 = 25
escudolv2 = 50
escudolv3 = 100
# +Dano
espadalv1 = 10
espadalv2 = 20
espadalv3 = 50
# Enche vida
poçãolv1 = 25
poçãolv2 = 50
poçãolv3 = 75

#batalha função:
def batalhaSlime():
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
        batalhaSlime()

#Lojinha função


def lojinha1():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY
    lojaAberta = True
    while lojaAberta:
        display.blit(lojinha, (lojinhaX, lojinhaY))
        display.blit(espada[1], (espadaX, espadaY))
        display.blit(escudo[1], (escudoX, escudoY))
        display.blit(poção[1], (poçãoX, poçãoY))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    lojaAberta = False

def lojinha2():
    global display
    display.blit(lojinha, (lojinhaX, lojinhaY))
    display.blit(espada[2], (espadaX, espadaY))
    display.blit(escudo[2], (escudoX, escudoY))
    display.blit(poção[2], (poçãoX, poçãoY))

    
def lojinha3():
    global display
    display.blit(lojinha, (lojinhaX, lojinhaY))
    display.blit(espada[3], (espadaX, espadaY))
    display.blit(escudo[3], (escudoX, escudoY))
    display.blit(poção[3], (poçãoX, poçãoY))
    

#Dado função:
dado=0

def girar():
    global display, dados, dado
    from random import randrange
    dado=randrange(0, 5)
    display.blit(dados[dado], (661, 462))
    dado += 1
    
def lojinhas():
    if mulequeOverX == 358 and mulequeOverY == 215:
        lojinha1()

    if mulequeOverX == 358 and mulequeOverY == 307:
        lojinha2()
         
    if mulequeOverX == 542 and mulequeOverY == 399:
        lojinha3()


#mover-se função
def mover():
    global mulequeOverX,mulequeOverY,dado
    print(dado)
    for i in range(dado):

        if mulequeOverX == 358 and mulequeOverY == 215 or mulequeOverX == 358 and mulequeOverY == 307 or mulequeOverX == 542 and mulequeOverY == 399:
            lojinhas()
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

    lojaAberta = False
    #obejetos in overword
    display.blit(mapa, (0, 0))
    display.blit(mulequeOver, (mulequeOverX, mulequeOverY))
    display.blit(slime, (slimeX, slimeY))
    display.blit(menu, (menuX, menuY))
    display.blit(inventario, (inventarioX, inventarioY))
    
    
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
                    lojinhas()
                    '''
                    evento()
                    '''
                    
                    
            print(mulequeOverXY)
    

    print(pygame.mouse.get_pos())
    pygame.display.flip()
