from settings import *
from resourcePath import resource_path
class Character:
    def __init__(self):
        super().__init__()
        self.x = WIDTH/2  
        self.y = HEIGHT/2 
        self.keys = pygame.key.get_pressed()            
        self.image = pygame.image.load(resource_path(f'./assets/sprites/plane/spaceship_{random.randint(1,2)}.png')).convert_alpha()
        self.sprite = pygame.transform.scale(self.image, (SIDE_BLOCK,SIDE_BLOCK ))  # Ajusta el tamaño aquí
        self.direction = pygame.math.Vector2(0,0)
        self.velocity = 162
        # self.rect = self.sprite.get_rect(topleft=(self.x * SIDE_BLOCK, self.y * SIDE_BLOCK))
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.health = 3
        self.health_down = pygame.mixer.Sound(resource_path('./assets/sound/health_down.mp3'))  # Ruta al archivo de sonido
        self.health_down.set_volume(0.6)
        self.shoot_sound = pygame.mixer.Sound(resource_path('./assets/sound/laser.mp3'))  # Ruta al archivo de sonido
        self.shoot_sound.set_volume(0.2)  # 50% del volumen original
        self.last_shot_time = 0  # Tiempo del último disparo
        self.on_bonus = None
        self.bonus_time = None
        self.shoot_delay = 250
        self.invulnerability_duration = 1000  # 1 segundo en milisegundos
        self.last_hit_time = 0
    
    def move(self, delta_time):
                
            # Actualizar posición del personaje
            self.y += self.direction.y * self.velocity * delta_time
            self.x += self.direction.x * self.velocity * delta_time

            # Limitar el movimiento dentro de la pantalla
            self.y = max(0, min(self.y, HEIGHT - SIDE_BLOCK))
            self.x = max(0, min(self.x, WIDTH - SIDE_BLOCK))
            self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
