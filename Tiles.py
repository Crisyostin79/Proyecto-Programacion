from turtle import right
import pygame, csv, os

#? Clase Tile 
class Tile(pygame.sprite.Sprite):
    #? Entrada: [imagen] Str, [x e y] int "Coordenada", [HojaSprite] Archivo 
    #? Salida: Un tile   
    #! Funcion: Sacar un tile espcifico.
    def __init__(self, imagen, x, y, HojaSprite):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = HojaSprite.Escoge_Sprite(imagen)
        # Manual load in: self.imagen = pygame.imagen.load(imagen)
        self.rect = self.imagen.get_rect()
        self.rect.x, self.rect.y = x, y

    #? Entrada: [Surface] Superficie pygame
    #! Se encarga de pintar El tile sacado anteriomente
    def draw(self, surface):
        surface.blit(self.imagen, (self.rect.x, self.rect.y))

#? Clase TileMap 
class TileMap():

    #? Entrada: [Nombre_archivo] Archivo csv, [HojaSprite] Archivo .json.
    #? Salida: Superficie Mapa.
    #! Se encarga de iniciar el Mapa y dejarlo listo para venir y pintarlo
    def __init__(self, Nombre_Archivo, HojaSprite):
        self.Dimension_Tile = 16 #* Esta Son las dimensiones del Tile
        self.Inicio_x, self.Inicio_y = 0, 0
        self.HojaSprite = HojaSprite
        self.tiles = self.Cargar_Tile(Nombre_Archivo)
        self.Mapa_Superficie = pygame.Surface((self.Mapa_Ancho, self.Mapa_Alto))
        self.Mapa_Superficie.set_colorkey((0, 0, 0))
        self.Cargar_Mapa()

    #? Entrada: [Superficie] Superficie Pygame.
    #? Salida: Superficie Pintada con el Mapa.
    #! Se encarga principalmente de pintar la Superficie con Los tiles del mapa. 
    def Pinta_mapa(self, Superficie):
        Superficie.blit(self.Mapa_Superficie, (0, 0))

    #? Entrada: [self] self de la clase TileMap en este caso tiles.
    #? Salida: El Mapa dibujado en una superficie.
    #! Se encarga de pintar el mapa leido del Archivo .csv.
    def Cargar_Mapa(self):
        for Tile in self.tiles:
            Tile.draw(self.Mapa_Superficie)

    #? Entrada: [Nombre_archivo] Archivo .json.
    #? Salida: Mapa Arreglo con la informacion del Archivo.
    #! Se encarga Solo de extraer la informacion del archivo y subirla a un arreglo
    #! en blanco.
    def Leer_CSV(self, Nombre_Archivo):
        Mapa = []
        with open(os.path.join(Nombre_Archivo)) as datos:
            datos = csv.reader(datos, delimiter=',')
            
            for Fila in datos:
                Mapa.append(list(Fila))
        
        return Mapa

    #? Entrada: [Nombre_Archivo] Archivo.json
    #? Salida: Sale un Arreglo con todos los tiles 
    #! Esta se encargar principalmente de crear un Arreglo con todos los tiles
    #! Cargados ya en formato tipo Sprite
    def Cargar_Tile(self, Nombre_Archivo):
        tiles = []
        Mapa = self.Leer_CSV(Nombre_Archivo)
        x, y = 0, 0
        for Filas in Mapa:
            x = 0
            for tile in Filas:
                if tile == 0:
                        self.Inicio_x, self.Inicio_y = x * self.Dimension_Tile,\
                        y * self.Dimension_Tile, self.HojaSprite
                for i in range(0,267):
                    if tile == f"{i}":
                        tiles.append(Tile(f'T{i}', x * self.Dimension_Tile,\
                             y * self.Dimension_Tile, self.HojaSprite))
                    

                x += 1
            y += 1
        self.Mapa_Ancho, self.Mapa_Alto = x * self.Dimension_Tile, y * self.Dimension_Tile
        return tiles
