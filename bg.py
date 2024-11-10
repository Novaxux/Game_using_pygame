from settings import *
from resourcePath import resource_path
class Bg:
    def __init__(self):
        self.color = (187,187,187)
        self.side = SIDE_BLOCK
        # Carga la imagen de fondo
        self.background_image = pygame.image.load(resource_path('./assets/sprites/enviroment/background.jpeg')).convert()
        # Ajusta la imagen de fondo al tamaño de la pantalla
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
        self.bg_y = 0  # Posición inicial de la imagen en el eje y
        self.bg_speed = 700 # Velocidad de desplazamiento


    def draw(self,screen) :
        # self.bg_y += self.bg_speed * delta_time
        # if self.bg_y >= HEIGHT:
        #         self.bg_y = 0
        screen.blit(self.background_image,(0,self.bg_y))
        screen.blit(self.background_image, (0, self.bg_y - HEIGHT + 3))

    def move(self,delta_time):
        self.bg_y += self.bg_speed * delta_time
        if self.bg_y >= HEIGHT:
                self.bg_y = 3