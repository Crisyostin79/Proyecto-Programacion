"""
Para este juego estamos usando:
Pygame 2.1.2
Python 3.8.10


Github = https://github.com/Crisyostin79/Proyecto-Programacion
"""

import pygame
from pygame.locals import *
import random

# importamos la clase desde otro archivo
from modulo_vida import HP
from modulo_menu import Menu_Cositas
from reproducto_musica import Musiquero
# Librerias que ya hemos usado anteriormente

from Tiles import *
from SpritesHoja import HojaSprites
from MenusInternos import MenuOpciones

# Nuevas Librerias 

import os 
# OS para un manejo mas facil de carpetas y archivos dentro del programa, sobretodo para facilitar la carga de imagenes

import sys
# solo para sys.exit cuando se cierra pygame

# tkinter para creacion de ventanas 
from tkinter import filedialog
from tkinter import *

# freq, size, channel, buffsize
pygame.mixer.pre_init(44100, 16, 2, 512)
pygame.init()  
# Inicializacion de Pygame

# Music and Sound
soundtrack = ['mainmusic.wav']
		
pygame.mixer.music.load('mainmusic.wav')




#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# Carga conjunto de imagenes para animacion de estar parada hacia la derecha
# usando el join de carpetas de os tomando como primer valor las subcarpetas y como 2do valor el archivo como tal
Idle_Derecha = [pygame.image.load(os.path.join('player/idle', '1.png')), pygame.image.load(os.path.join('player/idle', '2.png')),
                pygame.image.load(os.path.join('player/idle', '3.png')), pygame.image.load(os.path.join('player/idle', '4.png')),
                pygame.image.load(os.path.join('player/idle', '5.png')), pygame.image.load(os.path.join('player/idle', '6.png'))]

# Al conjunto de imagenes de Idle hacia la derecha, se le aplica un flip horizontal con la herramienta de pygame.transform.flip 
# para crear el conjunto de imagenes de Idle hacia la Izquierda  (Siendo el primer valor True de flip horizontal, y el segundo
# falso para que no haga flip vertical)
Idle_Izquierda = [pygame.transform.flip(Idle_Derecha[0],True, False), pygame.transform.flip(Idle_Derecha[1],True, False),
                  pygame.transform.flip(Idle_Derecha[2],True, False), pygame.transform.flip(Idle_Derecha[3],True, False), 
                  pygame.transform.flip(Idle_Derecha[4],True, False), pygame.transform.flip(Idle_Derecha[5],True, False)]

# Carga conjunto de imagenes para correr hacia la derecha
Run_Derecha = [pygame.image.load(os.path.join('player/run', '8.png')), pygame.image.load(os.path.join('player/run', '9.png')),
               pygame.image.load(os.path.join('player/run', '10.png')),pygame.image.load(os.path.join('player/run', '11.png')),
               pygame.image.load(os.path.join('player/run', '12.png')),pygame.image.load(os.path.join('player/run', '13.png')),
               pygame.image.load(os.path.join('player/run', '14.png')),pygame.image.load(os.path.join('player/run', '15.png'))]
 
# Al conjunto de imagenes correr hacia la derecha, se le aplica un flip horizontal con la herramienta de pygame 
# para crear el conjunto de imagenes de correr hacia la Izquierda  (Siendo el primer valor True de flip horizontal, y el segundo
# falso para que no haga flip vertical)
Run_Izquierda = [pygame.transform.flip(Run_Derecha[0],True,False), pygame.transform.flip(Run_Derecha[1],True,False),
                  pygame.transform.flip(Run_Derecha[2],True,False),pygame.transform.flip(Run_Derecha[3],True,False),
                  pygame.transform.flip(Run_Derecha[4],True,False),pygame.transform.flip(Run_Derecha[5],True,False),
                  pygame.transform.flip(Run_Derecha[6],True,False),pygame.transform.flip(Run_Derecha[7],True,False)]

# Carga conjunto de imagenes para animacion de ataque hacia la derecha
Ataque_Derecha = [pygame.image.load(os.path.join('player/atque', '0.png')), pygame.image.load(os.path.join('player/atque', '1.png')),
                  pygame.image.load(os.path.join('player/atque', '2.png')), pygame.image.load(os.path.join('player/atque', '3.png')),
                  pygame.image.load(os.path.join('player/atque', '4.png')), pygame.image.load(os.path.join('player/atque', '5.png')),
                  pygame.image.load(os.path.join('player/atque', '6.png')), pygame.image.load(os.path.join('player/atque', '7.png')),
                  pygame.image.load(os.path.join('player/atque', '8.png')), pygame.image.load(os.path.join('player/atque', '9.png')),
                  pygame.image.load(os.path.join('player/atque', '10.png')), pygame.image.load(os.path.join('player/atque', '11.png')),
                  pygame.image.load(os.path.join('player/atque', '12.png')), pygame.image.load(os.path.join('player/atque', '13.png'))]
 
# Al conjunto de imagenes para el ataque hacia la derecha, se le aplica un flip horizontal con la herramienta de pygame 
# para crear el conjunto de imagenes de ataque hacia la Izquierda  (Siendo el primer valor True de flip horizontal, y el segundo
# falso para que no haga flip vertical)
Ataque_Izquierda = [pygame.transform.flip(Ataque_Derecha[0],True,False), pygame.transform.flip(Ataque_Derecha[1],True,False),
                    pygame.transform.flip(Ataque_Derecha[2],True,False), pygame.transform.flip(Ataque_Derecha[3],True,False),
                    pygame.transform.flip(Ataque_Derecha[4],True,False), pygame.transform.flip(Ataque_Derecha[5],True,False),
                    pygame.transform.flip(Ataque_Derecha[6],True,False), pygame.transform.flip(Ataque_Derecha[7],True,False),
                    pygame.transform.flip(Ataque_Derecha[8],True,False), pygame.transform.flip(Ataque_Derecha[9],True,False),
                    pygame.transform.flip(Ataque_Derecha[10],True,False), pygame.transform.flip(Ataque_Derecha[11],True,False),
                    pygame.transform.flip(Ataque_Derecha[12],True,False), pygame.transform.flip(Ataque_Derecha[13],True,False)]

# Carga conjunto de imagenes para animacion de salto hacia la derecha
Salto_Derecha = [pygame.image.load(os.path.join('player/jump', '1.png')), pygame.image.load(os.path.join('player/jump', '2.png')),
                pygame.image.load(os.path.join('player/jump', '3.png')), pygame.image.load(os.path.join('player/jump', '3.png')),
                pygame.image.load(os.path.join('player/jump', '3.png')), pygame.image.load(os.path.join('player/jump', '3.png')),
                pygame.image.load(os.path.join('player/jump', '4.png')), pygame.image.load(os.path.join('player/jump', '5.png')),
                pygame.image.load(os.path.join('player/jump', '6.png')), pygame.image.load(os.path.join('player/jump', '6.png')),
                pygame.image.load(os.path.join('player/jump', '6.png')), pygame.image.load(os.path.join('player/jump', '6.png')),
                pygame.image.load(os.path.join('player/jump', '6.png'))]


Salto_Izquierda = [pygame.transform.flip(Salto_Derecha[0],True,False), pygame.transform.flip(Salto_Derecha[1],True,False),
                   pygame.transform.flip(Salto_Derecha[2],True,False), pygame.transform.flip(Salto_Derecha[3],True,False),
                   pygame.transform.flip(Salto_Derecha[4],True,False), pygame.transform.flip(Salto_Derecha[5],True,False),
                   pygame.transform.flip(Salto_Derecha[6],True,False), pygame.transform.flip(Salto_Derecha[7],True,False),
                   pygame.transform.flip(Salto_Derecha[8],True,False), pygame.transform.flip(Salto_Derecha[9],True,False),
                   pygame.transform.flip(Salto_Derecha[10],True,False), pygame.transform.flip(Salto_Derecha[11],True,False),
                   pygame.transform.flip(Salto_Derecha[12],True,False)]


Crouch_Derecha = [pygame.image.load(os.path.join('player/crouch', '1.png')), pygame.image.load(os.path.join('player/crouch', '2.png')),
                  pygame.image.load(os.path.join('player/crouch', '3.png')), pygame.image.load(os.path.join('player/crouch', '4.png')), 
                  pygame.image.load(os.path.join('player/crouch', '5.png')), pygame.image.load(os.path.join('player/crouch', '6.png'))]


Crouch_Izquierda = [pygame.transform.flip(Crouch_Derecha[0],True,False), pygame.transform.flip(Crouch_Derecha[1],True,False),
                    pygame.transform.flip(Crouch_Derecha[2],True,False), pygame.transform.flip(Crouch_Derecha[3],True,False),
                    pygame.transform.flip(Crouch_Derecha[4],True,False), pygame.transform.flip(Crouch_Derecha[5],True,False)]


Barra_HP = [pygame.image.load(os.path.join('health', '1.png')), pygame.image.load(os.path.join('health', '0.png')),
             pygame.image.load(os.path.join('health', '2.png')), pygame.image.load(os.path.join('health', '3.png')), 
             pygame.image.load(os.path.join('health', '4.png')), pygame.image.load(os.path.join('health', '5.png'))]


Death_Derecha = [pygame.image.load(os.path.join('player/muertito', '0.png')),  pygame.image.load(os.path.join('player/muertito', '1.png')),
                  pygame.image.load(os.path.join('player/muertito', '2.png')), pygame.image.load(os.path.join('player/muertito', '3.png')), 
                  pygame.image.load(os.path.join('player/muertito', '4.png')), pygame.image.load(os.path.join('player/muertito', '5.png')),
                  pygame.image.load(os.path.join('player/muertito', '6.png')), pygame.image.load(os.path.join('player/muertito', '7.png')),
                  pygame.image.load(os.path.join('player/muertito', '8.png')), pygame.image.load(os.path.join('player/muertito', '9.png')),
                  pygame.image.load(os.path.join('player/muertito', '10.png'))]


Death_Izquierda = [pygame.transform.flip(Death_Derecha[0],True,False),  pygame.transform.flip(Death_Derecha[1],True,False),
                    pygame.transform.flip(Death_Derecha[2],True,False), pygame.transform.flip(Death_Derecha[3],True,False),
                    pygame.transform.flip(Death_Derecha[4],True,False), pygame.transform.flip(Death_Derecha[5],True,False),
                    pygame.transform.flip(Death_Derecha[6],True,False), pygame.transform.flip(Death_Derecha[7],True,False),
                    pygame.transform.flip(Death_Derecha[8],True,False), pygame.transform.flip(Death_Derecha[9],True,False),
                    pygame.transform.flip(Death_Derecha[10],True,False)]


Hit_Derecha = [pygame.image.load(os.path.join('player/golpe_recibido', '0.png')),pygame.image.load(os.path.join('player/golpe_recibido', '1.png')),
               pygame.image.load(os.path.join('player/golpe_recibido', '2.png')),pygame.image.load(os.path.join('player/golpe_recibido', '3.png')),
               pygame.image.load(os.path.join('player/golpe_recibido', '4.png')),pygame.image.load(os.path.join('player/golpe_recibido', '4.png')),
               pygame.image.load(os.path.join('player/golpe_recibido', '5.png')),pygame.image.load(os.path.join('player/golpe_recibido', '6.png'))]


Hit_Izquierda = [pygame.transform.flip(Hit_Derecha[0],True,False),pygame.transform.flip(Hit_Derecha[1],True,False),
                 pygame.transform.flip(Hit_Derecha[2],True,False),pygame.transform.flip(Hit_Derecha[3],True,False),
                 pygame.transform.flip(Hit_Derecha[4],True,False),pygame.transform.flip(Hit_Derecha[5],True,False),
                 pygame.transform.flip(Hit_Derecha[6],True,False),pygame.transform.flip(Hit_Derecha[7],True,False)]

Dash_Derecha = [pygame.image.load(os.path.join('player/dash', '0.png')), pygame.image.load(os.path.join('player/dash', '1.png')),
                pygame.image.load(os.path.join('player/dash', '1.png')), pygame.image.load(os.path.join('player/dash', '2.png')),
                pygame.image.load(os.path.join('player/dash', '2.png')), pygame.image.load(os.path.join('player/dash', '3.png')),
                pygame.image.load(os.path.join('player/dash', '3.png'))]

Dash_Izquierda = [pygame.transform.flip(Dash_Derecha[0],True,False), pygame.transform.flip(Dash_Derecha[1],True,False),
                  pygame.transform.flip(Dash_Derecha[2],True,False), pygame.transform.flip(Dash_Derecha[3],True,False),
                  pygame.transform.flip(Dash_Derecha[4],True,False), pygame.transform.flip(Dash_Derecha[5],True,False),
                  pygame.transform.flip(Dash_Derecha[6],True,False)]

Especial_Derecha = [pygame.image.load(os.path.join('player/special_attack', '1.png')),pygame.image.load(os.path.join('player/special_attack', '2.png')),
                    pygame.image.load(os.path.join('player/special_attack', '3.png')), pygame.image.load(os.path.join('player/special_attack', '4.png')),
                    pygame.image.load(os.path.join('player/special_attack', '5.png')), pygame.image.load(os.path.join('player/special_attack', '6.png')),
                    pygame.image.load(os.path.join('player/special_attack', '7.png')), pygame.image.load(os.path.join('player/special_attack', '8.png')),
                    pygame.image.load(os.path.join('player/special_attack', '9.png')),pygame.image.load(os.path.join('player/special_attack', '10.png'))]

Especial_Izquierda = [pygame.transform.flip(Especial_Derecha[0],True,False),pygame.transform.flip(Especial_Derecha[1],True,False),
                      pygame.transform.flip(Especial_Derecha[2],True,False), pygame.transform.flip(Especial_Derecha[3],True,False),
                      pygame.transform.flip(Especial_Derecha[4],True,False), pygame.transform.flip(Especial_Derecha[5],True,False),
                      pygame.transform.flip(Especial_Derecha[6],True,False), pygame.transform.flip(Especial_Derecha[7],True,False),
                      pygame.transform.flip(Especial_Derecha[8],True,False), pygame.transform.flip(Especial_Derecha[9],True,False)]

cursorsito = pygame.image.load(os.path.join('imagenes_menu', 'cursor.png'))

slime_move_derecha = [pygame.image.load(os.path.join('enemigo_slime', '0.png')), pygame.image.load(os.path.join('enemigo_slime', '1.png')),
                    pygame.image.load(os.path.join('enemigo_slime', '1.png')), pygame.image.load(os.path.join('enemigo_slime', '1.png')),
                    pygame.image.load(os.path.join('enemigo_slime', '2.png')), pygame.image.load(os.path.join('enemigo_slime', '2.png')),
                    pygame.image.load(os.path.join('enemigo_slime', '2.png')), pygame.image.load(os.path.join('enemigo_slime', '3.png'))]

slime_move_izquierda = [pygame.transform.flip(slime_move_derecha[0],True,False), pygame.transform.flip(slime_move_derecha[1],True,False),
                        pygame.transform.flip(slime_move_derecha[2],True,False), pygame.transform.flip(slime_move_derecha[3],True,False),
                        pygame.transform.flip(slime_move_derecha[4],True,False), pygame.transform.flip(slime_move_derecha[5],True,False),
                        pygame.transform.flip(slime_move_derecha[7],True,False), pygame.transform.flip(slime_move_derecha[7],True,False)]

slime_derrota_derecha = [pygame.image.load(os.path.join('enemigo_slime', 'd0.png')), pygame.image.load(os.path.join('enemigo_slime', 'd1.png')),
                        pygame.image.load(os.path.join('enemigo_slime', 'd1.png')), pygame.image.load(os.path.join('enemigo_slime', 'd1.png')),
                        pygame.image.load(os.path.join('enemigo_slime', 'd2.png')), pygame.image.load(os.path.join('enemigo_slime', 'd2.png')),
                        pygame.image.load(os.path.join('enemigo_slime', 'd2.png')), pygame.image.load(os.path.join('enemigo_slime', 'd3.png'))]

slime_derrota_izquierda = [pygame.transform.flip(slime_derrota_derecha[0],True,False), pygame.transform.flip(slime_derrota_derecha[1],True,False),
                          pygame.transform.flip(slime_derrota_derecha[2],True,False), pygame.transform.flip(slime_derrota_derecha[3],True,False),
                          pygame.transform.flip(slime_derrota_derecha[4],True,False), pygame.transform.flip(slime_derrota_derecha[5],True,False),
                          pygame.transform.flip(slime_derrota_derecha[7],True,False), pygame.transform.flip(slime_derrota_derecha[7],True,False)]

bolt_derecha = [pygame.image.load(os.path.join('player/spell', '0.png')), pygame.image.load(os.path.join('player/spell', '1.png')),
                pygame.image.load(os.path.join('player/spell', '2.png')), pygame.image.load(os.path.join('player/spell', '3.png')),
                pygame.image.load(os.path.join('player/spell', '4.png')), pygame.image.load(os.path.join('player/spell', '5.png')),
                pygame.image.load(os.path.join('player/spell', '6.png')), pygame.image.load(os.path.join('player/spell', '7.png')),
                pygame.image.load(os.path.join('player/spell', '8.png')), pygame.image.load(os.path.join('player/spell', '9.png'))]

bolt_izquierda = [pygame.transform.flip(bolt_derecha[0],True,False), pygame.transform.flip(bolt_derecha[1],True,False),
                 pygame.transform.flip(bolt_derecha[2],True,False), pygame.transform.flip(bolt_derecha[3],True,False),
                 pygame.transform.flip(bolt_derecha[4],True,False), pygame.transform.flip(bolt_derecha[5],True,False),
                 pygame.transform.flip(bolt_derecha[6],True,False), pygame.transform.flip(bolt_derecha[7],True,False),
                 pygame.transform.flip(bolt_derecha[8],True,False), pygame.transform.flip(bolt_derecha[9],True,False)]

bolt_hit_derecha = [pygame.image.load(os.path.join('player/spell', 'hit0.png')), pygame.image.load(os.path.join('player/spell', 'hit1.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit2.png')), pygame.image.load(os.path.join('player/spell', 'hit3.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit4.png')), pygame.image.load(os.path.join('player/spell', 'hit5.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit6.png')), pygame.image.load(os.path.join('player/spell', 'hit7.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit8.png')), pygame.image.load(os.path.join('player/spell', 'hit9.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit10.png')), pygame.image.load(os.path.join('player/spell', 'hit11.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit12.png')), pygame.image.load(os.path.join('player/spell', 'hit13.png')),
                    pygame.image.load(os.path.join('player/spell', 'hit14.png')), pygame.image.load(os.path.join('player/spell', 'hit15.png'))]

mana_imagen = [pygame.image.load(os.path.join('imagenes_menu', 'n5.png')),pygame.image.load(os.path.join('imagenes_menu', 'n4.png')),
                pygame.image.load(os.path.join('imagenes_menu', 'n3.png')),pygame.image.load(os.path.join('imagenes_menu', 'n2.png')),
                pygame.image.load(os.path.join('imagenes_menu', 'n1.png')),pygame.image.load(os.path.join('imagenes_menu', 'n0.png'))]
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


# Declaracion de Variables universales antes del programa
vec = pygame.math.Vector2
ALTO = 640    # alto display
ANCHO = 928    # ancho display

FPS = 60       # frames por segundo
COUNT = 0      # contador
FPS_CLOCK = pygame.time.Clock()
# reloj global de pygame


# Creacion de display, icono y nombre del programa
displaysurface = pygame.display.set_mode((ANCHO, ALTO)) #creamos la ventana haciendo set_mode que toma como valores una tupla
pygame.display.set_caption("Haru_Beta_1") # le damos nombre al display
icon = pygame.image.load('iconito.png') # cargamos el icono del juego
pygame.display.set_icon(icon) # pegamos el icono del juego
pygame.mouse.set_visible(False) # Hacemos invisible el cursos del Mouse

sur_size = (4000, 640) # Creamos una tupla con valores x,y para una superficie
superficie = pygame.Surface(sur_size) 
# creamos una superficie en pygame la que despues pegaremos en el display
SUPx = 0 ; SUPy = 0  # valores iniciales de la superficie que despues podemos usar para desplazarla
desp = 0 # valor extra que se le agrega al desplazamiento para que recorra la superficie

max_slimes = 5
nMx = 0 ; nMy = 0
# creacion de timers independientes para diversos eventos
update_sprites_player = pygame.USEREVENT + 1
update_sprites_attaque = pygame.USEREVENT + 2
hit_cooldown = pygame.USEREVENT + 3
dash_cooldown = pygame.USEREVENT + 5

pygame.time.set_timer(update_sprites_player, 80)
pygame.time.set_timer(update_sprites_attaque, 35)
pygame.time.set_timer(hit_cooldown, 0)
pygame.time.set_timer(dash_cooldown, 0)

# al timer se le da como primer valor el nombre del evento ya que debe reconocer cuando ocurrira
# y como segundo valor un int que es el tiempo que tomara el evento en ms

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# creamos la clase para el fondo (temporal) con atributo pygame.sprite.Sprite
# que es una definicion base y simple para objetos dentro de un juego en pygame
# asignamos atributos propios cambiando self(siendo self una manera de llamar a los atributos
# # dados a una funcion para su uso y modificacion propia ) -> bg
# y creamos la funcion render para pegarlo dentro de la superficie

# Entrada: pygame.sprite.Sprite como base simple de objeto visible para la clase Background
class Background(pygame.sprite.Sprite):
      # funcion init que cumple la funcion de almacenar la mayoria de variables de uso para la clase y sub-funciones
      # Entrada: bg , siendo el mismo un cambio al nombre self que sera el nombre de los atributos de la clase
      def __init__(bg):
            bg.backgroundimage = pygame.image.load(os.path.join('fondito', 'fondo.png'))
            bg.Y = 0
            bg.X = 0
            
      # Entrada: bg siendo ahora este una variable de la clase que usara la funcion
      def render(bg):
            # pegamos el fondo en superficie y no en display
            # al blit tomando como primer valor la imagen , y como segundo una tupla con la posicion donde se pegara
            superficie.blit(bg.backgroundimage, (bg.X, bg.Y)) 

                         

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# tipo clase con base un objeto basico visible para pygame
class Ground(pygame.sprite.Sprite):
    # Entrada: ground como inicializaicion de variables con su nombre
    def __init__(ground):
        super().__init__() # esta linea de codigo se usa para cuando pasamos la clase como variable para
        # la funcion que hereda los datos de esta funcion y los mantenga , lo usamos en este caso para 
        # cuando agrupamos antes del while los conjuntos de sprites para confirmar las colisiones,
        # osea hereda tanto la imagen como el rect de la misma
        ground.image = pygame.image.load(os.path.join('fondito','10_3.png'))
        ground.rect = ground.image.get_rect(center = (1900, 618))
        # creamos el rect del piso usando la herramienta get_rect con valor center que le dice a la funcion
        # donde necesitamos que se centre el rectangulo ya que la imagen del piso es un poco grande
        
    # Entrada: ground con los atributos de la clase para su uso
    def render(ground):
        # pegamos el piso en el que se movera el personaje en superficie
        superficie.blit(ground.image, (ground.rect.x-60, ground.rect.y) )
    
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# creamos la clase altar_tp con atributo sprite de pygame para creacion de objeto visible simple
class altar_tp(pygame.sprite.Sprite):
      # Entrada: altar como nombre de los atributos de la clase
      def __init__(altar):
            super().__init__()
            altar.hide = False  # si queremos que el altar aparezca o desaparezca
            altar.image = pygame.image.load(os.path.join('fondito','lamp.png'))
            altar.rect = altar.image.get_rect(center = (335, 505))
      
      # entrada: altar con las variables de la clase para su uso
      def update(altar):
            if altar.hide == False:
                  # pegamos en la superficie el altar
                  superficie.blit(altar.image, (335, 505))


                  pressed_keys = pygame.key.get_pressed()

                  # confirma colision con el jugador
                  hits_tp = pygame.sprite.spritecollide(altar, Playergroup, False)

                  # si el jugador se encuentra en colision con el altar 
                  # puede apretar la tecla e para activar el altar de teletransporte
                  if pressed_keys[K_f] and hits_tp:
                      handler.stage_handler()



#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# creacion de la clase eventhandler que es una funcion que contiene diversos eventos dentro del juego , el primero siendo
# la creacion de la ventana de teletrasnsporte en stage_handler y la generacion de enemigos cuando se activa el menu de oleadas 
class EventHandler():
      # entrada: self como autoatributos de si mismo
      def __init__(self):
            self.enemy_count = 0
            self.battle = False #stage batalla inicia en falso
            self.enemy_generation = pygame.USEREVENT + 4 #llamada al timer de evneto para generar enemigos
            self.stage_enemies = [3]
            self.stage = 1
            for x in range(1, 21):
                  self.stage_enemies.append(int((x ** 2 / 2) + 1))
                  # adjunta en la lista la cantidad de enemigos que revisara el handler de eventos para
                  # generar en cada nivel de pelea

      # entrada: self como autoatributos de si mismo       
      def stage_handler(self):
            # aqui se genera la ventana para el altar de tp
            self.root = Tk() # iniciamos tkinter
            self.root.title("Warping Altar") #nombre de ventana
            self.root.geometry('200x180+855+450')# le damos tamaño(200x180) y posicion(855+450)
            self.frame = Frame(self.root) #creamos el frame principal de la ventana
            self.frame.pack()
         
            # creamos en el frame principal el primer texto
            # con primer valor el frame principal y 2do el texto a mostrar
            self.label = Label(self.frame, text = "Teletransporte hacia:") #texto superior a los botones
            self.label.pack()
             
            # creamos los botones con tkinter Button, con primer valor root que es el mismo tkinter, el texto a mostrar
            # sus dimensiones wid/hei y la funcion comando que sirve para activar un evento cuando el boton es presionado
            button1 = Button(self.root, text = "Primera Cueva", width = 18, height = 2, command = self.primera_cueva)
            button2 = Button(self.root, text = "Villa Everwinter", width = 18, height = 2, command = self.villa_everwinter)
            button3 = Button(self.root, text = "EX Dungeon", width = 18, height = 2, command = self.ex_dungeon)
            
            # le damos posicion a los botones
            button1.place(x = 30, y = 25)
            button2.place(x = 30, y = 75)
            button3.place(x = 30, y = 125)
            
            # activamos el mainloop para mantener la ventana activa
            self.root.mainloop()
      
      # entrada: self como autoatributos de si mismo
      def next_stage(self):  # cuando se apreta la tecla n ocurre la activacion de oleadas solo cuando el
                             # usuario activo el primer boton de teletransporte    
            self.stage += 1 #aumenta el nivel
            self.enemy_count = 0  #empieza con 0 enemigos
            print("Nivel: "  + str(self.stage)) # muestra en consola el nivel actual
            pygame.time.set_timer(self.enemy_generation, 2500 - (50 * self.stage)) # define el tiempo de spawn entre enemigos
      
      # entrada: self como autoatributos de si mismo      
      def primera_cueva(self): # si se apreta el primer boton...
            self.root.destroy() # cierra la ventana
            pygame.time.set_timer(self.enemy_generation, 2000) # pone un timer a la generacion de enemigo
            altar_tp.hide = True # ocultamos el altar
            self.battle = True # activamos el battle para cuando se presione n se activen las oleadas

      # entrada: self como autoatributo de si mismo
      def villa_everwinter(self): # segundo boton
            self.root.destroy() # cerramos la ventana
            altar_tp.hide = True
            player.pos.x = 1326 
            player.pos.y = 544  
            
      # entrada: self como autoatributo de si mismo
      def ex_dungeon(self):
            self.root.destroy() # cerramos la ventana
            altar_tp.hide = True
            player.pos.x = 3890
            player.pos.y = 512

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
####################################################################################################################### 
# creamos la clase player que contendra todas las variables que como objeto jugador necesita el personaje para moverse
# como posiciones iniciales, velocidades aceleraciones personales entre otros ademas de las funciones que le daran movimiento,
# capacidad de ataque, salto y gravedad entre otras, y como es habitual para las clases o definiciones en general darle el nombre:
# object/self con tal de autoidentificarse en este caso por ser nuetro personaje y tener nombre propio le asignaremos tal como su variable
# personal en este caso haru

# clase player con entrada de Sprite atributo simple de objeto visible para pygame
class Player(pygame.sprite.Sprite):
    # entrada: variable self->haru como nombre de las variables propias para el jugador
    def __init__(haru):
        super().__init__() #heredacion de atributos
        haru.image = pygame.image.load(os.path.join('player/idle', '1.png'))
        # creamos la "hitbox" de la sprite
        haru.rect = haru.image.get_rect()
        # ya que el rectangulo de sprite toma en consideracion el espacio vacio del mismo
        # "desinflamos" en x su ancho/tamaño para que las colisiones de personaje+objeto sean 
        # mas cercanas y tengan coherencia
        haru.rect.inflate_ip(-30,0)

        # uso de vectores con el fin de descomponer la posicion, vel y acc en 2 componentes
        # ej: el vec para pos se descompone en (haru.pos.x) y (haru.pos.y)
        # dandole una posicion x e y al mismo tiempo
        haru.pos = vec(250, 575) # vector Posicion Inicial
        haru.vel = vec(0,0) # Vector Velocidad inicial
        haru.acc = vec(0,0) # Vector Aceleracion inicial
        haru.direction = "RIGHT" # Direccion inicial

        # Movimiento 
        haru.idle = True  # Standy By
        haru.jumping = False  # salto
        haru.double_jump = False # doble salto
        haru.running = False # correr
        haru.crouch = False # agachar
        haru.dash = False 
        haru.njumps = 0 # n de saltos
        
        # Frames del arreglo de imagen correspondiente al tipo de movimiento
        haru.move_frame = 0
        haru.idle_frame = 0
        haru.death_frame = 0
        haru.dash_frame = 0
        haru.salto_frame = 0
        haru.crouch_frame = 0
        haru.desaparecer = 0
        haru.golpeado_frame = 0
        
        # Combate
        haru.death = False
        haru.golpeado = False
        haru.health = 5
        haru.attacking = False
        haru.cooldown = False   # CD de ataque
        haru.dash_cooldown = False # CD dash
        haru.attack_frame = 0
        haru.magic_cooldown = 1
        haru.special_attack = False
        haru.special_frame = 0
        haru.mana = 5
        
    def move(haru):
      # Mantiene una aceleracion constante en direccion hacia abajo  (gravedad)
      # a mayor valor de y menor sera el salto
      haru.acc = vec(0,0.5)
 
      # Volvera el booleano de correr a falso si es que el movimiento decrece hasta cierto punto
      # y viceversa
      if abs(haru.vel.x) > 0.3:
            haru.running = True
      else:
            haru.running = False
            
 
      # llamado de pygame para confirmar uso de teclas
      pressed_keys = pygame.key.get_pressed()
 
      # acelera en la direccion en la que se presiona la tecla
      if pressed_keys[K_a]:
            haru.acc.x = -0.3
            #haru.Coliciones_X(map.tiles)
            # si esta muerto no puede moverse
            if haru.health == 0:
                haru.acc.x = 0
                haru.Coliciones_X(map.tiles)
      if pressed_keys[K_d]:
            haru.acc.x = 0.3
            #haru.Coliciones_X(map.tiles)
            if haru.health == 0:
               haru.acc.x = 0
               haru.Coliciones_X(map.tiles)
      
      if pressed_keys[K_LSHIFT]: 
        haru.running = False
        haru.idle = False
        if haru.dash_cooldown == False: # si el CD es falso  
            haru.dash_cooldown = True # empieza el CD
            pygame.time.set_timer(dash_cooldown, 2000) # convierte el CD en 2 segundos  
            if haru.health != 0:
                
                haru.dash = True
                if haru.direction == "RIGHT":
                    haru.acc.x = 10
                else:
                    haru.acc.x = -10
      
      # calculo de velocidad tomando en cuenta una friccion (-0.10)
      haru.acc.x += haru.vel.x * (-0.10)
      
      haru.vel += haru.acc 
      haru.pos += haru.vel + 0.9 * haru.acc  # actualiza la posicion con nuevos valores
      
      
      # este codigo sirve para mantener el personaje dentro de la pantalla
      # o hacer que se haga teletransporte entre los 2 extremos
      if haru.pos.x > sur_size[0]-32:
            haru.pos.x = sur_size[0]-32 # intercambiable
      if haru.pos.x < 0:
            haru.pos.x = 0
                              # intercambiable
      if haru.pos.y > 640:
         haru.pos.y = 250 
         haru.pos.x = 23
         haru.health = haru.health - 1
         health.image = Barra_HP[haru.health]
         
      
      haru.rect.midbottom = haru.pos  # actualiza el la parte inferior del rectangulo con la nueva posicion
      haru.Coliciones_Y(map.tiles) # actualiza el la parte inferior del rectangulo con la nueva posicion

    # entrada: self->haru como sus autoatributos
    def gravity_check(haru):

      # confirma si el jugador esta colisionando con los sprites del piso
      # grounch_check = pygame.sprite.spritecollide(player ,ground_group, False)
      if haru.vel.y > 0:
          # si hay contacto
          """
          if grounch_check:
              intersec = grounch_check[0] # buscamos el primer grupo de sprites que se intersecta
              if haru.pos.y < intersec.rect.bottom: # si su y es menor a donde ocurre la colision
                  haru.pos.y = intersec.rect.top + 1
                  haru.vel.y = 0
                  haru.salto_frame = 0
                  haru.jumping = False
            """
    # entrada: self->haru como sus autoatributos
    def update(haru):
          # se devuelve al sprite base despues del movimiento
          if haru.move_frame > 7:
                haru.move_frame = 0 
                return

          # se devuelve al sprite base despues del movimiento
          if haru.idle_frame > 5 :
                haru.idle_frame = 0 
                return

          if haru.dash_frame > 6:
              haru.dash = False
              haru.dash_frame = 0
              return

          # se devuelve al sprite base despues del movimiento
          if haru.salto_frame > 12:
              haru.salto_frame = 0 
              return

          # volvemos al frame 1 y no al 0 para mantener el bucle de
          # crouch en movimiento fluido
          if haru.crouch_frame >= 5:
              haru.crouch_frame = 1 
              return
          # si llega al ultimo frame de muerte
          # activa un contador para que desaparezca el cuerpo
          if haru.death_frame >= 10:
              haru.death_frame = 10
              haru.desaparecer += 1
              return
          # vuelve al frame base despues de golpe y desactiva su animacion
          if haru.golpeado_frame >= 6:
              haru.golpeado = False
              haru.golpeado_frame = 0
              if not haru.golpeado and haru.golpeado_frame != 0:
                haru.golpeado = False
                haru.golpeado_frame = 0
            
          if haru.special_frame >= 10:
            haru.special_attack  = False
            haru.special_frame = 0
            return


          pressed_keys = pygame.key.get_pressed()
          
          # si apretamos la tecla s
          if pressed_keys[K_s]:
            # se activa el crouch
            haru.crouch = True
            # si esta muerto no puede hacer crouch
            if haru.health == 0:
                haru.crouch = False
          else:
            # si no esta activa, crouch vuelve a falso y se devuelve al frame 0
            haru.crouch = False
            haru.crouch_frame = 0

          

          
          
          # esto conjunto de if es el que hace simular el movimiento
          # ciclando los frames de cada arreglo de imagenes
          
          
          if haru.jumping == False and haru.running == True:
                if haru.vel.x > 0:
                      haru.image = Run_Derecha[haru.move_frame]
                      haru.direction = "RIGHT"
                else:
                      haru.image = Run_Izquierda[haru.move_frame]
                      haru.direction = "LEFT"
                haru.move_frame += 1

          elif haru.jumping == True and haru.running == True:  
                if haru.vel.x > 0:
                      haru.image = Salto_Derecha[haru.salto_frame]
                      haru.direction = "RIGHT"
                else:
                      haru.image = Salto_Izquierda[haru.salto_frame]
                      haru.direction = "LEFT"
                haru.salto_frame += 1

          elif haru.jumping == True and haru.running == False:  
                if haru.vel.x > 0:
                      haru.image = Salto_Derecha[haru.salto_frame]
                      haru.direction = "RIGHT"
                else:
                      haru.image = Salto_Izquierda[haru.salto_frame]
                      haru.direction = "LEFT"
                haru.salto_frame += 1

          elif haru.crouch:
                haru.golpeado = False
                if haru.direction == "RIGHT":
                      haru.image = Crouch_Derecha[haru.crouch_frame]
                elif haru.direction == "LEFT":
                      haru.image = Crouch_Izquierda[haru.crouch_frame]
                haru.crouch_frame += 1

          elif haru.dash:
              haru.idle = False
              haru.jumping = False
              haru.running = False
              if haru.direction == "RIGHT":
                  haru.image = Dash_Derecha[haru.dash_frame]
              else:
                  haru.image = Dash_Izquierda[haru.dash_frame]
              haru.dash_frame += 1

          elif haru.golpeado:
              if haru.direction == "RIGHT":
                  haru.image = Hit_Derecha[haru.golpeado_frame]
              elif haru.direction == "LEFT":
                  haru.image = Hit_Izquierda[haru.golpeado_frame]
              haru.golpeado_frame += 1

          elif haru.health == 0:
              haru.golpeado = False
              haru.running = False
              haru.jumping = False
              haru.crouch = False
              haru.special_attack = False
              if haru.direction == "RIGHT":
                  haru.image = Death_Derecha[haru.death_frame]
                  haru.death_frame += 1
              else:
                  haru.image = Death_Izquierda[haru.death_frame]
                  haru.death_frame += 1

          elif haru.special_attack:
            if haru.direction == "RIGHT":
                  haru.image = Especial_Derecha[haru.special_frame]
            elif haru.direction == "LEFT":
                  haru.image = Especial_Izquierda[haru.special_frame]
            haru.special_frame += 1

          else:
              if haru.direction == "RIGHT":
                 haru.image = Idle_Derecha[haru.idle_frame]
              elif haru.direction == "LEFT":
                 haru.image = Idle_Izquierda[haru.idle_frame]
              haru.idle_frame += 1
          
          # devuelve el frame base de los sprites idle si hay algun frame que se muestre incorrecto
          # teniendo en cuenta que la velocidad sea menor al minimo requerido para considerar movimiento y se 
          # este mostrando un frame distinto al idle inicial
          if abs(haru.vel.x) < 0.2 and haru.move_frame != 0:
                haru.golpeado = False
                haru.dash = False
                haru.running = False
                haru.move_frame = 0
                if haru.direction == "RIGHT":
                      haru.image = Run_Derecha[haru.move_frame]
                elif haru.direction == "LEFT":
                      haru.image = Run_Izquierda[haru.move_frame]

    # entrada: self->haru como sus autoatributos
    def attack(haru):        
      # Si el frame de ataque llega a su fin se devuelve al inicio    
      if haru.attack_frame > 10:
            haru.attack_frame = 0
            haru.attacking = False
 
      # confirma la direccion para mostrar el frame correcto de ataque
      if haru.direction == "RIGHT":
             haru.image = Ataque_Derecha[haru.attack_frame]

      elif haru.direction == "LEFT":
             haru.correction()
             haru.image = Ataque_Izquierda[haru.attack_frame] 
        
      # actualiza el frame de ataque 
      haru.attack_frame += 1


    def Comprueba_hits(haru, mTiles):
        hits = []
        for tile in mTiles:
            if haru.rect.colliderect(tile):
                hits.append(tile) 
        return hits

    def Coliciones_X(haru, mtiles):
        Coliciones = haru.Comprueba_hits(mtiles)
        for tile in Coliciones:
            if haru.vel.x > 0: # Movimiento derecha 
                haru.vel.x = 0
                haru.pos.x = tile.rect.left- haru.rect.w
                haru.rect.x = haru.pos.x
            elif haru.vel.x < 0: #Movimiento izquierda
                haru.vel.x = 0
                haru.pos.x = tile.rect.right
                haru.rect.x = haru.pos.x 

    def Coliciones_Y(haru, mtiles):        
        haru.on_pasto = False
        haru.rect.bottom += 1
        Coliciones = haru.Comprueba_hits(mtiles)
        for tile in Coliciones:
            if haru.vel.y > 0: # Toque con el suelo 
                haru.on_pasto = True
                haru.jumping = False
                haru.vel.y = 0
                haru.pos.y = tile.rect.top
                haru.rect.bottom = haru.pos.y 
            elif haru.vel.y < 0: # Toque con la cabeza
                haru.vel.y = 0 
                print("Arriba")
                haru.pos.y = tile.rect.bottom + haru.rect.h
                haru.rect.bottom = haru.pos.y








    def correction(haru):

      # esta funcion es usara para corregir un error de frame
      # con la posicion de ataque cuando se dirige a la izquierda
      # ya que al usar el flip de imagen hace que el jugador tenga un pequeno desplazamiento
      if haru.attack_frame == 1:
            haru.pos.x += 10
      if haru.attack_frame == 10:
            haru.pos.x -= 10

    def jump(haru):
        if haru.njumps >= 2:
            print("LLL")
            haru.jumping = False
        haru.rect.x += 1
 
        # confirma si el jugador esta en contacto con el piso
        #hits = pygame.sprite.spritecollide(haru, ground_group, False)
     
        haru.rect.x -= 1
 
        # si toca el piso y no esta saltando, hace que el jugador salte
        if haru.on_pasto and not(haru.jumping):
            haru.double_jump = False
            haru.jumping = True
            haru.vel.y = -10
            haru.njumps = 1
            print("aa")
            #print(haru.jumping, haru.njumps)
            
            # si esta muerto no puede saltar
            if haru.health == 0:
                haru.vel.y = 0

        # si esta en el piso y la velocidad aerea es mayor o igual a 0
        # y el numero de saltos es menor a 2, puede volver a saltar
        elif not haru.on_pasto and haru.njumps < 2:
            haru.double_jump = True
            haru.jumping = True
            haru.njumps += 1
            haru.rect.x += 1
            haru.vel.y = -10
            print("ee")
            #print(haru.jumping, haru.njumps)
            haru.rect.x -=1
            # si esta muerto no puede hacer doble salto
            if haru.health == 0:
                haru.vel.y = 0
        print("JUmping:", haru.jumping, "On pasto:", haru.on_pasto,  haru.njumps)   
            

    # entrada: self->haru como sus autoatributos
    def player_hit(haru):
        if haru.cooldown == False: # si el CD es falso  
            haru.cooldown = True # empieza el CD
            pygame.time.set_timer(hit_cooldown, 1000) # convierte el CD en 1 segundo
        
            haru.health = haru.health - 1
            health.image = Barra_HP[haru.health]
            if haru.health <= 0:
                haru.death = True
                haru.kill()
                pygame.display.update()
                
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################             
class special_attack(pygame.sprite.Sprite):
      def __init__(bolt):
            super().__init__()
            bolt.direction  = player.direction
            if bolt.direction == "RIGHT":
                  bolt.image = bolt_derecha[0]
            else:
                  bolt.image = bolt_izquierda[0]

            bolt.image_hit = bolt_hit_derecha[0]      
            bolt.rect = bolt.image.get_rect(center = player.pos)
            bolt.rect.x = player.pos.x
            bolt.rect.y = player.pos.y -30
            bolt.frame = 0
            bolt.hit_frame = 0
            bolt.hit = False

      def cast(bolt):
        if bolt.frame >= 9:
            bolt.frame = 0
            return
         
        player.magic_cooldown = 0
        holyhits = pygame.sprite.spritecollide(bolt, slimes, False)
        if holyhits :
                bolt.hit = True
        # distancia maxima del proyectil
        if player.pos.x -250 < bolt.rect.x < player.pos.x+250:
            if bolt.direction == "RIGHT":
                  bolt.image = bolt_derecha[bolt.frame]
                  superficie.blit(bolt.image, bolt.rect)
            else:
                  bolt.image = bolt_izquierda[bolt.frame]
                  superficie.blit(bolt.image, bolt.rect)
            bolt.frame += 1           

            # genera el movimiento del proyectil moviendo su rect con la funcion
            # move_ip que significa move in place dandoles valores a la parte x para
            # generar el desplazamiento
            if bolt.direction == "RIGHT":
                  bolt.rect.move_ip(6, 0)
            else:
                  bolt.rect.move_ip(-6, 0)    

        else:
            player.magic_cooldown = 1
            bolt.kill()
            
            
        
      
        

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################  

# creacion de clase slime para el enemigo con atributo sprite de objeto visible para pygame
class Slime(pygame.sprite.Sprite):
    # creacion de las variables "globales" para el slime con atributo self->slime para si mismo
    # entrada: slime como sus autoatributos
    def __init__(slime):
        super().__init__() # heredacion de atributos
        slime.image = pygame.image.load(os.path.join('enemigo_slime', 'base.png'))
            
        slime.rect = slime.image.get_rect() #obtenemos el rect del slime
        slime.mapa_pos = random.randint(0,4)
        if slime.mapa_pos == 0:
            slime.pos = vec(613, 520) # posicion inicial x , y
        elif slime.mapa_pos == 1:
            slime.pos = vec(1300, 520) # posicion inicial x , y
        elif slime.mapa_pos == 2:
            slime.pos = vec(1900, 538) # posicion inicial x , y
        elif slime.mapa_pos == 3:
            slime.pos = vec(2485, 473) # posicion inicial x , y
        elif slime.mapa_pos == 4:
            slime.pos = vec(3000, 538) # posicion inicial x , y

        slime.vel = vec(0,0) # vector velocidad inicial para el enemigo
            
        slime.direction = random.randint(0, 1) # 0 derecha, 1 izquierda
        slime.vel.x = 1  # velocidad para el enemigo
        slime.death = False
        slime.move_frame = 0
        slime.death_frame = 0
            
    # entrada: slime como sus autoatributos
    def move(slime):
        # condiciones para que el enemigo cicle entre x posicion
        if slime.mapa_pos == 0 or slime.mapa_pos == 3:
            slime.direction = 3
            slime.vel.x = 0
            slime.rect.center = slime.pos # actualiza la posicion del rect
        else:
            if slime.pos.x == 1212 or slime.pos.x == 1770 or slime.pos.x == 2765  :
                slime.direction = 0
            if slime.pos.x == 1490 or slime.pos.x == 2110 or slime.pos.x == 3200:
                slime.direction = 1

            # actualiza la posicion con nuevos valores   
            if slime.direction == 0: # si derecha:
                slime.pos.x += slime.vel.x
                        
            if slime.direction == 1:
                slime.pos.x -= slime.vel.x
            
            if slime.direction == 3:
                slime.pos.x = slime.pos.x
                    
        
            slime.rect.center = slime.pos # actualiza la posicion del rect
        

    # entrada: slime como sus autoatributos
    def update(slime):
        if slime.move_frame >= 6:
            slime.move_frame = 0
            return
        if slime.death_frame >= 7:
            slime.death_frame = 7

        if slime.direction == 0:
            slime.image = slime_move_derecha[slime.move_frame]
        else:
            slime.image = slime_move_izquierda[slime.move_frame]
                

        slime.move_frame += 1

        # confirma si hay colision con el jugador partiendo en falso porque no inician chocando
        # sprite collide usa 3 argumentos, el primer es el grupo de sprite propio, el 2do es con el que contacta
        # y tercero es un bool con falso si es que no colisionan y true si hay contacto
        hits_enemy = pygame.sprite.spritecollide(slime, Playergroup, False)

            # Checks for collision with Fireballs
        bolt_hits = pygame.sprite.spritecollide(slime, Holybolts, False)

            # se activa cuando se cumple las 2 condiciones ( colision + jugador atacando )
        if hits_enemy and player.attacking == True or bolt_hits :
            if slime.direction == 0:
                slime.image = slime_derrota_derecha[slime.death_frame]
                slime.death_frame += 1
            else:
                slime.image = slime_derrota_izquierda[slime.death_frame]
                slime.death_frame += 1
            if slime.death_frame == 7 or bolt_hits:
                player.mana += 1
                slime.kill() # cancela todas las variables definidas para nuestro enemigo slime sin 
                # eliminar el sprite en pantalla como tal
                slime.death = True
                print("Enemigo Derrotado")
 
        # si ocurre colision y el jugador no ataca        
        elif hits_enemy and player.attacking == False:
            print("golpe")
            player.player_hit() 
            # cancelamos los frames actuales del jugador para
            player.jumping = False
            player.crouch = False
            player.running = False
            player.idle = False
            player.dash = False
            player.golpeado = True # prioritizar que muestre cuando fue golpeado

    # entrada: slime como sus autoatributos
    def render(slime):
        superficie.blit(slime.image, slime.pos)
        
 


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
HojaSprite = HojaSprites('Texturas.png')
map = TileMap('Mundo Inicial_Terreno.csv', HojaSprite )
map2 = TileMap('Mundo Inicial_Decoraciones.csv', HojaSprite )


player = Player() # iniciamos la clase jugador
Playergroup = pygame.sprite.Group() # creamos el grupo de sprites de jugador
Playergroup.add(player) # anadimos el el jugador y sus sprites al grupo creado anteriormente
# esto es lo que usamos para despues confirmar colisiones


# iniciamos el piso y su grupo de sprites
#ground = Ground()
ground_group = pygame.sprite.Group()
#ground_group.add(ground)

# iniciamos el fondo
background = Background() 

Holybolts = pygame.sprite.Group()

mmanager = Musiquero()

# iniciamos el altar, y su grupo de sprites
altar = altar_tp()
altargroup = pygame.sprite.Group()
altargroup.add(altar)

# iniciamos el manejo de eventos
handler = EventHandler()

# iniciamos el enemigo y su grupo de sprites
slime = Slime()
slimes = pygame.sprite.Group()
slimes.add(slime)

# iniciamos la barra de vida	
health = HP() 
Menucito = Menu_Cositas()
hit_frame = 0

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
def Primer_Nivel(): 
    FPS_CLOCK = pygame.time.Clock()
    FPS = 100
    update_sprites_player = pygame.USEREVENT + 1
    pygame.time.set_timer(update_sprites_player, 80)
    nMx = 0 ; nMy = 0
    SUPx = 0 ; SUPy = 0
    desp = 0
    Cerrar = False
    mmanager.playsoundtrack(soundtrack[0], -1, 0.025)
    # while para el ciclo de juego
    while True:
        
        
        # llamamos la funcion gravedad para el jugador primero
        # esto con el fin de confirmar en cada momento si el jugador esta en constante colision con el piso
        # o a si mismo en el "aire"
        # player.gravity_check() 


        # manejo de eventos de pygame
        for event in pygame.event.get():
            # si el tipo de evento es : 
            if event.type == handler.enemy_generation:
                # si el numero de enemigos actual es menor al numero de enemigos que deberian spawnear en el stage
                if handler.enemy_count < handler.stage_enemies[handler.stage - 1]:
                    # crea un enemigo
                    enemy = Slime()
                    slimes.add(enemy)
                    # lo anade al contador
                    handler.enemy_count += 1 
                    
            # si el tipo de eventos es actualizar los sprites:         
            if event.type == update_sprites_player:
                # actualiza los sprites con USEREVENT y el timer correspondiente
                player.update() 

            # si el tipo de eventos es actualizar los sprites de ataque:      
            if event.type == update_sprites_attaque:
                # actualiza los sprites con USEREVENT y el timer correspondiente si el jugador esta atacando
                if player.attacking == True:
                    player.attack()  

            # si el tipo de evento es CD de golpe
            if event.type == hit_cooldown:
                # pone un temporizador al golpe del jugador con USEREVENT timer de 1 segundo
                player.cooldown = False

            # si el tipo de evento es CD de golpe   
            if event.type == dash_cooldown:
                player.dash_cooldown = False

            

            # cierra pygame y la consola cuando el evento es CERRAR/QUIT
            if event.type == QUIT:
                pygame.quit() # cerramos pygame
                sys.exit() # aqui usamos sys para salir exitosamente del programa
                
            # eventos para cuando se usa el boton izq del raton/mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # primero confirma si el ataque del jugador es falso
                if player.attacking == False:
                        # primero confirma si el jugador esta muerto o no
                        if player.death == True:
                            pass
                        else:
                            # para luego activarlo 
                            player.attacking = True 
                            player.attack()
                        
            if event.type == pygame.MOUSEMOTION : nMx,nMy = event.pos # Coordenada Mouse 
            # manejo de eventos cuando se presionan teclas 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and player.magic_cooldown == 1:
                    if player.mana >= 1:
                        player.mana -= 1
                        player.special_attack = True
                        holybolt = special_attack()
                        Holybolts.add(holybolt)
                # si se presiona la tecla n
                if event.key == pygame.K_n:
                    # si entro en la primera cueva y no hay enemigos
                    if handler.battle == True and len(slimes) == 0:
                        # pasa al sgte stage (crea oleada de slimes)
                        handler.next_stage()

                if event.key == pygame.K_t:
                    Cerrar = MenuOpciones(displaysurface)
                    
                # si se apreta la tecla espacio:
                if event.key == pygame.K_SPACE:
                    player.jump()

            # manejo de eventos cuando se suelta una tecla
            if event.type == pygame.KEYUP:
                pass
        
        
        # funciones de jugador
        player.move() 
        
        
        #funciones update
        

        # funciones de render
        
        #ground.render()  
        
        background.render()
        
        map.Pinta_mapa(superficie)
        map2.Pinta_mapa(superficie)
        # funciones para el enemigo
        # para cada enemigo en el grupo de sprites
        for enemy in slimes:
            enemy.update()
            enemy.move()
            enemy.render()
            
        for bolt in Holybolts:
            bolt.cast()

        
        altar.update() # la funcion update de altar es render/update al mismo tiempo  
        

        slime.render()
        # render de jugador mientras esta vivo 
        if player.desaparecer <= 20:
            superficie.blit(player.image, player.rect)

        

         
        # pegamos toda la superficie en el display
        displaysurface.blit(superficie, (SUPx, SUPy))
        
        
        

        # ya que la hp, el menu y el cursor esta en display la pegamos encima de todo
        Menucito.render()
        if player.mana == 5:
            displaysurface.blit(mana_imagen[0],(190, 580))
        elif player.mana == 4:
            displaysurface.blit(mana_imagen[1],(190, 580))
        elif player.mana == 3:
            displaysurface.blit(mana_imagen[2],(190, 580))
        elif player.mana == 2:
            displaysurface.blit(mana_imagen[3],(190, 580))
        elif player.mana == 1:
            displaysurface.blit(mana_imagen[4],(190, 580))
        elif player.mana == 0:
            displaysurface.blit(mana_imagen[5],(190, 580)) 
        health.render()
        displaysurface.blit(cursorsito, (nMx, nMy))

        # desplazamiento de la superficie:
        # si el jugador se encuentra en:
        if player.pos.x < 3900:
            if player.pos.x > 750+desp:
                # se aplica desplazamiento en direccion:
                SUPx -= 1.5
                desp += 1.5
                # si el jugador esta mas alla del primer limite:
                if player.pos.x > 850+desp:
                    # se duplica el desplazamiento de superficie
                    SUPx -= 3
                    desp += 3
            # si el jugador se encuentra en:
            elif player.pos.x < 150+desp and SUPx<0:
                # se aplica desplazamiento en direccion:
                SUPx += 1.5
                desp -= 1.5
                # si el jugador esta mas alla del primer limite:
                if player.pos.x < 50+desp:
                    # se duplica el desplazamiento de superficie
                    SUPx += 3
                    desp -= 3
        
        if Cerrar == True:
            return
        pygame.display.update() 
        FPS_CLOCK.tick(FPS)

