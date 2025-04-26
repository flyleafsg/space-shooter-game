# alien.py
import pygame
import math
from settings import ASSETS_DIR, SCREEN_HEIGHT, ALIEN_BASE_SPEED

class Alien(pygame.sprite.Sprite):
    def __init__(self, pos, speed=ALIEN_BASE_SPEED, frames=None):
        super().__init__()
        # Animated alien frames
        self.frames = frames or [
            pygame.image.load(f"{ASSETS_DIR}/alien_frame1.png").convert_alpha(),
            pygame.image.load(f"{ASSETS_DIR}/alien_frame2.png").convert_alpha(),
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(midtop=pos)
        self.speed = speed
        self.animation_timer = 0
        self.animation_speed = 0.2

    def update(self, dt):
        # Animate
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
        # Move down
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class BossAlien(Alien):
    def __init__(self, pos, speed, health=20):
        # Load boss frames
        frames = [
            pygame.image.load(f"{ASSETS_DIR}/boss_frame1.png").convert_alpha(),
            pygame.image.load(f"{ASSETS_DIR}/boss_frame2.png").convert_alpha(),
            pygame.image.load(f"{ASSETS_DIR}/boss_frame3.png").convert_alpha(),
        ]
        super().__init__(pos, speed, frames)
        self.health = health

    def update(self, dt):
        # Base animation & movement
        super().update(dt)
        # Oscillate horizontally for boss effect
        offset = int(2 * math.sin(pygame.time.get_ticks() / 500))
        self.rect.x += offset
        if self.health <= 0:
            self.kill()
