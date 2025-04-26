
import pygame
from settings import ASSETS_DIR

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.shoot_sound     = pygame.mixer.Sound(f"{ASSETS_DIR}/shoot.wav")
        self.explosion_sound = pygame.mixer.Sound(f"{ASSETS_DIR}/explosion.wav")
        self.boss_sound      = pygame.mixer.Sound(f"{ASSETS_DIR}/boss.wav")
        self.volume = 1.0
        self._apply_volume()

    def _apply_volume(self):
        self.shoot_sound.set_volume(self.volume)
        self.explosion_sound.set_volume(self.volume)
        self.boss_sound.set_volume(self.volume)

    def set_volume(self, vol: float):
        self.volume = max(0.0, min(1.0, vol))
        self._apply_volume()

    def increase_volume(self, step: float = 0.1):
        self.set_volume(self.volume + step)

    def decrease_volume(self, step: float = 0.1):
        self.set_volume(self.volume - step)

    def get_volume(self):
        return self.volume

    def play_shoot(self):
        self.shoot_sound.play()

    def play_explosion(self):
        self.explosion_sound.play()

    def play_boss(self):
        self.boss_sound.play()
