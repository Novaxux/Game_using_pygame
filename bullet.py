# from rect import Rectangle
import math, pygame
from settings import *
from resourcePath import resource_path
# class Bullet(Rectangle):
class Bullet:
    def __init__(self, x, y,screen):
        super().__init__()
        self.x = x 
        self.y = y
        self.screen = screen
        self.color = (234,32,55)
        self.direction = pygame.math.Vector2(0,-1)
        self.image = pygame.image.load(resource_path('./assets/sprites/projectile/up_projectile.png')).convert_alpha()
        self.sprite_up = pygame.transform.scale(self.image, (SIDE_BLOCK,SIDE_BLOCK ))  # Ajusta el tamaño aquí
        # self.sprite_up = pygame.transform.scale(self.image, (25,25))  # Ajusta el tamaño aquí
        self.velocity = 625
        self.sprite_down = pygame.transform.rotate(self.sprite_up,180)
        # Rectángulo del proyectil para detectar colisiones y controlar el dibujo
        # self.rect = self.sprite_up.get_rect(topleft=(self.x * SIDE_BLOCK, self.y * SIDE_BLOCK))
        self.rect = self.sprite_up.get_rect(topleft=(self.x, self.y))
    def move(self, delta_time):             
        self.y += self.direction.y * self.velocity * delta_time
        self.x += self.direction.x * self.velocity * delta_time
        # self.rect.topleft = (self.x * SIDE_BLOCK, self.y * SIDE_BLOCK)
        self.rect.topleft = (self.x, self.y )

    def draw(self, screen):
                     # Establecer el sprite según la dirección inicial
        self.sprite = self.sprite_up if self.direction.y == -1 else self.sprite_down
        # if self.direction.y == -1 :
        screen.blit(self.sprite,self.rect)
        # if self.direction.y == 1 :
        #     screen.blit(self.sprite_down,self.rect)
    def off_screen(self):
        # Comprueba si la bala ha salido de la pantalla
        return  not ((0 <= self.x <= WIDTH-1) and (0 <= self.y <= HEIGHT-1))

        