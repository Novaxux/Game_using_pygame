from settings import *
from enemy import Enemy
from resourcePath import resource_path
class Bonus(Enemy):
    def __init__(self):
        super().__init__()
        self.start_time = None
        self.image = pygame.image.load(resource_path('./assets/sprites/bonus/bonus.png')).convert_alpha()
        self.sprite = pygame.transform.scale(self.image, (SIDE_BLOCK,SIDE_BLOCK ))  # Ajusta el tamaño aquí
        self.activated = False
        self.duration = 4
        self.elapsed_time = None
    
    def reset(self):
        self.start_time = None
        self.activated = False  