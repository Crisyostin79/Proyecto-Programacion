# Bienvenidos al Proyecto de Programacion 1
# [Debido a un Problema logistico debera descargar el archivo de musica desde GDRIVE](https://drive.google.com/drive/folders/1O1p14FyGHiSGr3v12_giqn6aa6of5Dhd?usp=sharing)
Este trabajo pertenece: <br>
[Jorge Soto](https://github.com/Linich14)                
[Christian Verdugo](https://github.com/Crisyostin79)        

### Idea General del Proyecto :shipit:
Este proyecto fue hecho para el Progra 1 de la carrera de Ingieneria Civil En Informatica de la UCT en la cual dentro del proyecto nos propusimos crear un videojuego ocupando las diversos conocimientos que hemos ido adquiriendo a lo largo del ramo tanto de este y complementado del de Programacion de Robot, en si este proyecto se trata sobre crear una especie de juego del genero de plataforma para que se hagan un ejemplo como Mario Bros.<br>
Como primer avance decidimos dividir este proyecto en 3 partes para asi trabajar cada una por separado y luego unirlo todo de las cuales las partes para desarrollar el juego fueron principalmente el Personaje, Mapa, Menu.

## [Mapa](Mapa)
El Mapa del proyecto investigamos sobre que habian varias formas de realizar el mapa del juego en este caso encontramos una que se peude hacer de manera mas facil o mas general debido a que de por si la manera mas facil de generar un mapa es con un arreglo dentro de python y en base a ese arreglo ir pintando los tiles dentro de la superficie del mapa pero en este caso haremos eso mismo pero utilizando dos programas externos los cuales son los que se muestran acontinuacion.

### Los programas Fueron: 
- [TexturePackerGui](https://www.codeandweb.com/texturepacker) Este programa fue el encargado de hacer la union de las imagenes(Tiles) dentro de una sola imagen y aparte de eso hacer un archivo .json con todos los datos de donde encontraba cada tile dentro de la imagen creada para asi despues dentro de pygame poder cargarla de mejor manera sin ocupar tanto espacio y recursos.
- [Tiled](https://www.mapeditor.org/) Este programa nos da la facilidad de crear los mapas de manera mas rapida y comoda ya que con la imagen deberemos de solo ir pintando como si cada tile fuera un color distinto y luego eso se exporta a un formato .csv que mas adelante sera leido dentro de python para asi crear el mapa de manera mas facil y generar mas de un mapa ya solo con el hecho de crearlo el **Tiled**.

## Librerias Importadas
- **PYGAME:** Este es un modulo para python el cual esta principalmente esta orientado a la creacion de videojuegos de manera mas sencilla.
  - Referencia: Se pude evidenciar en la mayoria de los codigos.
- **CSV:** Este es un modulo para python es permite la escritura y lectura de archivos .csv que son archivos del tipo tabulares por asi decirse como trabajar con un "Excel".
  - Referencia: [Tiles.py](Mapa/Tiles.py)
- **JSON:** Este es un modulo que se especializa en trabajar con archivos  de formato JSON(JavaScript Object Notation) que principalmente es un intercambio de datos de objetos de Sintaxis literal de Java Script.
  - Referencia: [SpritesHoja.py](Mapa/SpritesHoja.py)
- **OS:** Este modulo cumple la funcion que de moverse atravez de las archivos de windows o mas bien de las rutas
  - Referencia: [Tiles.py](Mapa/Tiles.py)

## Funciones de Librerias.
### **Pygame:**
   - pygame.init()
   - pygame.display.set_caption()
   - pygame.display.set_mode((*Ancho*,*Largo*))
   - *Superficie*.get_at():
   - pygame.sprite.Sprite:
   - pygame.get_rect():
   - *Superficie*.blit(*Cosa a pintar*,(*Posicion X*, *Posicon Y*)):
   - pygame.Surface(*Ancho*,*Alto*):
   - *Superficie*.set_colorkey(())
   - *Superficie*.draw():
   - pygame.image.load():
   - pygame.time.Clocl():
   - pygame.display.update():
   - pygame.event.get()
   - pygame.QUIT
  
### **OS:**
   - os.path.join()
  
### **CSV:**
   - csv.reader( )
  
### **JSON:**
   - json.load()




## [Sprites.py](SpritesHoja.py)
[Creditos de donde salieron los codigos](https://www.youtube.com/watch?v=mCdA4bJAGGk)
