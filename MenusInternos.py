import pygame as pg
import os

Game_Status=True
nMx,nMy = 0, 0

# Se encarga de cargar la imagenes a formato de pygame
# By Alberto Caro
def CI(aImag,transp=False):
    try:
        imagen = pg.image.load(aImag)                                   
    except pg.error.message:         
            raise SystemExit.message
    imagen = imagen.convert() 
    if transp:# Si transp es True va a tomar el color de 0,0 y luego
        color = imagen.get_at((0,0))# los quitara todos en la imagen 
        imagen.set_colorkey(color)
    return imagen



# Se encarga de cargar ciertas imagenes a formato de pygame para asi 
# Poder pintarlas donde uno desee dentro del bucle. (Otras imagenes)
def CargaBotonM():
    Botones=[]
    Botones.append(CI(nBoton[0], True))
    Botones.append(CI(nBoton[1], True))
    Botones.append(CI(nBoton[2], True))
    Botones.append(CI(nBoton[3], True))
    Botones.append(CI(nBoton[4], True))
    return Botones


# Nombre de los archivos que debe de cargar.
nBoton=["Menu img/FondoMenu/B1.png",
        "Menu img/FondoMenu/B2.png",
        "Menu img/FondoMenu/B2.png",
        "Menu img/FondoMenu/B3.png",
        "Menu img/FondoMenu/B4.png",
        "Menu img/FondoMenu/B5.png"
        ]
        

# Se encarga de pintar lso botones cargados a formato de pygame en 
# las posiciones donde deberian or estos para que parezca menu.      
def PintaMenu(Surface, Lista):
    Surface.blit(Lista[0],(310,213))
    Surface.blit(Lista[1],(310,278))
    Surface.blit(Lista[3],(310,338))
    Surface.blit(Lista[4],(560,338))




# Se coloco el Ciclo del juego dentro de una funcion con todas las 
# acciones que este debe hacer para asi poder exportarlo a otro 
# archivo con faciliddad.
def MenuOpciones(Ventana):
    Menu = pg.Surface((928, 640))
    Menu.fill((0,0,0))
    Botones = CargaBotonM()
    MenuStatus = True
    cursorsito = pg.image.load(os.path.join('imagenes_menu', 'cursor.png'))
    nMx = 0 ; nMy = 0
    while MenuStatus:
        cKey = pg.key.get_pressed()
        if cKey[pg.K_i]:
            return
        ev = pg.event.get()
        for e in ev:
            if e.type == pg.QUIT: 
                MenuStatus = False    
                quit()
            if e.type == pg.MOUSEMOTION: nMx,nMy = e.pos
            if nMx in range(310,614) and nMy in range(210,255):
                if e.type == pg.MOUSEBUTTONDOWN:
                    return False
            if nMx in range(310,614) and nMy in range(276,320):
                if e.type == pg.MOUSEBUTTONDOWN:
                    return True
            if nMx in range(310,614) and nMy in range(336,380):
                if e.type == pg.MOUSEBUTTONDOWN:
                    MenuStatus = False    
                    quit()
        PintaMenu(Menu, Botones)
        Ventana.blit(Menu,(0,0))
        Ventana.blit(cursorsito,(nMx,nMy))      
        pg.display.update()
        
        


        
        
        




















