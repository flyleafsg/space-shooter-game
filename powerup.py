# powerup.py
import pygame
import random
from settings import ASSETS_DIR, SCREEN_WIDTH, SCREEN_HEIGHT, POWERUP_SPEED

class PowerUp(pygame.sprite.Sprite):
    # Types of power-ups and their images
    TYPES = ["extra_bullet", "shield"]
    IMAGES = {
        "extra_bullet": pygame.image.load(f"{ASSETS_DIR}/powerup_bullet.png").convert_alpha(),
        "shield": pygame.image.load(f"{ASSETS_DIR}/powerup_shield.png").convert_alpha(),
    }

    def __init__(self, pos=None):
        super().__init__()
        self.type = random.choice(self.TYPES)
        self.image = self.IMAGES[self.type]
        # Spawn at random x if not provided
        x = pos[0] if pos else random.randint(20, SCREEN_WIDTH - 20)
        y = pos[1] if pos else -50
        self.rect = self.image.get_rect(midtop=(x, y))
        self.speed = POWERUP_SPEED

    def update(self, dt):
        # Fall downwards
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def apply(self, player):
        # Apply effect to player
        if self.type == "extra_bullet":
            player.multishot = True
        elif self.type == "shield":
            player.shield = True
        self.kill()

