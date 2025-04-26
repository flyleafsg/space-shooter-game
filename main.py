# main.py
import pygame, sys, random
from settings    import *
from player      import Player
from bullet      import Bullet
from alien       import Alien
from logger      import load_progress, save_progress

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()

    # Load progress
    progress    = load_progress()
    high_score  = progress["high_score"]
    max_level   = progress["max_level"]

    # Sprite groups
    player_group = pygame.sprite.GroupSingle(Player((SCREEN_WIDTH//2, SCREEN_HEIGHT - 30)))
    bullet_group = pygame.sprite.Group()
    alien_group  = pygame.sprite.Group()

    score = 0
    level = 1
    alien_speed = ALIEN_BASE_SPEED

    spawn_timer = 0

    while True:
        dt = clock.tick(FPS) / 1000  # seconds since last frame

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save before exiting
                save_progress(max(high_score, score), max(max_level, level))
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_group.sprite.shoot(bullet_group)

        keys = pygame.key.get_pressed()
        player_group.update(keys)
        bullet_group.update()
        alien_group.update()

        # --- Alien Spawning Logic ---
        spawn_timer += dt
        if spawn_timer > max(0.5, 2 - level * 0.1):
            spawn_timer = 0
            # spawn an alien at random x
            alien = Alien((random.randint(20, SCREEN_WIDTH-20), -50), speed=alien_speed)
            alien_group.add(alien)

        # --- Collision Detection ---
        for bullet in pygame.sprite.groupcollide(bullet_group, alien_group, True, True):
            score += 10
            if score > high_score:
                high_score = score
        # Aliens hitting bottom?
        for alien in list(alien_group):
            if alien.rect.top > SCREEN_HEIGHT:
                alien.kill()
                # penalize or end game:
                save_progress(high_score, max(max_level, level))
                game_over(screen, score, high_score)

        # --- Level Up ---
        if score >= level * ALIENS_PER_LEVEL * 10:
            level += 1
            alien_speed += ALIEN_ACCEL

        # --- Rendering ---
        screen.fill((0, 0, 0))
        # optional: draw background
        player_group.draw(screen)
        bullet_group.draw(screen)
        alien_group.draw(screen)

        # draw score & level
        font = pygame.font.Font(None, 36)
        screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Level: {level}", True, (255,255,255)), (10,50))
        screen.blit(font.render(f"High Score: {high_score}", True, (255,255,255)), (10,90))

        pygame.display.flip()

def game_over(screen, score, high_score):
    # Simple game over screen
    font = pygame.font.Font(None, 72)
    text = font.render("GAME OVER", True, (255,0,0))
    screen.blit(text, text.get_rect(center=screen.get_rect().center))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

