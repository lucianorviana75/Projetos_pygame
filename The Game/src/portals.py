import pygame
import math
import random

from config import *
from entities import diferenca_angular



def criar_portais():
    portais = []
    for _ in range(NUM_CAMADAS):
        camada = []
        for _ in range(PORTAIS_POR_CAMADA):
            camada.append({
                "angulo": random.uniform(0, 2 * math.pi),
                "aberto": False,
                "timer": random.randint(*DIFFICULTY_SETTINGS[DIFFICULTY]["portal_timer"])
            })
        portais.append(camada)
    return portais


def atualizar_portais(portais):
    for camada in portais:
        for p in camada:
            p["timer"] -= 1
            if p["timer"] <= 0:
                p["aberto"] = not p["aberto"]
                p["timer"] = random.randint(80, 220)


def tentar_portal(ent, direcao, portais):
    nova = ent["camada"] + direcao

    if nova < -1 or nova >= len(portais):
        return False

    for p in portais[ent["camada"]]:
        if p["aberto"] and abs(diferenca_angular(ent["angulo"], p["angulo"])) < 0.25:
            ent["camada"] = nova
            ent["angulo"] += math.pi / 2
            return True

    return False


def desenhar_portais(portais, tela, centro):
    for i in range(NUM_CAMADAS):
        r = RAIO_BASE + i * (ESPESSURA + ESPACO)
        for p in portais[i]:
            cor = PORTAL_ABERTO if p["aberto"] else PORTAL_FECHADO
            for off in (-0.25, 0.25):
                a = p["angulo"] + off
                x1 = centro[0] + math.cos(a) * r
                y1 = centro[1] + math.sin(a) * r
                x2 = centro[0] + math.cos(a) * (r + ESPESSURA)
                y2 = centro[1] + math.sin(a) * (r + ESPESSURA)
                pygame.draw.line(tela, cor, (x1, y1), (x2, y2), 4)