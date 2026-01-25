import pygame

pygame.init()
#janela
LARGURA,ALTURA = 800,600
TELA = pygame.display.set_mode((800,600))
pygame.display.set_caption("teste")

rodando = True
while rodando:
    
    
    pygame.display.flip()
    
    
pygame.quit()    
    