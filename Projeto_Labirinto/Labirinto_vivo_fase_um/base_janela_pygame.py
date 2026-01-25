import pygame
#import math
#import random

#janela
pygame.init()
LARGURA, ALTURA = 600, 600
TELA = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Programa de treino")
#centro
CENTRO = (LARGURA // 2, ALTURA // 2)
#tempo
clock = pygame.time.Clock()

rodando = True

while rodando:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.KEY == pygame.K_ESCAPE:
                rodando = False       

    
    pygame.display.flip()
pygame.quit()
