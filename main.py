# main.py
import pygame
import sys
import random

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    ALIEN_BASE_SPEED,
    ALIEN_ACCEL,
    ALIENS_PER_LEVEL,
    ASSETS_DIR
)
from player   import Player
from bullet   import Bullet
from alien    import Alien, BossAlien
from powerup  import PowerUp
from logger   import load_progress, save_progress, log_event
from sound    import SoundManager     # ← this must come *before* you ever call it
from menu     import Menu

def game_over(screen, score, high_score):
    """Display Game Over screen and wait."""
    font = pygame.font.Font(None, 72)
    text_surface = font.render("GAME OVER", True, (255, 0, 0))
    rect = text_surface.get_rect(center=screen.get_rect().center)
    screen.blit(text_surface, rect)
    pygame.display.flip()
    pygame.time.wait(3000)


def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tourette Gun vs Aliens")
    clock = pygame.time.Clock()

    # Load background
    background_image = pygame.image.load(f"{ASSETS_DIR}/background.jpg").convert()

    # Managers
    sound_manager = SoundManager()
    menu = Menu(screen)

    # Main menu loop
    while True:
        choice = menu.run()
        if choice == "Quit":
            pygame.quit()
            sys.exit()
        if choice == "Settings":
            menu.settings(sound_manager)
            continue
        if choice == "Start Game":
            break

    # Load progress
    progress = load_progress()
    high_score = progress.get("high_score", 0)
    max_level = progress.get("max_level", 1)

    # Sprite groups
    player_group = pygame.sprite.GroupSingle(
        Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    )
    bullet_group = pygame.sprite.Group()
    alien_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()

    # Game state
    score = 0
    level = 1
    alien_speed = ALIEN_BASE_SPEED
    spawn_timer = 0.0
    powerup_timer = 0.0

    # Game loop
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(high_score, max(max_level, level))
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_group.sprite.shoot(bullet_group)
                    sound_manager.play_shoot()
                if event.key == pygame.K_p:
                    menu.pause()

        # Update
        keys = pygame.key.get_pressed()
        player_group.update(keys)
        bullet_group.update(dt)
        alien_group.update(dt)
        powerup_group.update(dt)

        # Spawn aliens
        spawn_timer += dt
        if spawn_timer >= max(0.5, 2 - level * 0.1):
            spawn_timer = 0.0
            x = random.randint(20, SCREEN_WIDTH - 20)
            if level % 5 == 0 and not any(isinstance(a, BossAlien) for a in alien_group):
                boss = BossAlien((x, -100), speed=alien_speed * 0.5, health=level * 10)
                alien_group.add(boss)
                sound_manager.play_boss()
                log_event(f"Boss spawned at level {level}")
            else:
                alien = Alien((x, -50), speed=alien_speed)
                alien_group.add(alien)
                log_event(f"Alien spawned at speed {alien_speed}")

        # Spawn power-ups
        powerup_timer += dt
        if powerup_timer >= 10.0:
            powerup_timer = 0.0
            pu = PowerUp()
            powerup_group.add(pu)
            log_event("PowerUp spawned")

        # Collisions bullets vs aliens
        hits = pygame.sprite.groupcollide(bullet_group, alien_group, True, False)
        for _, aliens in hits.items():
            for a in aliens:
                if isinstance(a, BossAlien):
                    a.health -= 1
                    if a.health <= 0:
                        a.kill()
                        sound_manager.play_explosion()
                        score += 50
                        log_event("Boss destroyed")
                else:
                    a.kill()
                    sound_manager.play_explosion()
                    score += 10
                    log_event("Alien destroyed")
                high_score = max(high_score, score)

        # Collisions player vs power-ups
        for pu in pygame.sprite.spritecollide(player_group.sprite, powerup_group, False):
            pu.apply(player_group.sprite)
            sound_manager.play_explosion()
            log_event(f"PowerUp applied: {pu.type}")

        # Check game over
        for a in alien_group.sprites():
            if a.rect.top > SCREEN_HEIGHT:
                save_progress(high_score, max(max_level, level))
                game_over(screen, score, high_score)
                running = False
                break
        if not running:
            break

        # Level up
        if score >= level * ALIENS_PER_LEVEL * 10:
            level += 1
            alien_speed += ALIEN_ACCEL
            log_event(f"Level up to {level}")

        # Draw
        screen.blit(background_image, (0, 0))
        player_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)
        powerup_group.draw(screen)

        font = pygame.font.Font(None, 36)
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, (255, 255, 255)), (10, 50))
        screen.blit(font.render(f"High Score: {high_score}", True, (255, 255, 255)), (10, 90))

        pygame.display.flip()

    # Restart
    main()


if __name__ == "__main__":
    main()
