#python
import pygame
import math

pygame.init()

tela = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Parte2 - Camadas Orgânicas")

clock = pygame.time.Clock()

CENTRO = (400, 400)

# Camadas base
camadas = [
    {"raio": 50, "fase": 0, "cor": (255,200,0)},# Kernei Layer
    {"raio": 110, "fase": 1, "cor":(255,140,0)},# Drives
    {"raio": 170, "fase": 2, "cor":(255,110,40)},# Sistem
    {"raio": 230, "fase": 3, "cor":(255,180,120)},# Serviços/Usuario
]

tempo = 0

rodando = True
while rodando:
    tela.fill((12,12,12))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
                
    tempo += 0.02     
    
    # Kernel
    
    pygame.draw.circle(tela,(255, 180, 0), CENTRO, 15)
    
    #Camadas vivas
    
    for camada in camadas:
        pulso = math.sin(tempo + camada["fase"]) * 4
        
        raio_atual = camada["raio"] + pulso
        
        pygame.draw.circle(
            tela,
            camada["cor"],
            CENTRO,
            int(raio_atual),
            2
            
        )  
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()                 