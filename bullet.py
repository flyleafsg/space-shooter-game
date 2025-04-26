# bullet.py
import pygame
from settings import ASSETS_DIR, BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Animated bullet frames
        self.frames = [
            pygame.image.load(f"{ASSETS_DIR}/bullet_1.png").convert_alpha(),
            pygame.image.load(f"{ASSETS_DIR}/bullet_2.png").convert_alpha(),
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = BULLET_SPEED
        self.animation_timer = 0
        self.animation_speed = 0.1  # seconds per frame

    def update(self, dt):
        # Animate
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
        # Move up
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
