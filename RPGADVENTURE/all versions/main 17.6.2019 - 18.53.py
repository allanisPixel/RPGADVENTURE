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
fonte = pygame.font.SysFont(None,25) #"AsepriteFont.ttf"

#------------------------------- C O L O R S ---------------------------------------

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
verde = (0,255,0)
azul = (0,0,255)

#------------------------------- O B J E T O S - BLIT-SPRITES ----------------------

#Coisas com sprite
#Intro
telaInicial = pygame.image.load("telaInicial.png")
start = pygame.image.load("start.png")


#Over
mulequeOver = pygame.image.load("mulekeoverword.png")
mapa = pygame.image.load("map1.png")
slime = pygame.image.load("slime 0.png")

#menus over
menu = pygame.image.load("menu.png")
inventario = pygame.image.load("inventario.png")

#lojinha
lojinha = pygame.image.load("lojinha.png")
buy = pygame.image.load("buy.png")
saida = pygame.image.load("saida.png")


#batalha
campoBatalha = pygame.image.load("telaDeBatalha.png")
menuDeBatalha = pygame.image.load("menuDeBatalha.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")
mucegu = pygame.image.load("mucegu.png")
rato = pygame.image.load("Rato.png")
slimeBatalha = pygame.image.load("slime 0.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")
attack = pygame.image.load("attack.png")
itens = pygame.image.load("itens.png")


#Dado
dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]

#Itens
espada = [pygame.image.load("espada lv0.png"),pygame.image.load("espada lv1.png"),
          pygame.image.load("espada lv2.png"),pygame.image.load("espada lv3.png")]
         
escudo = [pygame.image.load("escudo lv0.png"),pygame.image.load("escudo lv1.png"),
          pygame.image.load("escudo lv2.png"),pygame.image.load("escudo lv3.png")]

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

#cordenadas no inventario #Isso aqui tem que ser atualizado após cada compra

swordX, swordY = (42), (480)
shildX, shildY = (95), (480)
potionX, potionY = (147), (480)
#-------------------------------- BLITANDO TRECHOS DE CODIGOS RE-PRINT ----------------------------
def blitOver():
    display.blit(mapa, (0, 0))
    display.blit(mulequeOver, (mulequeOverX, mulequeOverY))
    display.blit(slime, (slimeX, slimeY))
    display.blit(menu, (menuX, menuY))

    texto(str(HP),preto,menu,187,21)
    texto(str(ATC),preto,menu,187,50)
    texto(str(DEF),preto,menu,187,77)
    texto(str(DIN),preto,menu,187,103)
    
    display.blit(inventario, (inventarioX, inventarioY))
    display.blit(espada[sword], (swordX, swordY ))
    display.blit(escudo[shild], (shildX, shildY))
    display.blit(poção[potion], (potionX, potionY))
    
    pygame.display.update()

def blitLojinha1():
    texto("10",preto,lojinha,75,57)
    texto("10",preto,lojinha,75,110)
    texto("10",preto,lojinha,75,155)
    texto("1",preto,lojinha,50,80)
    texto("1",preto,lojinha,50,129)
    texto("1",preto,lojinha,50,176)
    texto(str(DIN),preto,lojinha,55,200)
    display.blit(lojinha, (lojinhaX, lojinhaY))
    display.blit(espada[1], (espadaX, espadaY))
    display.blit(escudo[1], (escudoX, escudoY))
    display.blit(poção[1], (poçãoX, poçãoY))
    display.blit(buy, (360, 247)) 
    display.blit(buy, (360, 297)) 
    display.blit(buy, (360, 343))
    display.blit(saida, (537, 177))
    pygame.display.update()


'''
def blitLojinha2():




def blitLojinha3():
'''


#-------------------------------- F U N Ç Õ E -----------------------------------------------------
#Função Especial para textos
#Obs.: aqui tem um monte de variaveis a serem criadas
def texto(textoAqui, corTexto, superfice, textoX, textoY):
    msg = fonte.render(textoAqui, True, corTexto)
    superfice.blit(msg,[textoX, textoY])
    
#Dados do minino
HP = 100
DEF = 0
ATC = 0
DIN = 1000 #mude isso despues
POT = 0

#Dados atributos dos ITENS ====== Real/Teorico
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

# --------Vairaveis dos mobs------

mobHP = 0 #inicio de batatra = X no fim tem que voltar a 0 e isso sera uma condição lida

# --------Tipo do item -----------
sword = 0
shild = 0 
potion = 0

#batalha função:
def batalhaSlime():
    global display, campoBatalha, campoBatalhaX, campoBatalhaY, slimeBatalha, slimeBatalhaX, slimeBatalhaY ,mulequeBatalha, mulequeBatalhaX, mulequeBatalhaY, batalhaAcontece
    batalhaAcontece = True
    while batalhaAcontece:
    
        display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
        display.blit(slimeBatalha, (slimeBatalhaX, slimeBatalhaY))
        display.blit(mulequeBatalha, (mulequeBatalhaX, mulequeBatalhaY))

        pygame.display.update()
        
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    batalhaAcontece = False

#Evento função
#if mulequeOverX ==  and mulequeOverY ==  or
randon=0

def evento():
    
    global display, randon
    if mulequeOverX ==  128 and mulequeOverY == 215: #or mulequeOverX == 174 and mulequeOverY == 215 or mulequeOverX == 220 and mulequeOverY == 215 or mulequeOverX == 266 and mulequeOverY == 215:
 
        from random import randrange
        randon=randrange(0, 5)
        if randon == 1:
            batalhaSlime()
    
#Lojinha função

def lojinha1():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY, event, HP, DEF, ATC, DIN, sword, shild, potion
    lojaAberta = True
    while lojaAberta:
        blitLojinha1()

        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 537 and Ymouse > 177 and Xmouse < 565 and Ymouse < 206:
                    lojaAberta = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if Xmouse > Xdesenho 'and' Ymouse > Ydesnho --->
                # 'and' Xmouse < Xdesnho + larguraDesnho 'and' Ymouse < Ydesenho + tamanhoDesnho
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 247 and Xmouse < 394 and Ymouse < 263:
                    ATC = espadalv1
                    DIN -= 10
                    sword = 1
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 299 and Xmouse < 394 and Ymouse < 312:
                    DEF = escudolv1
                    DIN -= 10
                    shild = 1 
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 344 and Xmouse < 394 and Ymouse < 357:
                    POT = poçãolv1
                    DIN -= 10
                    potion = 1
                      
        

def lojinha2():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY, event, HP, DEF, ATC, DIN, sword, shild, potion
    lojaAberta = True
    while lojaAberta:
        
        texto("20",preto,lojinha,75,57)
        texto("20",preto,lojinha,75,110)
        texto("20",preto,lojinha,75,155)
        texto("2",preto,lojinha,50,80)
        texto("2",preto,lojinha,50,129)
        texto("2",preto,lojinha,50,176)
        texto(str(DIN),preto,lojinha,55,200)
        display.blit(lojinha, (lojinhaX, lojinhaY))
        display.blit(espada[2], (espadaX, espadaY))
        display.blit(escudo[2], (escudoX, escudoY))
        display.blit(poção[2], (poçãoX, poçãoY))
        display.blit(buy, (360, 247)) 
        display.blit(buy, (360, 297)) 
        display.blit(buy, (360, 343)) 
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 537 and Ymouse > 177 and Xmouse < 565 and Ymouse < 206:
                    lojaAberta = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 247 and Xmouse < 394 and Ymouse < 263:
                    ATC = espadalv2
                    DIN -= 20
                    sword = 2
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 299 and Xmouse < 394 and Ymouse < 312:
                    DEF = escudolv2
                    DIN -= 20
                    shild = 2 
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 344 and Xmouse < 394 and Ymouse < 357:
                    POT = poçãolv2
                    DIN -= 20
                    potion = 2
                      
                pygame.display.update()
                
def lojinha3():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY, event, HP, DEF, ATC, DIN, sword, shild, potion
    lojaAberta = True
    while lojaAberta:
        
        texto("30",preto,lojinha,75,57)
        texto("30",preto,lojinha,75,110)
        texto("30",preto,lojinha,75,155)
        texto("3",preto,lojinha,50,80)
        texto("3",preto,lojinha,50,129)
        texto("3",preto,lojinha,50,176)
        texto(str(DIN),preto,lojinha,55,200)
        display.blit(lojinha, (lojinhaX, lojinhaY))
        display.blit(espada[3], (espadaX, espadaY))
        display.blit(escudo[3], (escudoX, escudoY))
        display.blit(poção[3], (poçãoX, poçãoY))
        display.blit(buy, (360, 247)) 
        display.blit(buy, (360, 297)) 
        display.blit(buy, (360, 343)) 
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 537 and Ymouse > 177 and Xmouse < 565 and Ymouse < 206:
                    lojaAberta = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 247 and Xmouse < 394 and Ymouse < 263:
                    ATC = espadalv3
                    DIN -= 30
                    sword = 3
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 299 and Xmouse < 394 and Ymouse < 312:
                    DEF = escudolv3
                    DIN -= 30
                    shild = 3 
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 344 and Xmouse < 394 and Ymouse < 357:
                    POT = poçãolv3
                    DIN -= 30
                    potion = 3
                      
                pygame.display.update()
    

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
    batalhaAcontece = False
    
    #obejetos in overword
    blitOver()
    
    fps.tick(5)#25
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
            
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
                evento()
                blitOver()
                
                
                
                
                   
    pygame.display.flip()
