import pygame
import math
from config import *

# ========================================
# NÚCLEO - CUBO VISUAL
# ========================================

def desenhar_cubo(tela, centro, ang):
    tamanho = 40
    dist = 200

    pontos = [
        (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
        (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
    ]

    projetados = []

    for x, y, z in pontos:
        xz = x * math.cos(ang) - z * math.sin(ang)
        zz = x * math.sin(ang) + z * math.cos(ang)

        yz = y * math.cos(ang) - zz * math.sin(ang)
        zz = y * math.sin(ang) + zz * math.cos(ang)

        escala = dist / (dist + zz * tamanho)
        px = centro[0] + xz * tamanho * escala
        py = centro[1] + yz * tamanho * escala

        projetados.append((px, py))

    arestas = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    for a, b in arestas:
        pygame.draw.line(
            tela,
            PORTAL_ABERTO,
            projetados[a],
            projetados[b],
            2
        )