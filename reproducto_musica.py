import pygame
from pygame.locals import *


# creamos la clase para el reproductor de musica/sonido de pygame
class Musiquero:
    # como atributo de entrada self como autoatributo 
    def __init__(self):
        super().__init__()
        self.volume = 0.025  # configuracion de volumen
 
    # cuando se llame el reproductor de musica en el programa principal,
    # entraran 3 variables, music como el archivo a reproducir, num como
    # la cantidad de veces que se reproducira la cancion y vol como volumen para la pista
    def playsoundtrack(self, music, num, vol):
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(num)
 
    # lo mismo para cuando se ejecute un sonido y no una musica/cancion 
    # pero ahora solo entrara la pista a reproducir y el volumen
    def playsound(self, sound, vol):
        sound.set_volume(vol)
        sound.play()
    
    #entrada su autoatributo para poder detener el reproductor
    def stop(self):
        pygame.mixer.music.stop()