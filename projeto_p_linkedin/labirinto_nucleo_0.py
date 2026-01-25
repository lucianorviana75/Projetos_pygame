import pygame
import math


pygame.init()

#janela
LARGURA,ALTURA = 800,600
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Labirinto Linux - do Kernel para o usuario")

#Centro
CENTRO =(LARGURA // 2, ALTURA // 2)

clock = pygame.time.Clock() 
rodando = True

# Camadas (inspiradas em sistemas)
camadas = [
    {"raio": 80, "cor" :(255,165,0)}, #kernel (laranja)
    {"raio": 130,"cor" :(0,200,255)}, #Drivers
    {"raio": 180,"cor":(0,255,120)}, #serviços
    {"raio": 230,"cor":(180,180,180)}, #User Space
]

while rodando:
    tela.fill((10,10,10))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
                
    # Desenhar camadas
    for camada in camadas:
        pygame.draw.circle(
            tela,
            camada["cor"],
            CENTRO,
            camada["raio"],
            3
            
        )                
    pygame.display.flip()
    clock.tick(60)
pygame.quit()