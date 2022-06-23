import pygame
from pygame.locals import *
import os


ALTO = 640
ANCHO = 928
display = pygame.display.set_mode((ANCHO, ALTO))


# clase menu_cositas con variable Sprite para objeto visible simple de pygame
class Menu_Cositas(pygame.sprite.Sprite):
      # entrada: mc(menu cositas) como self variable para si misma
      def __init__(mc):
            # cargamos las imagenes de menu
            mc.image = [pygame.image.load(os.path.join('imagenes_menu', 'bottomground.png')), pygame.image.load(os.path.join('imagenes_menu', 'attackicon.png')),
                        pygame.image.load(os.path.join('imagenes_menu', 'dashicon.png')), pygame.image.load(os.path.join('imagenes_menu', 'specialaicon.png')),
                        pygame.image.load(os.path.join('imagenes_menu', 'click_i.png')),  pygame.image.load(os.path.join('imagenes_menu', 'shiftbutton.png')),
                        pygame.image.load(os.path.join('imagenes_menu', 'pausita.png')),pygame.image.load(os.path.join('imagenes_menu', 'tecla_e.png'))]
      # entrada: mc como autoatributo
      def render(mc):
        #display.blit(mc.image[0],(0, 620)) # menu inferior
        display.blit(mc.image[1],(37, 580)) # icon de ataque
        display.blit(mc.image[2],(100, 580)) # icono de dash
        display.blit(mc.image[3],(160, 580)) # icono de ataque especial
    
        display.blit(mc.image[4],(45, 620)) # icono click izq
        display.blit(mc.image[5],(110, 620)) # icono shift
        display.blit(mc.image[7],(165, 620)) # icono e
        #display.blit(mc.image[6],(800, 605)) # icono pausa
        