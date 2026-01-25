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
    {"raio": 80, "cor" :(255,165,0), "inicio":0.3, "fim":5.8}, #kernel (laranja)
    {"raio": 130,"cor" :(0,200,255),"inicio":1.2, "fim":6.1}, #Drivers
    {"raio": 180,"cor":(0,255,120),"inicio":0.6, "fim":4.8}, #serviços
    {"raio": 230,"cor":(180,180,180),"inicio":2.0, "fim":6.0}, #User Space
]

while rodando:
    tela.fill((10,10,10))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
                
    # Desenhar paredes do labirinto
    for camada in camadas:
        r = camada["raio"]
        rect = pygame.Rect(
            CENTRO[0] - r,
            CENTRO[1] - r,
            r * 2,
            r * 2
            
        )    
        pygame.draw.arc(
            tela,
            camada["cor"],
            rect,
            camada["inicio"],
            camada["fim"],
            4
        )            
    pygame.display.flip()
    clock.tick(60)
pygame.quit()