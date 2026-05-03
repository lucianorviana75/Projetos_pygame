import math
import random
from config import *

def diferenca_angular(a, b):
    return (b - a + math.pi) % (2 * math.pi) - math.pi

def criar_azul():
    return {"angulo": 0.0, "camada": NUM_CAMADAS - 1}

def criar_vermelhos():
    return [
        {"angulo": random.uniform(0, 2 * math.pi), "camada": 0}
        for _ in range(INIMIGOS)
    ]

def mover_azul(azul, vermelhos):
    azul["angulo"] += VEL_AZUL

    # foge dos vermelhos
    for v in vermelhos:
        if v["camada"] == azul["camada"]:
            d = diferenca_angular(azul["angulo"], v["angulo"])
            if abs(d) < 0.4:
                azul["angulo"] += 0.03 * (-1 if d > 0 else 1)

def mover_vermelhos(vermelhos, azul):
    vel = DIFFICULTY_SETTINGS[DIFFICULTY]["vel_vermelho"]

    for v in vermelhos:
        # --- passo 1: direção REAL para o azul ---
        d_real = diferenca_angular(v["angulo"], azul["angulo"])

        # --- passo 2: alvo com personalidade ---
        if v.get("role") == "flanker":
            alvo = azul["angulo"] + v.get("offset", 0.0)
        elif v.get("role") == "blocker":
            alvo = azul["angulo"] + VEL_AZUL * 20
        else:  # hunter ou default
            alvo = azul["angulo"]

        d_behavior = diferenca_angular(v["angulo"], alvo)

        # --- passo 3: REGRA DE OURO ---
        # se o comportamento causar afastamento, ignora
        if abs(d_behavior) > abs(d_real):
            d = d_real
        else:
            d = d_behavior

        # --- passo 4: mover SEMPRE na direção do azul ---
        v["angulo"] += vel * (1 if d > 0 else -1)