import pygame
import math

pygame.init()
# Janela
LARGURA,ALTURA =  600,400
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("sistema vivo")

# Centro
CENTRO = (LARGURA // 2 ,ALTURA // 2)

# Tempo 
clock = pygame.time.Clock
tempo = 0

while rodando:
    #O comando tela.fill ,cria uma tela com um tom de cinza quase escuro
    tela.fill((12,12,12))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    tempo += 0.003
    
    pygame.display.flip()
    clock.tick(60)        
    

pygame.quit()
