import pygame
import math
import random

from config import *
from entities import *
from portals import *
from core import desenhar_cubo

pygame.init()

# =========================
# TELA
# =========================
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("NÚCLEO")

CENTRO = (LARGURA // 2, ALTURA // 2)
clock = pygame.time.Clock()
FONTE = pygame.font.SysFont("consolas", 22)

# =========================
# FUNÇÕES DE APOIO
# =========================
def raio_camada(c):
    return RAIO_BASE + c * (ESPESSURA + ESPACO) + ESPESSURA // 2

def desenhar_bolinha(ent, cor):
    if ent["camada"] < 0:
        pygame.draw.circle(TELA, cor, CENTRO, 10)
        return
    r = raio_camada(ent["camada"])
    x = CENTRO[0] + math.cos(ent["angulo"]) * r
    y = CENTRO[1] + math.sin(ent["angulo"]) * r
    pygame.draw.circle(TELA, cor, (int(x), int(y)), 8)

def texto(txt, y):
    TELA.blit(FONTE.render(txt, True, TEXTO), (20, y))

# =========================
# INICIAR JOGO
# =========================
def novo_jogo():
    azul = {"angulo": 0.0, "camada": NUM_CAMADAS - 1}

    vermelhos = [
        {
            "angulo": random.uniform(0, 2 * math.pi),
            "camada": 0,
            "offset": 0.0,
            "role": "hunter"
        },
        {
            "angulo": random.uniform(0, 2 * math.pi),
            "camada": 0,
            "offset": random.choice([-1.0, 1.0]),
            "role": "flanker"
        },
        {
            "angulo": random.uniform(0, 2 * math.pi),
            "camada": 0,
            "offset": random.uniform(-0.7, 0.7),
            "role": "blocker"
        },
        {
            "angulo": random.uniform(0, 2 * math.pi),
            "camada": 0,
            "offset": random.uniform(-0.5, 0.5),
            "role": "persecutor"
        }
    ]

    portais = criar_portais()
    tempo = DIFFICULTY_SETTINGS[DIFFICULTY]["time_total"]
    estado = "rodando"
    ang_cubo = 0.0

    return azul, vermelhos, portais, tempo, estado, ang_cubo

# ✅ INICIALIZAÇÃO
azul, vermelhos, portais, tempo, estado, ang_cubo = novo_jogo()

# =========================
# LOOP PRINCIPAL
# =========================
rodando = True
while rodando:
    # ⏱️ cria dt PRIMEIRO
    dt = clock.tick(FPS) / 1000

    ang_cubo += 0.01
    TELA.fill(FUNDO)

    # EVENTOS
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False

        if e.type == pygame.KEYDOWN:
        # ❌ sair do jogo
            if e.key == pygame.K_ESCAPE:
                rodando = False

            # 🔄 reiniciar jogo (apenas se acabou)
            elif e.key == pygame.K_r and estado in ("derrota", "vitoria"):
                azul, vermelhos, portais, tempo, estado, ang_cubo = novo_jogo()

   

    # ================= LOGICA =================
    if estado == "rodando":
        tempo -= dt
        if tempo <= 0:
            estado = "derrota"

        # 🔵 AZUL
        mover_azul(azul, vermelhos)

        # tenta ENTRAR no núcleo
        if tentar_portal(azul, -1, portais) and azul["camada"] < 0:
            estado = "vitoria"

        # 🔴 VERMELHOS (SEMPRE SE MOVEM)
        for v in vermelhos:

            # movimento angular SEMPRE
            mover_vermelhos([v], azul)

            # alinhar pista com o azul
            if v["camada"] < azul["camada"]:
                tentar_portal(v, +1, portais)
            elif v["camada"] > azul["camada"]:
                tentar_portal(v, -1, portais)

            # 💀 CAPTURA
            if v["camada"] == azul["camada"]:
                if abs(
                    diferenca_angular(v["angulo"], azul["angulo"])
                ) < DIFFICULTY_SETTINGS[DIFFICULTY]["capture_dist"]:
                    estado = "derrota"
                    break

        atualizar_portais(portais)

    elif estado == "vitoria":
        azul["angulo"] += 0.05  # efeito visual

    # ================= DESENHO =================
    for i in range(NUM_CAMADAS):
        r = RAIO_BASE + i * (ESPESSURA + ESPACO)
        pygame.draw.circle(TELA, CINZA, CENTRO, r + ESPESSURA, ESPESSURA)

    desenhar_portais(portais, TELA, CENTRO)
    desenhar_cubo(TELA, CENTRO, ang_cubo)

    desenhar_bolinha(azul, AZUL)
    for v in vermelhos:
        desenhar_bolinha(v, VERMELHO)

    texto(f"Tempo: {int(tempo)}", 20)

    if estado == "derrota":
        texto("CAPTURADO!  R para reiniciar", 55)
    if estado == "vitoria":
        texto("CHEGOU AO NÚCLEO!", 55)

    pygame.display.flip()

pygame.quit()