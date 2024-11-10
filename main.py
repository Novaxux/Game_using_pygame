# import pygame ,sys
from settings import *
from character import Character
from bullet import Bullet
from bg import Bg
from enemy import Enemy
from bonus import Bonus
from buttons import Buttons
from max_level import *
from settings import *
from resourcePath import resource_path
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
        self.character = Character()
        self.bg = Bg()
        self.font = pygame.font.Font(resource_path('./assets/sprites/font/BD_Cartoon_Shout.ttf'),20)
        self.active = True
        self.caption = pygame.display.set_caption('Juegito de prueba')
        self.bullet = Bullet(self.character.x, self.character.y, self.display_surface)
        self.bullets = []  # Lista para almacenar balas activas
        # self.character.shoot_delay = 150  # Retraso en milisegundos entre disparos (0.5 segundos)
        self.bonus_time = 2
        # self.character.last_shot_time = 0  # Tiempo del último disparo
        self.score = 0
        self.enemies = []
        self.max_enemies = 3
        self.max_level = load_level()
        self.level = 1
        self.bonus = Bonus()
        self.buttons = Buttons()
       
    def draw_score(self):
        score_surface = self.font.render(f'Score: {self.score}', True, 'white')
        score_rect = score_surface.get_rect(topright=(WIDTH - 10, 10))  # Esquina superior izquierda
        self.display_surface.blit(score_surface, score_rect)
    def draw_level(self):
        level_surface = self.font.render(f'Level: {self.level}', True, 'white')
        score_rect = level_surface.get_rect(topleft=(0 + 10, 10))  # Esquina superior derecha
        self.display_surface.blit(level_surface, score_rect)
    def draw_health(self):
        health_surface = self.font.render(f'Health: {self.character.health}', True, 'white')
        score_rect = health_surface.get_rect(midtop=(WIDTH // 2, 10))  # Parte superior central de la pantalla
        self.display_surface.blit(health_surface, score_rect)
    def draw (self):
        self.buttons.draw(self.display_surface)
        self.bg.draw(self.display_surface)
        self.character.draw(self.display_surface)
        for enemy in self.enemies:
            enemy.draw(self.display_surface)
        for bullets in self.bullets:
            bullets.draw(self.display_surface)
        self.draw_score()
        self.draw_level()
        self.draw_health()
        # if self.bonus.activated:
        #     self.bonus.draw(self.score,self.display_surface)
    def character_collision_update_game(self,current_time):
        if current_time - self.character.last_hit_time > self.character.invulnerability_duration:
            self.character.health -= 1
            self.character.health_down.play()
            self.character.last_hit_time = current_time  # Actualiza el último tiempo de golpe
            if self.character.health == 0:
                self.active = False
            return True
    def bullet_to_enemy_collition_update_game(self,enemy,bullet):
        #  for bullet in self.bullets[:]:
                if enemy.rect.colliderect(bullet.rect):
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    enemy.health -=1
                    if enemy.health == 0:
                        enemy.explosion_sound.play()
                        self.score += 1
                        self.enemies.remove(enemy)
                    return True

    def update_bonus_collition(self,bullet):
        if self.bonus.activated and bullet.rect.colliderect(self.bonus.rect):
            # Elimina la bala y desactiva el bonus
            self.character.shoot_delay = 100
            if bullet in self.bullets:
                self.bullets.remove(bullet)
            self.character.on_bonus = True
            self.score += 1
            self.bonus.reset()
            return True
    def check_collisions(self):
        current_time = pygame.time.get_ticks()  # Tiempo actual
        # Colisiones con enemigos
        for enemy in self.enemies[:]:
            if enemy.rect.colliderect(self.character.rect):
                    if self.character_collision_update_game(current_time):
                        break
            # Colisiones entre balas y enemigos
            for bullet in self.bullets[:]:
                if self.bullet_to_enemy_collition_update_game(enemy,bullet):
                    break
                if self.update_bonus_collition(bullet):
                    break
                # Si la bala sale de la pantalla, se elimina
                if bullet.off_screen() and bullet in self.bullets:
                    self.bullets.remove(bullet)
                # bullet.draw(self.display_surface)
    def generate_bonus(self):
        bonus_score = self.score
        if bonus_score == 5 and self.bonus.start_time is None and self.bonus.activated is False:
            self.bonus.activated = True
            self.bonus.start_time = pygame.time.get_ticks()
        if self.bonus.start_time is not None:
                elapsed_time = (pygame.time.get_ticks() - self.bonus.start_time) / 1000  # Tiempo transcurrido en segundos
                if elapsed_time < self.bonus.duration:
                    self.bonus.draw(self.display_surface)
                else:
                    bonus_score += 1
                    self.bonus.reset()
    def update_game_status(self):
        if self.score >= 10:
            self.level += 1
            self.score = 0
        if self.level > self.max_level:
            self.max_level= self.level
            save_level(self.max_level)
        if self.character.on_bonus is True and self.character.bonus_time is None:
            self.character.bonus_time = pygame.time.get_ticks()
            self.character.on_bonus = False
        if self.character.bonus_time is not None:
            delay_time = pygame.time.get_ticks()
            if delay_time - self.character.bonus_time > 5000:
                self.character.bonus_time = None
                self.character.shoot_delay = 250
            
    def check_increase_difficulty(self):
        if self.level == 2:
            self.max_enemies = 4
        elif self.level == 3:
            self.max_enemies = 5
        elif self.level == 5:
            self.max_enemies = 6
        elif self.level == 6:
            self.max_enemies = 7
        elif self.max_enemies == 10:
            self.max_enemies = 8
    
    def generate_bullets(self):
    # contar el tiempo actual
        current_time = pygame.time.get_ticks()
        # Disparar con retraso
        if self.buttons.shoot_pressed and (current_time - self.character.last_shot_time > self.character.shoot_delay):
            bullet = Bullet(self.character.x, self.character.y, self.display_surface)
            bullet.direction.x, bullet.direction.y = (0,-1)  # Asignar dirección a la bala
            self.bullets.append(bullet)
            self.character.shoot_sound.play()
            self.character.last_shot_time = current_time
            # Solo dispara una bala por ciclo, aunque se mantengan varias teclas presionadas
    def generate_enemies(self):
        if len(self.enemies)< self.max_enemies:
            enemy = Enemy()
            self.enemies.append(enemy)
    def lose (self):
        bg = pygame.Surface((300, 300))
        bg.fill('white')
        bg.set_alpha(70)
        bg_rect = bg.get_rect(center = (WIDTH/2, HEIGHT/2))
        
        msg= self.font.render('Try again', True,'black')
        msg_rect = msg.get_rect(center = (WIDTH/2,HEIGHT/2))

        max_lvl = self.font.render(f'Max Level: {self.max_level}', True,'black')
        max_lvl_rect = max_lvl.get_rect(center = (WIDTH/2, HEIGHT/2 + 30))
        
        self.display_surface.blit(bg,bg_rect)
        self.display_surface.blit(msg,msg_rect)
        self.display_surface.blit(max_lvl,max_lvl_rect)
    def win_bg (self):
            self.active = False
            bg = pygame.Surface((300, 300))
            bg.fill('white')
            bg.set_alpha(50)
            bg_rect = bg.get_rect(center = (WIDTH/2, HEIGHT/2))
            
            msg= self.font.render('You win', True,'black')
            msg_rect = msg.get_rect(center = (WIDTH/2,HEIGHT/2))
            
            self.display_surface.blit(bg,bg_rect)
            self.display_surface.blit(msg,msg_rect)
    def move(self,delta_time):
        self.bg.move(delta_time)
        # self.character.move(keys,delta_time)
        self.buttons.update_character_movement(self.character)
        self.character.move(delta_time)
        if self.bonus.activated:  
            self.bonus.move(delta_time)
        for enemy in self.enemies:
            enemy.move(delta_time)
        for bullet in self.bullets:
            bullet.move(delta_time)
    def try_again(self,event):
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = True
                self.character = Character()
                self.bullets.clear()  # Limpia las balas activas
                self.score = 0
                self.level = 2
                self.max_enemies = 3
                self.enemies.clear()  # Limpia enemigos activos
                self.bonus.reset()
    def run(self):
        last_time = pygame.time.get_ticks()  # Tiempo de la última actualización
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.buttons.check_status(event)
                self.try_again(event)

            # keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()
            delta_time = (current_time - last_time) / 1000  # Delta time en segundos
            last_time = current_time
            # color superficie
            self.display_surface.fill("#696969")
            # mientras no se haya perdido
            self.draw()
            # if self.active and self.level < 10:
            if self.active:
                self.generate_enemies()
                self.update_game_status()
                self.generate_bullets()
                self.generate_bonus()
                self.check_collisions()
                self.move(delta_time)
                self.check_increase_difficulty()
            else:
                self.lose()

            pygame.display.update()
            self.clock.tick(FRAMERATE)
            
if __name__ == '__main__':
    game = Game()
    game.run()