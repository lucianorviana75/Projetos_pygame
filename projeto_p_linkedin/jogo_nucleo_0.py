import pygame
import math
import random

pygame.init()

#----------------JANELA---------------------------
LARGURA, ALTURA = 800,800
TELA = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Jogo o Nucleo")

CENTRO = (LARGURA // 2,ALTURA // 2)
FPS = 60
clock = pygame.time.Clock()

FONTE = pygame.font.SysFont("consolas", 24)

#--------------CONSTANTES-------------------------
VEL_EXPLORADOR = 0.015
VEL_INIMIGO = 0.010

NUM_CAMADAS = 6
RAIO_INICIAL = 90
ESPESSURA = 25
ESPACO = 15

#---------------FUNÇÕES MATEMÁTICAS E AUXILIARES---------------------------
#F00
def angulo_dentro(a, inicio, largura):
    dif = ( a - inicio + math.pi) %  (2 * math.pi) - math.pi
    return abs(dif) < largura / 2
#FO1
def diferenca_angular(a, b):
    return (b - a + math.pi) % (2 * math.pi) - math.pi

#F02
def colidiu(a, b):
    return (
        a["camada"] == b["camada"]
        and abs(diferenca_angular(a["angulo"], b["angulo"])) < 0.12
    )
#F03
def tentar_mudar_camada(entidade, camadas, direcao):
    camada = entidade["camada"]

    if camada < 0 or camada >= len(camadas):
        return

    c = camadas[camada]

    if angulo_dentro(entidade["angulo"], c["angulo_saida"], c["largura_saida"]):
        entidade["camada"] += direcao
        entidade["angulo"] += math.pi / 2

#----------------CRIAÇÃO DE ENTIDADES---------------------------------------------------        
#F01
def criar_camadas():
    camadas = []
    for i in range(NUM_CAMADAS):
        camadas.append({
            "raio": RAIO_INICIAL + i * (ESPESSURA + ESPACO),
            "espessura": ESPESSURA,
            "angulo_saida": random.uniform(0, 2 * math.pi),
            "largura_saida": math.pi / 6,
            "vel": random.choice([-1, 1]) * random.uniform(0.002, 0.01)
        })
    return camadas
#F02
def criar_explorador():
    return {
        "angulo": 0.0,
        "camada": NUM_CAMADAS - 1  # começa fora
    }

#F03
def criar_inimigo():
    return {
        "angulo": math.pi,
        "camada": 0  # núcleo
    }
    
#--------------------LÓGICA DE MOVIMENTO----------------------------------    
#F01
def atualizar_explorador(exp, camadas):

    # gira sempre
    exp["angulo"] += VEL_EXPLORADOR

    # proteção
    if exp["camada"] >= len(camadas):
        return

    # pega camada atual
    camada_atual = camadas[exp["camada"]]

    # verifica saída
    if angulo_dentro(
        exp["angulo"],
        camada_atual["angulo_saida"],
        camada_atual["largura_saida"]
    ):
        if exp["camada"] > 0:
            exp["camada"] -= 1
            exp["angulo"] += math.pi / 2

#F05        
def atualizar_inimigo(inim, exp, camadas):
    dif = diferenca_angular(inim["angulo"], exp["angulo"])
    inim["angulo"] += VEL_INIMIGO * (1 if dif > 0 else -1)

    if inim["camada"] < exp["camada"]:
        tentar_mudar_camada(inim, camadas, direcao=+1)

    # só sobe camada pela saída
    if inim["camada"] < exp["camada"]:
        tentar_mudar_camada(inim, camadas, direcao=+1)

#-----------------DESENHO-------------------------------------

#F01
def desenhar_camada(camada):
    r = camada["raio"]
    esp = camada["espessura"]
    #pygame.draw.circle(TELA, (40, 40, 40), CENTRO, r + esp, esp)
    pygame.draw.circle(TELA, (40, 40, 40), CENTRO, r + esp, esp)
    
   

    # destaque da saída
    cor_saida = (0, 180, 255)  # azul ciano
    
    inicio = camada["angulo_saida"] - camada['largura_saida'] / 2
    fim = camada["angulo_saida"] + camada["largura_saida"] / 2
    
    for a in [inicio, fim]:
        x1 = CENTRO[0] + math.cos(a) * r
        y1 = CENTRO[1] + math.sin(a) * r
        x2 = CENTRO[0] + math.cos(a) * (r + esp)
        y2 = CENTRO[1] + math.sin(a) * (r + esp)
        pygame.draw.line(TELA, cor_saida, (x1, y1), (x2, y2), 5)
        
        
#F08        
def desenhar_bolinha(entidade, cor, camadas):
    camada_idx = int(entidade["camada"])

    if camada_idx < 0:
        r = RAIO_INICIAL // 2
    elif camada_idx >= len(camadas):
        r = RAIO_INICIAL + NUM_CAMADAS * (ESPESSURA + ESPACO)
    else:
        camada = camadas[camada_idx]
        r = camada["raio"] + camada["espessura"] // 2

    x = CENTRO[0] + math.cos(entidade["angulo"]) * r
    y = CENTRO[1] + math.sin(entidade["angulo"]) * r
    pygame.draw.circle(TELA, cor, (int(x), int(y)), 6)

#F09
def mensagem(texto):
    render = FONTE.render(texto, True, (200, 200, 200))
    rect =render.get_rect(center=(LARGURA // 2, ALTURA // 2))
    TELA.blit(render, rect) 


#--------------------LOOP DO JOGO------------------------------------       
#Fj00
def jogo():
    camadas = criar_camadas()
    explorador = criar_explorador()
    inimigo = criar_inimigo()
    
    
    estado = "rodando"
    
   
    
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
                    
                if evento.key == pygame.K_r and estado != "rodando":
                    return True # reinicia
                
                
        TELA.fill((8, 8, 8))
        
        for camada in camadas:
            camada["angulo_saida"] += camada["vel"]
            desenhar_camada(camada)
            
                                    
        if estado == "rodando":
            atualizar_explorador(explorador, camadas)
            atualizar_inimigo(inimigo, explorador, camadas)

            if colidiu(explorador, inimigo):
                estado = "derrota"
                
            if explorador["camada"] < 0:
                estado = "vitoria"
                
        desenhar_bolinha(explorador, (0, 220, 180), camadas)
        desenhar_bolinha(inimigo, (220, 50, 50), camadas)
        
        if estado == "derrota":
            mensagem("CAPTURADO! Pressione R para recomeçar")
                                   
        if estado == "vitoria":
            mensagem("ESCAPOU DO NÚCLEO! Pressione R ")
            
        pygame.display.flip()
        
rodando = True
while rodando:
    rodando = jogo()

pygame.quit()
            
       
            


#---------------------LOOP GERAL-------------------
#while True:
 #   jogo()


