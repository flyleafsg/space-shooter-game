
# menu.py
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.options = ["Start Game", "Settings", "Quit"]
        self.selected = 0
        # Precompute option positions
        self.option_rects = []
        for i, option in enumerate(self.options):
            rect = self.font.render(option, True, (255, 255, 255)).get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 60)
            )
            self.option_rects.append(rect)

    def display(self):
        """Draws menu options with highlight for selected."""
        self.screen.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (200, 200, 200)
            text_surf = self.font.render(option, True, color)
            rect = self.option_rects[i]
            self.screen.blit(text_surf, rect)
        pygame.display.flip()

    def run(self):
        """Handles keyboard and mouse input to select menu options."""
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(30)
            self.display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "Quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.options[self.selected]
                elif event.type == pygame.MOUSEMOTION:
                    # Update selection on hover
                    for i, rect in enumerate(self.option_rects):
                        if rect.collidepoint(event.pos):
                            self.selected = i
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Click selection
                    for i, rect in enumerate(self.option_rects):
                        if rect.collidepoint(event.pos):
                            return self.options[i]

    def pause(self):
        """Displays a pause screen until 'P' is pressed."""
        font = pygame.font.Font(None, 72)
        text = font.render("PAUSED (P to resume)", True, (255, 255, 255))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False
            self.screen.blit(text, rect)
            pygame.display.flip()

    def settings(self, sound_manager):
        """Volume control screen."""
        opts = ["Volume ↑", "Volume ↓", "Back"]
        sel = 0
        clock = pygame.time.Clock()

        # Precompute settings rects
        rects = []
        for i, o in enumerate(opts):
            rect = self.font.render(o, True, (255, 255, 255)).get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 60)
            )
            rects.append(rect)

        while True:
            clock.tick(30)
            self.screen.fill((10, 10, 10))

            # Render options
            for i, o in enumerate(opts):
                color = (255, 255, 0) if i == sel else (200, 200, 200)
                txt = self.font.render(o, True, color)
                self.screen.blit(txt, rects[i])

            # Render current volume
            vol_txt = self.font.render(f"Vol: {int(sound_manager.get_volume()*100)}%", True, (180, 180, 180))
            vrect = vol_txt.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
            self.screen.blit(vol_txt, vrect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sel = (sel - 1) % len(opts)
                    elif event.key == pygame.K_DOWN:
                        sel = (sel + 1) % len(opts)
                    elif event.key == pygame.K_RETURN:
                        choice = opts[sel]
                        if choice == "Volume ↑":
                            sound_manager.increase_volume(0.1)
                        elif choice == "Volume ↓":
                            sound_manager.decrease_volume(0.1)
                        elif choice == "Back":
                            return
