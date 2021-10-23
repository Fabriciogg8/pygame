import pygame as pg
vec = pg.math.Vector2


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (252, 240, 3)
BLUE = (0, 0, 255)
DARKGREY = (40, 40, 40)
PGREEN = (129, 207, 52)
WALLCOLOR = (86, 219, 148)
GREY = (171, 176, 172)
CYAN = (50, 168, 158)

# propiedades del juego
WIDTH = 1024 # 16 * 64 or 32 * 32 or 64 *16
HEIGHT = 704 # 16 * 48 or 32 * 24 or 64 * 12 #originalmente 768 le baje dos cuadrados para poder ver todo el escenario 
FPS = 60
TITLE = "Earthelp"
BGCOLOR = GREY

TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE 

WALL_IMG = "tile_367.png"

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 250 #son pixeles por segundo, si nuestra pantalla tiene 1024, demora 10 segundos en cruzar la pantalla si lo ponemos en 100
PLAYER_IMG = "soldier1_gun.png"
PLAYER_ROT_SPEED = 150 #mismo sistema que para la velocidad en este caso grados por segundo
PLAYER_HIT_RECT = pg.Rect(0,0,32,32)
BARREL_OFFSET = vec(20,10) #es una constante para que la bala salga desde el punto correcto donde esta el arma

# Gun settings
BULLET_IMG = "tile_187.png"
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200 #velocidad que nos empuja hacia atras cada vez que disparamos el arma
GUN_SPREAD = 5 #para que las balas no salgan tan en linea recta, asi se ve mas real que salgan medio torcidas
BULLET_DAMAGE = 10


# Mob settings
MOB_IMG = "hitman1_knife.png"
MOB_SPEEDS = [150, 75, 125, 100, 115, 65, 200, 185]
MOB_HIT_RECT = pg.Rect(0,0,32,32)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50