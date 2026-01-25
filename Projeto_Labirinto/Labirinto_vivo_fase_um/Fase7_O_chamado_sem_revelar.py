import pygame
import math

pygame.init()

energia = 0

# Janela
LARGURA, ALTURA = 800, 800
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Sistema vivo")

#Centro
CENTRO = (LARGURA // 2, ALTURA // 2)

# Tempo
clock = pygame.time.Clock() 
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
                    
    #Parametros dos raios        
    quantidade_raios = 24
    comprimento_base = 120
    #os raios respiram
    pulso_raios = math.sin(tempo * 2) * 20
    comprimento = comprimento_base + pulso_raios
    
    for i in range(quantidade_raios):
        
        #Antes angulo perfeito
        desvio = math.sin(tempo * 0.6 + i) * 0.2
        #Agora ângulo orgânico
        angulo = (2 * math.pi / quantidade_raios) * i + desvio
        
        x = CENTRO[0] + comprimento * math.cos(angulo)
        y = CENTRO[1] + comprimento * math.sin(angulo)
        
        ritmo = math.sin(tempo* 1.5 + i)
        if ritmo > 0.2:
            pygame.draw.line(
                tela,
                (180, 180, 180),
                CENTRO,
                (int(x), int(y)),
                1
            
        )
            
    #Tempo    
    tempo += 0.003
    
    #Pulso do nucleo(respiração)
    pulso_base =math.sin(tempo) * 2
    
    # quanto mais atividade, mais o núcleo se retrai
    raio_nucleo = int(26 + pulso_base - energia * 0.3)
    raio_nucleo = max(10, min(30, raio_nucleo))
    
    #Cor viva mais calma
    cor_nucleo = (
        255,
        min(200, int(120 + energia * 2)),
        40
    )
    
    pygame.draw.circle(tela, cor_nucleo, CENTRO, raio_nucleo)
    energia = 0
    pygame.display.flip()
    clock.tick(60)  
      
pygame.quit()