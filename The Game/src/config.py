# config.py


LARGURA, ALTURA = 800, 800
FPS = 60

NUM_CAMADAS = 5
PORTAIS_POR_CAMADA = 3
INIMIGOS = 5

RAIO_BASE = 120
ESPESSURA = 30
ESPACO = 20

VEL_AZUL = 0.018
VEL_VERMELHO = 0.014

#tempo = DIFFICULTY_SETTINGS[DIFFICULTY]["time_total"]

#TEMPO_MAX = 50

# CORES
AZUL = (0, 180, 255)
VERMELHO = (220, 60, 60)
CINZA = (45, 45, 45)
FUNDO = (10, 10, 10)

PORTAL_ABERTO = (0, 220, 255)
PORTAL_FECHADO = (90, 90, 90)

TEXTO = (220, 220, 220)

# ========================
# DIFICULDADE DO JOGO
# ========================

EASY = "easy"
NORMAL = "normal"
HARD = "hard"

# ESCOLHA A DIFICULDADE AQUI
DIFFICULTY = HARD  #Para  trcar e ´so mudar esta linha para EASY, NORMAL ou HARD

DIFFICULTY_SETTINGS = {
    EASY: {
        "vel_vermelho": 0.010,
        "capture_dist": 0.12,
        "portal_timer": (120, 260),
        "time_total": 70
    },
    NORMAL: {
        "vel_vermelho": 0.014,
        "capture_dist": 0.15,
        "portal_timer": (80, 220),
        "time_total": 50
    },
    HARD: {
        "vel_vermelho": 0.025,
        "capture_dist": 0.26,
        "portal_timer": (40, 140),
        "time_total": 35
    }
}