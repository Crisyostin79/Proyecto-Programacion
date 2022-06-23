import pygame
from pygame.locals import *
import os

ALTO = 643
ANCHO = 928
display = pygame.display.set_mode((ANCHO, ALTO))


# clase hp con variable Sprite para objeto visible simple de pygame
class HP(pygame.sprite.Sprite):
      # entrada: hb(healthbar) como cambio de nombre para self de las variables de la clase
      def __init__(hb):
            hb.image = pygame.image.load(os.path.join('health', '5.png'))
            
      # entrada: hb(healthbar) como su autoatributo
      def render(hb):
            display.blit(hb.image, (2,4))
            