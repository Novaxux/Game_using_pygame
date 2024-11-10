from settings import random, pygame,WIDTH, HEIGHT, SIDE_BLOCK 
from resourcePath import resource_path
class Enemy:
    def __init__(self):
        super().__init__()
        self.x = 0 
        self.y = random.randint(0,HEIGHT -1)
        self.direction = pygame.math.Vector2(1,0)
        self.image = pygame.image.load(resource_path(f'./assets/sprites/enemy/enemy_spaceship_{random.randint(0,1)}.png')).convert_alpha()
        self.sprite = pygame.transform.scale(self.image, (SIDE_BLOCK,SIDE_BLOCK ))  # Ajusta el tamaño aquí
        # rectangulo de colision
        # self.rect = self.sprite.get_rect(topleft=(self.x * SIDE_BLOCK, self.y * SIDE_BLOCK))
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y ))
        self.velocity = 125
        self.health = 2
        self.explosion_sound = pygame.mixer.Sound(resource_path('./assets/sound/explosion.mp3'))  # Ruta al archivo de sonido
        self.explosion_sound.set_volume(0.6)
        
    def reset(self):
        self.x = 0
        # self.y = random.randint(0,CELL_NUM-1)
        self.y = random.randint(0,HEIGHT - 1)
        self.health = 2

    def move(self,delta_time):
        if not self.off_screen():
            self.x += self.direction.x * self.velocity * delta_time
            self.y += self.direction.y * self.velocity * delta_time
        else:    
            # self.x = random.choice([0,WIDTH_CELL_NUM-1])
            # self.y = random.randint(0,CELL_NUM-1)
            self.x = random.choice([0,WIDTH - 1])
            self.y = random.randint(0,HEIGHT - 1)
            if self.x == 0:
                self.direction.x = 1
            else:
                self.direction.x = -1
            self.direction.y = random.randint(-1, 1)
        # self.rect.topleft = (self.x * SIDE_BLOCK, self.y * SIDE_BLOCK)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect) 
    def off_screen(self):
        # Comprueba si la bala ha salido de la pantalla
        # return  not ((0 <= self.x <= WIDTH_CELL_NUM-1) and (0 <= self.y <= CELL_NUM-1))
        return  not ((0 <= self.x <= WIDTH - 1) and (0 <= self.y <= HEIGHT - SIDE_BLOCK))