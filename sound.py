
# sound.py
import pygame
from settings import ASSETS_DIR

class SoundManager:
    def __init__(self):
        # Initialize mixer
        pygame.mixer.init()
        # Load sounds
        self.shoot_sound = pygame.mixer.Sound(f"{ASSETS_DIR}/shoot.wav")
        self.explosion_sound = pygame.mixer.Sound(f"{ASSETS_DIR}/explosion.wav")
        self.boss_sound = pygame.mixer.Sound(f"{ASSETS_DIR}/boss.wav")

    def play_shoot(self):
        self.shoot_sound.play()

    def play_explosion(self):
        self.explosion_sound.play()

    def play_boss(self):
        self.boss_sound.play()

