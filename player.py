
import pygame
from settings import ASSETS_DIR, PLAYER_SPEED 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(ASSETS_DIR + 'player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = PLAYER_SPEED

def updata(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x += self.speed

def shoot(self, bullet_group):
     from bullet import Bullet
     bullet = Bullet(self.rect.midtop)
     bullet_group.add(bullet)