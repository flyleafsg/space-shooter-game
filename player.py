
import pygame
from settings import ASSETS_DIR, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Load and set up the player sprite
        # Ensure the path includes the slash
        self.image = pygame.image.load(f"{ASSETS_DIR}/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = PLAYER_SPEED
        # Power-up flags
        self.multishot = False
        self.shield = False

    def update(self, keys):
        # Move left/right
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x += self.speed

    def shoot(self, bullet_group):
        from bullet import Bullet
        # Single or multi-shot
        if not self.multishot:
            bullet = Bullet(self.rect.midtop)
            bullet_group.add(bullet)
        else:
            offsets = [(-15, 0), (0, 0), (15, 0)]
            for dx, dy in offsets:
                pos = (self.rect.centerx + dx, self.rect.top + dy)
                bullet = Bullet(pos)
                bullet_group.add(bullet)
