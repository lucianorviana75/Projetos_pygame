import pygame
import math
#--------
#JANELA
#--------
LARGURA, ALTURA = 800, 800

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Fase 9 - LAbirinto Radial")

CENTRO = (LARGURA // 2, ALTURA // 2)
clock = pygame.time.Clock() 
rodando = True
#-----------------------
#ESTRUTURADO LABIRINTO
#-----------------------
#Caminhos (raios)

quantidade_raios = 24
raio_max = 260

#paredes(arcos)

paredes = [
    {"raio":80, "inicio":0.0,          "fim":math.pi / 2},
    {"raio":120,"inicio":math.pi,      "fim":math.pi * 1.4},
    {"raio":160,"inicio":math.pi / 3,  "fim":math.pi},
    {"raio":200,"inicio":math.pi * 1.5,"fim":math.pi * 19},
    ]
#--------------------------
#LOOP PRINCIPAL
#--------------------------

while rodando:
    
    #Limpa a tela
    tela.fill((12,12,12))
    
    #Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False     
    #Paredes (Arcos)
    for parede in paredes:
        r = parede["raio"]
        rect = pygame.Rect(
            CENTRO[0] - r,
            CENTRO[1] - r,
            r * 2,
            r * 2
            
        )
        pygame.draw.arc(
            tela,
            (120,120,120),
            rect,
            parede["inicio"],
            parede["fim"],
            4
        )
    #Caminhos (Raios)
    for i in range(quantidade_raios):
        angulo = (2 * math.pi / quantidade_raios) *i
        X_fim = CENTRO[0] + raio_max * math.cos(angulo)
        y_fim = CENTRO[1] + raio_max * math.sin(angulo)
        
        pygame.draw.line(
            tela,
            (180,180,180),
            CENTRO,
            (int(X_fim), int(y_fim)),
            1
        )
        
    #Nucleo
    pygame.draw.circle(
        tela,
        (255,200,60),
        CENTRO,
        18
    )
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()        