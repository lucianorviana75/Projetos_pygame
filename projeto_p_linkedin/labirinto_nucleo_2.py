import pygame
import math
import random


pygame.init()

#---------------------janela------------------------------------
LARGURA,ALTURA = 800,800
TELA = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Labirinto Linux -Sistema vivo ")

#Centro
CENTRO =(LARGURA // 2, ALTURA // 2)
FPS = 60
clock = pygame.time.Clock() 




#---------------------Explorador---------------------------------
explorador ={
    "angulo": 0.0,
    "camada":0
}
VEL_ANGULAR = 0.015

#----------------------cAMADAS-----------------------------------
NUM_CAMADAS = 6
RAIO_INICIAL = 90
ESPESSURA = 25
ESPACO = 15

camadas = []

for i in range(NUM_CAMADAS):
    camadas.append({
        "raio":RAIO_INICIAL + i * (ESPESSURA + ESPACO),
        "espessura": ESPESSURA,
        "angulo_saida": random.uniform(0, 2 * math.pi),
        "largura_saida":math.pi / 6,
        "vel": random.choice([-1, 1]) * random.uniform(0.002, 0.01)
    })
#-------------------funções--------------------------------------
def angulo_dentro(a, inicio,largura):
    dif = (a - inicio + math.pi) % (2 * math.pi) -math.pi
    return abs(dif) < largura / 2


def atualizar_explorador(explorador, camadas):
    explorador["angulo"] += VEL_ANGULAR
    
    if explorador["camada"] >= len(camadas):
        return
    
    camada = camadas[explorador["camada"]]
    
    if angulo_dentro(explorador["angulo"],
                     camada["angulo_saida"],
                     camada["largura_saida"]):
        explorador["camada"] += 1
        explorador["angulo"] += math.pi/ 2
        
def desenhar_camada(camada):
    r = camada["raio"]
    esp = camada["espessura"]
    
    pygame.draw.circle(TELA, (60,60,60), CENTRO, r + esp, esp)
    
    inicio = camada ["angulo_saida"] - camada["largura_saida"] / 2
    fim = camada["angulo_saida"] + camada["largura_saida"] / 2
    
    for a in [inicio, fim]:
        x1 = CENTRO[0] + math.cos(a) * (r)
        y1 = CENTRO[1] + math.sin(a) * (r)
        x2 = CENTRO[0] + math.cos(a) * (r + esp)
        y2 = CENTRO[1] + math.sin(a) * (r + esp)
        pygame.draw.line(TELA, (8,8,8,), (x1, y1), (x2, y2), 4)                        
                                             
def  desenhar_explorador(explorador, camadas):
    if explorador["camada"] >= len(camadas):
        return
    
    camada = camadas[explorador["camada"]]
    r =camada["raio"] + camada["espessura"] // 2
    
    x = CENTRO[0] + math.cos(explorador["angulo"]) * r
    y = CENTRO[1] + math.sin(explorador["angulo"]) * r
    
    pygame.draw.circle(TELA, (0, 220, 180), (int(x), int(y)), 6)
    
#-----------------------loop principal------------------------------
rodando = True
tempo = 0

while rodando:
    clock.tick(FPS)
    tempo += 1
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
            
    TELA.fill((8,8,8))
    
    for camada in camadas:
        camada["angulo_saida"] += camada["vel"]
        desenhar_camada(camada)
        
    atualizar_explorador(explorador, camadas)
    desenhar_explorador(explorador, camadas)
    
    pygame.display.flip()

pygame.quit()                