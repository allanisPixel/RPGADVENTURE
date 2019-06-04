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
mapa= pygame.image.load("map1.png")
slime=[pygame.image.load("slime 1.png"),pygame.image.load("slime 2.png") ]
dados = [pygame.image.load("dieWhite_border1.png"),pygame.image.load("dieWhite_border2.png"),
         pygame.image.load("dieWhite_border3.png"),pygame.image.load("dieWhite_border4.png"),
         pygame.image.load("dieWhite_border5.png"),pygame.image.load("dieWhite_border6.png")]
x, y = 0, 0
dadon=0
while True:
    keys = pygame.key.get_pressed()
    display.blit(mapa, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    display.blit(slime[x], (x, y))
    x+=1
    display.blit(dados[dadon], (661, 462))
    if x == len(slime):
        x = 0
    print(pygame.mouse.get_pos())
    pygame.display.flip()
