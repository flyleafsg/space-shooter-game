# This file contains the game settings and constants for a simple space shooter game.

# settings.py

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Frame rate
FPS = 60

# Player settings
PLAYER_SPEED = 5

# Bullet settings
BULLET_SPEED = 10

# Alien settings
ALIEN_BASE_SPEED = 2    # starting fall speed
ALIEN_ACCEL = 0.2       # speed increase per level
ALIENS_PER_LEVEL = 5    # number of aliens required per level up

# Power-up settings
POWERUP_SPEED = 3       # downward speed of power-ups

# Asset directory path
ASSETS_DIR = "assets"

# Data file for persistence
DATA_FILE = "data/progress.json"
