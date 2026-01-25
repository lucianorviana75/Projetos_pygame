import pygame
import math
import random

pygame.init()
tela = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption("parte5 - gomos/pulso 2x1")

clock = pygame.time.Clock()
CENTRO = (400, 400)

#camadas de cores

camadas = [
    {"raio": 60,  "gomos": 12, "vel": 1.0, "amp": 3},
    {"raio": 100, "gomos": 18, "vel": 1.4, "amp": 5},
    {"raio": 140, "gomos": 24, "vel": 1.9, "amp": 8},
    {"raio": 180, "gomos": 32, "vel": 2.5, "amp": 12}
]


tempo = 0

rodando = True

#loop 
while rodando:#linha que fazabrir a janela
    tela.fill((12,12,12))
    #linhas de comando para desativar só usando a tecla esc
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False   
    #fim             
                
    tempo += 0.003 #linha da velocidade dos pulsos
    
    #kernel
    pygame.draw.circle(tela,(255,210,0), CENTRO, 18)
    
    #Desenhar camadasdo gomo
    for camada in camadas:
        raio_base = camada["raio"]
        vel = camada["vel"]
        amp = camada["amp"]
        
        #Cor dinamica
        cor = (
            min(255, int(100 + amp * 10)),
            min(255, int(50 + vel * 40)),
            0
        )
        
        
        
        for i in range(camada["gomos"]):
            ang_base = (2 * math.pi /camada["gomos"]) * i
            
            pulso_lento = math.sin(tempo * vel + i) * 6
            pulso_rapido = math.sin(tempo * vel * 2 + i) * (amp * 0.5)
            pulso = pulso_lento + pulso_rapido
            
            raio = raio_base + pulso
            
            x = CENTRO[0] + raio * math.cos(ang_base)
            y = CENTRO[1] + raio * math.sin(ang_base)
            
            angulo_inicio = ang_base
            angulo_fim = ang_base + (2 * math.pi / camada["gomos"])
            
            passos = 6
            for p in range(passos):
                a1 = angulo_inicio + (angulo_fim - angulo_inicio)*(p/ passos )
                a2 = angulo_inicio + (angulo_fim - angulo_inicio)*((p + 1)/ passos )
                
                r1 = raio_base + math.sin(tempo * 2 + i + p) * 4
                r2 = raio_base + math.sin(tempo * 2 + i + p + 1) * 4
                
                x1 = CENTRO[0] + r1 * math.cos(a1)
                y1 = CENTRO[1] + r1 * math.sin(a1)
                
                x2 = CENTRO[0] + r2 * math.cos(a2)
                y2 = CENTRO[1] + r2 * math.sin(a2)
                
                pygame.draw.line(
                    tela,
                    cor,
                    
                    (int(CENTRO[0]), int(CENTRO[1])),
                    (int(x2), int(y2)),
                    2
                )
        #faz aparecer a imagem        
        pygame.display.flip()
        clock.tick(60)        
                
            
            
                        



pygame.quit()