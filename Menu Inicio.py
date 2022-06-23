import pygame as pg
from pygame.locals import *
import os
from JuegoFinal import Primer_Nivel

# Constantes
#===================================================================
nRes=928, 640 ; Game_Status=True
nMx,nMy = 0, 0


#Inicia el juego 
def pygame_init(nRes):
    pg.init()
    pg.display.set_caption("Haru_PreRelease v1.17")
    return pg.display.set_mode(nRes)

win = pygame_init(nRes)

#Fondo 
bg = pg.image.load(os.path.join('images','bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()
cursorsito = pg.image.load(os.path.join('imagenes_menu', 'cursor.png'))
clock = pg.time.Clock()


class player(object):
    run = [pg.image.load(os.path.join('images2', str(x) + '.png')) for x in range(8,16)]
   
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.runCount = 0
   
    def draw(self, win):
        if self.runCount > 42:
            self.runCount = 0
        win.blit(self.run[self.runCount//6], (self.x,self.y))
        self.runCount += 1


def redrawWindow():
    win.blit(bg, (bgX, -150))  
    win.blit(bg, (bgX2, -150))  
    runner.draw(win) 
      


# Esta funcion se encarga de caragr la musica a formato de pygame
# para asi poder ser reproducida mas adelante 
def Musica():
    pg.mixer.music.load("Music/Song2.wav")


#Caraga las imagenes a pg
# by alberto Caro 
def Cargar_Imag(aImag,transp=False):
    try:
        imagen = pg.image.load(aImag)                                   
    except pg.error.message:         
            raise SystemExit.message
    imagen = imagen.convert() 
    if transp:# Si transp es True va a tomar el color de 0,0 y luego
        color = imagen.get_at((0,0))# los quitara todos en la imagen 
        imagen.set_colorkey(color)
    return imagen


#Lista con nombres de las imagenes a cargar
aTilesName = ["Menu img/T01.png", # Background
              "Menu img/T01.png",  # Boton Start
              "Menu img/T02.png",
              "Menu img/T03.png",
              "Menu img/T04.png",
              "Menu img/T05.png",
              "Menu img/T06.png",
              "Menu img/T07.png"
              ]


# Lista Con las imagenes ya caragdas de por si dentro de formato de
# Pygame para asi poder ser puestas sobre cualquier superficie.  
imagPY = [Cargar_Imag(aTilesName[0],False), #Imagen de Fondo 
          Cargar_Imag(aTilesName[1],True),
          Cargar_Imag(aTilesName[2],True), # Boton play Sombra
          Cargar_Imag(aTilesName[3],True), # Boton Dos lineas 
          Cargar_Imag(aTilesName[4],True), # Boton play 
          Cargar_Imag(aTilesName[5],True),  # Siguiente cancion
          Cargar_Imag(aTilesName[6],True),
          Cargar_Imag(aTilesName[7],True),
          ]


# Esta funcion se encarga de pintar los botones en la pantalla. 
def Pinta_Menu():
    win.blit(imagPY[1],((393,345)))
    win.blit(imagPY[3],((13,590)))
    win.blit(imagPY[4],((58,590)))
    win.blit(imagPY[5],((103,590)))
    win.blit(imagPY[6],((399,418)))

# Esta funcion se encarga de detectar en base a la posicion del mouse
# y si es que dentro de cieta posicion hay un click entonces debe de 
# realizar una accion.
def BotonesInterac():
    if nMx in range(394,534) and nMy in range(322,380):
        win.blit(imagPY[2],(393,345))
        if e.type == MOUSEBUTTONDOWN:
            #sPausa = pg.event.wait()
            Primer_Nivel()
    if nMx in range(14,48) and nMy in range(590,626):
        if e.type == MOUSEBUTTONDOWN:
            pg.mixer.music.play(10)
    if nMx in range(60,93) and nMy in range(590,626):
        if e.type == MOUSEBUTTONDOWN:
            pg.mixer.music.stop()
            
#==================================================================#
#                              Main                                #
#==================================================================#
#Fondo 
run = True
fps = 60  # NEW
runner = player(150, 535, 69, 44)
pg.time.set_timer(USEREVENT+1, 500)
Musica()

while Game_Status:
    cKey = pg.key.get_pressed()
    if cKey[pg.K_s]   : pg.image.save(win, 'Captura.png')
    ev = pg.event.get()
    for e in ev:
        if e.type == pg.QUIT: Game_Status = 0
        if e.type == pg.MOUSEMOTION: nMx,nMy = e.pos
    #Fondo
    redrawWindow() 
    bgX -= 1.4 
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:  
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

   
    
    Pinta_Menu()
    BotonesInterac()
    win.blit(cursorsito, (nMx, nMy))
    clock.tick(fps) 
    pg.display.update()
    pg.display.flip()
    

