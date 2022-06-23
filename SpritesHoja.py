import pygame
import json


#? Esta es una Clase  la cual se encarga directamente de cargar
#? las imagenes de los tiles
class HojaSprites:
    #? Entrada: [Nombre_Archivo] Nombre del archivo .png y .json.
    #? Salida: [Hoja_Sprite] Imagen.png cargada a formato de Pygame.
    #?         [Datos] Archivo .jsopn cragdo en un arreglo.
    #! Lo que hace es iniciar la clase HojaSprite
    #! Cargando El Nombre del archivo y convertiendo la imagen a fomrato de pygame
    #! y leyendo el archivo .json y subinedolo a un arreglo.
    def __init__(self, NombreArchivo):
        self.NombreArchivo = NombreArchivo
        self.Hoja_Sprites = pygame.image.load(NombreArchivo).convert()
        self.Datos_Archivo = self.NombreArchivo.replace('png', 'json')
        with open(self.Datos_Archivo) as f:
            self.Datos = json.load(f)
        f.close()

    #? Entrada: [x, y, w, h] 
    #? Salida: Superficie con tile.
    #! Se encarga principalmente recortar un sprite en la imagen.png
    #! y lo pega en la superficie.  
    def Recorta_Sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.Hoja_Sprites,(0, 0),(x, y, w, h))
        return sprite

    #? Entrada: [Nombre] str es el nombre del Sprite
    #? Salida: [Imagen] Sprite cortado
    #! Se encarga de buscar Los datos del sprite en el archivo .json 
    #! y luego lo recorta en la imagen y lo devuelve en una superficie
    def Escoge_Sprite(self, Nombre):
        sprite = self.Datos['frames'][Nombre]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.Recorta_Sprite(x, y, w, h)
        return image
        