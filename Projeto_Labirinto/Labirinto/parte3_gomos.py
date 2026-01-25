#PYTHON
import pygame
import math
import random

pygame.init()
tela = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Parte3 - Gomos / Processos")

clock = pygame.time.Clock()
CENTRO = (400,400)

# Camadas com cores
camadas = [
    {"raio": 60,"cor": (255,200,0), "gomos": 6},
    {"raio": 120,"cor":(255,140,0), "gomos": 10},
    {"raio": 180,"cor":(255,110,40), "gomos":14},
    {"raio": 240,"cor":(255,180,120), "gomos":18},
]

tempo = 0

rodando = True
while rodando:
    #linha que faz abrir a janela
    tela.fill((12,12,12))
    
    for evento in pygame.event.get():
        if evento.type ==  pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
    
    tempo += 0.02 #linha pra velocidade                
    
    #Kernel
    pygame.draw.circle(tela, (255, 210, 0), CENTRO, 18)
    
    #Desenhar camadas e gomos
    for camada in camadas:
        raio_base = camada["raio"]
        
        for i in range(camada["gomos"]):
            ang_base = (2 * math.pi / camada["gomos"]) * i
            
            #Pulso individual do processo
            pulso = math.sin(tempo * 2 + i) * 5
            
            raio = raio_base + pulso
            
            x = CENTRO[0]+ raio * math.cos(ang_base)
            y = CENTRO[1]+ raio * math.sin(ang_base)
            
            pygame.draw.line(
                tela,
                camada["cor"],
                CENTRO,
                (int(x), int(y)),
                2
            )
            
                
            
            
        pygame.display.flip()
        clock.tick(60)    


pygame.quit()