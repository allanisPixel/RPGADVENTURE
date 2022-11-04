import pygame
import random
import sys
import time

#some defesa com HP

#sons MP#
#efeitos WAV
#Inicio de tudo
pygame.init()
tamanho = Largura, altura = 800, 600
display = pygame.display.set_mode (tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("TADS Adventure")# (virgula) icone do titulo
fonte = pygame.font.SysFont(None,25) #"AsepriteFont.ttf"

'''
pygame.mixer.music.load("Musica ambiente.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.stop()
pygame.mixer.music.unpause()
'''

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
torre = pygame.image.load("torre.png")

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
abelhas = pygame.image.load("abelhas.png")
rato = pygame.image.load("rato.png")
slimeBatalha = pygame.image.load("slime 0.png")
mulequeBatalha = pygame.image.load("mulekeloco.png")
attack = pygame.image.load("attack.png")
itens = pygame.image.load("itens.png")
boss = pygame.image.load("boss.png")



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
torreX, torreY = 680,375
mulequeOverX, mulequeOverY = 36, 215
mulequeOverXY=(0,0)

#Cordenadas do boy
boyX, boyY=36, 215

#menus over
menuX, menuY = 435, 25
inventarioX, inventarioY = 34, 468

#Cordenadas das coisa na batalha
campoBatalhaX, campoBatalhaY = 100, 10
mobBatalhaX, mobBatalhaY = 600, 260
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
    display.blit(torre, (torreX, torreY))
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
    pygame.mixer.music.stop()

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

def blitLojinha2():
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
    display.blit(saida, (537, 177))
    pygame.display.update()

def blitLojinha3():
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
    display.blit(saida, (537, 177))
    pygame.display.update()

def blitBatalhaSlime():

    display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
    display.blit(slimeBatalha, (mobBatalhaX, mobBatalhaY))
    display.blit(mulequeBatalha, (mulequeBatalhaX, mulequeBatalhaY))
    texto(str(HP),preto,campoBatalha,85,190)
    texto(str(mobHP),preto,campoBatalha,510,200)
    texto(str(ATC),preto,campoBatalha,150,362)
    texto(str(DEF),preto,campoBatalha,150,387)
    texto(str(POT),preto,campoBatalha,150,409)
        
    display.blit(espada[sword], (210, 362))
    display.blit(escudo[shild], (210, 387))
    display.blit(poção[potion], (210, 409))
    
    pygame.display.update()

def blitBatalhaAbelhas():

    display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
    display.blit(abelhas, (mobBatalhaX, mobBatalhaY))
    display.blit(mulequeBatalha, (mulequeBatalhaX, mulequeBatalhaY))
    texto(str(HP),preto,campoBatalha,85,190)
    texto(str(mobHP),preto,campoBatalha,510,200)
    texto(str(ATC),preto,campoBatalha,150,362)
    texto(str(DEF),preto,campoBatalha,150,387)
    texto(str(POT),preto,campoBatalha,150,409)
        
    display.blit(espada[sword], (210, 362))
    display.blit(escudo[shild], (210, 387))
    display.blit(poção[potion], (210, 409))
    
    pygame.display.update()

def blitBatalhaRato():
    
    display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
    display.blit(rato, (mobBatalhaX, mobBatalhaY))
    display.blit(mulequeBatalha, (mulequeBatalhaX, mulequeBatalhaY))
    texto(str(HP),preto,campoBatalha,85,190)
    texto(str(mobHP),preto,campoBatalha,510,200)
    texto(str(ATC),preto,campoBatalha,150,362)
    texto(str(DEF),preto,campoBatalha,150,387)
    texto(str(POT),preto,campoBatalha,150,409)
        
    display.blit(espada[sword], (210, 362))
    display.blit(escudo[shild], (210, 387))
    display.blit(poção[potion], (210, 409))
    
    pygame.display.update()

def blitBatalhaBoss():

    display.blit(campoBatalha, (campoBatalhaX, campoBatalhaY))
    display.blit(boss, (390, 90))
    display.blit(mulequeBatalha, (mulequeBatalhaX, mulequeBatalhaY))
    texto(str(HP),preto,campoBatalha,85,190)
    texto(str(mobHP),preto,campoBatalha,400,90)
    texto(str(ATC),preto,campoBatalha,150,362)
    texto(str(DEF),preto,campoBatalha,150,387)
    texto(str(POT),preto,campoBatalha,150,409)
        
    display.blit(espada[sword], (210, 362))
    display.blit(escudo[shild], (210, 387))
    display.blit(poção[potion], (210, 409))

    pygame.display.update()
    
#-------------------------------- F U N Ç Õ E -----------------------------------------------------
#Função Especial para textos
#Obs.: aqui tem um monte de variaveis a serem criadas
def texto(textoAqui, corTexto, superfice, textoX, textoY):
    msg = fonte.render(textoAqui, True, corTexto)
    superfice.blit(msg,[textoX, textoY])
    
#Dados do minino
HP = 150
DEF = 10
ATC = 10
DIN = 0 #mude isso despues
POT = 0

# --------Tipo do item -----------
sword = 0
shild = 0 
potion = 0

# --------Vairaveis dos mobs------
#inicio de batatra = X no fim tem que voltar a 0 e isso sera uma condição lida

mobHP = 0 
mobDAN = 0

def vezmob(): 
    global HP, mobDAN, DEF
    HP -= (mobDAN - DEF)

#batalha função:
def batalhaSlime():   
    global display, campoBatalha, campoBatalhaX, campoBatalhaY, slimeBatalha, slimeBatalhaX, slimeBatalhaY ,mulequeBatalha, mulequeBatalhaX, mulequeBatalhaY, batalhaAcontece, HP, POT ,mobHP, ATC, DEF, mobHP, mobDAN                   

    mobHP = 50 
    mobDAN = 15
    
    batalhaAcontece = True
    while batalhaAcontece:
        '''

        '''
        blitBatalhaSlime()
        
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    batalhaAcontece = False
                    vezmob()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 370 and Xmouse < 206 and Ymouse < 400:
                    mobHP -= ATC
                    #
                    vezmob()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 406 and Xmouse < 206 and Ymouse < 434:
                    HP += POT
                    #
                    vezmob()    
            if mobHP <= 0:
                texto("Você ganhou.",preto,campoBatalha,220,360)

            if HP <= 0:
                texto("Você perdeu.",preto,campoBatalha,220,360)

def batalhaAbelha():   
    global display, campoBatalha, campoBatalhaX, campoBatalhaY, slimeBatalha, slimeBatalhaX, slimeBatalhaY ,mulequeBatalha, mulequeBatalhaX, mulequeBatalhaY, batalhaAcontece, HP, POT ,mobHP, ATC, DEF, mobHP, mobDAN                   

    mobHP = 75 
    mobDAN = 20
    
    batalhaAcontece = True
    while batalhaAcontece:
        '''

        '''
        blitBatalhaAbelhas()
        
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    batalhaAcontece = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 370 and Xmouse < 206 and Ymouse < 400:
                    mobHP -= ATC
                    #
                    vezmob()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 406 and Xmouse < 206 and Ymouse < 434:
                    HP += POT
                    #
                    vezmob()    
            if mobHP <= 0:
                texto("Você ganhou.",preto,campoBatalha,220,360)

            if HP <= 0:
                texto("Você perdeu.",preto,campoBatalha,220,360)

def batalhaRato():   
    global display, campoBatalha, campoBatalhaX, campoBatalhaY, slimeBatalha, slimeBatalhaX, slimeBatalhaY ,mulequeBatalha, mulequeBatalhaX, mulequeBatalhaY, batalhaAcontece, HP, POT ,mobHP, ATC, DEF, mobHP, mobDAN                   

    mobHP = 80 
    mobDAN = 15
    
    batalhaAcontece = True
    while batalhaAcontece:
        '''

        '''
        blitBatalhaRato()
        
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    batalhaAcontece = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 370 and Xmouse < 206 and Ymouse < 400:
                    mobHP -= ATC
                    #
                    vezmob()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 406 and Xmouse < 206 and Ymouse < 434:
                    HP += POT
                    #
                    vezmob()    
            if mobHP <= 0:
                texto("Você ganhou.",preto,campoBatalha,220,360)

            if HP <= 0:
                texto("Você perdeu.",preto,campoBatalha,220,360)

def batalhaBoss():   
    global display, campoBatalha, campoBatalhaX, campoBatalhaY, slimeBatalha, slimeBatalhaX, slimeBatalhaY ,mulequeBatalha, mulequeBatalhaX, mulequeBatalhaY, batalhaAcontece, HP, POT ,mobHP, ATC, DEF, mobHP, mobDAN                   

    mobHP = 100 
    mobDAN = 20
    
    batalhaAcontece = True
    while batalhaAcontece:
        '''

        '''
        blitBatalhaBoss()
        
        for event in pygame.event.get():   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    batalhaAcontece = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 370 and Xmouse < 206 and Ymouse < 400:
                    mobHP -= ATC
                    #
                    vezmob()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 110 and Ymouse > 406 and Xmouse < 206 and Ymouse < 434:
                    HP += POT
                    #
                    vezmob()    
            if mobHP <= 0:
                texto("Você ganhou.",preto,campoBatalha,220,360)

            if HP <= 0:
                texto("Você perdeu.",preto,campoBatalha,220,360)
                
#Evento função
# mulequeOverX ==  and mulequeOverY ==  or
                    
randon=0
def evento():
    global display, randon, DIN
    if mulequeOverX == 634 and mulequeOverY == 399:
        batalhaBoss()
    
    elif mulequeOverX ==  128 and mulequeOverY == 215 or mulequeOverX == 174 and mulequeOverY == 215 or mulequeOverX == 220 and mulequeOverY == 215 or mulequeOverX == 266 and mulequeOverY == 215 or mulequeOverX == 404 and mulequeOverY == 215 or mulequeOverX == 450 and mulequeOverY == 215 or mulequeOverX == 496 and mulequeOverY == 215 or mulequeOverX == 542 and mulequeOverY == 215 or mulequeOverX == 634 and mulequeOverY == 215 or mulequeOverX == 680 and mulequeOverY == 215 or mulequeOverX == 726 and mulequeOverY == 215 or mulequeOverX == 726 and mulequeOverY == 261 or mulequeOverX == 726 and mulequeOverY == 307 or mulequeOverX == 588 and mulequeOverY == 307 or mulequeOverX == 542 and mulequeOverY == 307 or mulequeOverX == 496 and mulequeOverY == 307 or mulequeOverX == 450 and mulequeOverY == 307 or mulequeOverX == 404 and mulequeOverY == 307 or mulequeOverX == 312 and mulequeOverY == 307 or mulequeOverX == 266 and mulequeOverY == 307 or mulequeOverX == 220 and mulequeOverY == 307 or mulequeOverX == 174 and mulequeOverY == 307 or mulequeOverX == 82 and mulequeOverY == 307 or mulequeOverX == 36 and mulequeOverY == 307 or mulequeOverX == 36 and mulequeOverY == 399 or mulequeOverX == 82 and mulequeOverY == 399 or mulequeOverX == 174 and mulequeOverY == 399 or mulequeOverX == 220 and mulequeOverY == 399 or mulequeOverX == 312 and mulequeOverY == 399 or mulequeOverX == 358 and mulequeOverY == 399 or mulequeOverX == 404 and mulequeOverY == 399 or mulequeOverX == 450 and mulequeOverY == 399 or mulequeOverX == 496 and mulequeOverY == 399 or mulequeOverX == 588 and mulequeOverY == 399:
        from random import randrange
        randon = randrange(0, 5)
        print(randon)
        if randon == 0:
            batalhaSlime()
        if randon == 1:
            batalhaAbelha()
        if randon == 2:
            batalhaRato()
        if randon == 3:
            batalhaSlime()
        if randon == 4:
            DIN += 250
            mony=True
            while mony:
                texto("Você achou 250$.Press X para continuar.",preto,menuDeBatalha,0,50)    
                display.blit(menuDeBatalha, (150, 150))
                pygame.display.update()
                for event in pygame.event.get():   
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            mony = False            
            
        if randon == 5:
            while mony:
                DIN += 150
                texto("Você achou 150$.Press X para continuar.",preto,menuDeBatalha,0,50)    
                display.blit(menuDeBatalha, (150, 150))
                pygame.display.update()
                for event in pygame.event.get():   
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            mony = False
                            
#Lojinha função

def lojinha1():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY, event, HP, DEF, ATC, DIN, POT, sword, shild, potion

    pygame.mixer.music.stop()
    pygame.mixer.music.load("lojinha.mp3")
    pygame.mixer.music.play(loops=-1)
    
    lojaAberta = True
    while lojaAberta:
        blitLojinha1()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 537 and Ymouse > 177 and Xmouse < 565 and Ymouse < 206:
                    pygame.mixer.music.stop()
                    lojaAberta = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # if Xmouse > Xdesenho 'and' Ymouse > Ydesnho --->
                # 'and' Xmouse < Xdesnho + larguraDesnho 'and' Ymouse < Ydesenho + tamanhoDesnho
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 247 and Xmouse < 394 and Ymouse < 263:
                    DIN -= 10
                    sword = 1
                    ATC = 20
                    #
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 299 and Xmouse < 394 and Ymouse < 312:
                    DIN -= 10
                    shild = 1
                    DEF = 25
                    #
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 344 and Xmouse < 394 and Ymouse < 357:
                    DIN -= 10
                    potion = 1
                    POT = 25
                    #
                    
            blitLojinha1()     
        

def lojinha2():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY, event, HP, DEF, ATC, DIN, POT, sword, shild, potion
    lojaAberta = True
    while lojaAberta:
        
        blitLojinha2()
        
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
                    DIN -= 20
                    sword = 2
                    ATC = 20
                    #
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 299 and Xmouse < 394 and Ymouse < 312:
                    DIN -= 20
                    shild = 2
                    DEF = 50
                    #
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 344 and Xmouse < 394 and Ymouse < 357:
                    DIN -= 20
                    potion = 2
                    POT = 50
                    #
                      
            blitLojinha2()
                
def lojinha3():
    global display, lojinha, lojinhaX, lojinhaY, espada, espadaX, espadaY, escudo, escudoX, escudoY, poção, poçãoX, poçãoY, event, HP, DEF, ATC, DIN, POT, sword, shild, potion
    lojaAberta = True
    while lojaAberta:
        blitLojinha3()
        
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
                    DIN -= 30
                    sword = 3
                    ATC = 50
                    #
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 299 and Xmouse < 394 and Ymouse < 312:
                    DIN -= 30
                    shild = 3
                    DEF = 100
                    #
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                Xmouse = pygame.mouse.get_pos()[0]
                Ymouse = pygame.mouse.get_pos()[1]
                if Xmouse > 360 and Ymouse > 344 and Xmouse < 394 and Ymouse < 357:
                    DIN -= 30
                    potion = 3
                    POT = 75
                    #
                      
            blitLojinha3()
    
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
def jogo():
    global display, mulequeOverX, mulequeOverY, mulequeOverXY
    pygame.mixer.music.load("Musica ambiente.mp3")
    pygame.mixer.music.play(loops=-1)
    play = True
    while play:
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
                print(mulequeOverXY)
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
                    print(mulequeOverXY)
                    evento()
                    blitOver()
                    lojinhas()
            
        pygame.display.flip()
#jogo em ato
jogo()
