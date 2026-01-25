import pygame
import math

pygame.init()

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
                    
            
        
    #Tempo    
    tempo += 0.003
    
    #Pulso do nucleo(respiração)
    pulso = math.sin(tempo) * 4
    raio_nucleo = int(20 + pulso)
    
    #Cor viva mais calma
    cor_nucleo = (220,180,40)
    
    pygame.draw.circle(tela, cor_nucleo, CENTRO, raio_nucleo)

    pygame.display.flip()
    clock.tick(60)  
      
pygame.quit()