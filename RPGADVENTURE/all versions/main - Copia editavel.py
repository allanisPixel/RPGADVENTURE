#importando bibliotecas
import pygame
import random

pygame.init() #comando que inicia o pygame

#tela #par ordenado memorizado em par e em unidade
tamanhoTela = largura, altura = 800,600
tela = pygame.display.set_mode (tamanhoTela) #?
#Atualizar o nome da tela
pygame.display.set_caption("TADS Adventure")



#Sprite Mapa
mapa = pygame.image.load("map1.png")
#Sprite dados
dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]
x,y = 0,0 #?
dadon= 0 #?



#rodando
while True:
    tela.blit(mapa, (0, 0))
