import pygame
from settings import WIDTH, HEIGHT

class Buttons:
    def __init__(self):
        self.button_size = WIDTH * 0.1  # 10% del ancho de la pantalla
        # Ubicación de los botones en porcentaje
        self.up_button = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.5, self.button_size, self.button_size)
        self.down_button = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.85, self.button_size, self.button_size)
        self.left_button = pygame.Rect(WIDTH * 0, HEIGHT * 0.675, self.button_size, self.button_size)
        self.right_button = pygame.Rect(WIDTH * 0.2, HEIGHT * 0.675, self.button_size, self.button_size)      
        self.shoot_button = pygame.Rect(WIDTH * 0.75, HEIGHT * 0.5, self.button_size*2.3, self.button_size*2.3)
        self.is_up_pressed = False
        self.is_down_pressed = False
        self.is_left_pressed = False
        self.is_right_pressed = False
        self.shoot_pressed = False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255, 0), self.up_button)    # Botón arriba
        pygame.draw.rect(screen, (0, 0, 255, 0), self.down_button)  # Botón abajo
        pygame.draw.rect(screen, (0, 0, 255, 0), self.left_button)  # Botón izquierda
        pygame.draw.rect(screen, (0, 0, 255, 0), self.right_button) # Botón derecha
        pygame.draw.rect(screen, (0, 0, 255, 0), self.shoot_button) # Botón disparar

    def check_status(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            touch_pos = pygame.mouse.get_pos()
            # Cambiar estado a True si el botón está presionado
            if self.up_button.collidepoint(touch_pos):
                self.is_up_pressed = True
            if self.down_button.collidepoint(touch_pos):
                self.is_down_pressed = True
            if self.left_button.collidepoint(touch_pos):
                self.is_left_pressed = True
            if self.right_button.collidepoint(touch_pos):
                self.is_right_pressed = True
            if self.shoot_button.collidepoint(touch_pos):
                self.shoot_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Cambiar estado a False al soltar el botón
            self.is_up_pressed = False
            self.is_down_pressed = False
            self.is_left_pressed = False
            self.is_right_pressed = False                
            self.shoot_pressed = False                

    def update_character_movement(self, character):
        if self.is_up_pressed:
            character.direction.x, character.direction.y = (0, -1)
        elif self.is_down_pressed:
            character.direction.x, character.direction.y = (0, 1)
        elif self.is_left_pressed:
            character.direction.x, character.direction.y = (-1, 0)
        elif self.is_right_pressed:
            character.direction.x, character.direction.y = (1, 0)
        else:
            character.direction.x, character.direction.y = (0, 0)

    # def generate_bullets(self,keys,bullet):
    # # contar el tiempo actual
    #     current_time = pygame.time.get_ticks()
    #     # Disparar con retraso
    #     for key, direction in self.character.projectile_directions.items(): #devuelve claves, valor
    #         if keys[key] and (current_time - self.last_shot_time > self.character.shoot_delay):
    #             bullet = Bullet(self.character.x, self.character.y, self.display_surface)
    #             bullet.direction.x, bullet.direction.y = direction  # Asignar dirección a la bala
    #             self.bullets.append(bullet)
    #             self.character.shoot_sound.play()
    #             self.last_shot_time = current_time
    #             # break  # Solo dispara una bala por ciclo, aunque se mantengan varias teclas presionadas