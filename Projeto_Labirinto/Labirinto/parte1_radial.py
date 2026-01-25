import pygame
import math
pygame.init()

tela = pygame.display.set_mode((800,800))#comando que da tamanho a tela
pygame.display.set_caption("Parte 1 - Espaço Radial")

clock = pygame.time.Clock()

centro =(400, 400)
raio = 150 
angulo = 0

rodando = True
while rodando :
    tela.fill((10,10,10))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False    
            
    angulo += 0.003
    
    X = centro[0] + raio * math.cos(angulo)
    Y = centro[1] + raio* math.sin(angulo)
    
    pygame.draw.circle(tela, (255, 150,0),centro, 5)
    pygame.draw.circle(tela, (255,200,0), (int(X), int(Y)), 8)   
    
    pygame.display.flip()
    
pygame.quit()         