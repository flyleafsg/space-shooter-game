
# menu.py
# menu.py
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self, screen):
        self.screen   = screen
        self.font     = pygame.font.Font(None, 50)
        self.options  = ["Start Game", "Settings", "Quit"]
        self.selected = 0

    def display(self):
        self.screen.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (200, 200, 200)
            text  = self.font.render(option, True, color)
            rect  = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i*60))
            self.screen.blit(text, rect)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "Quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        return self.options[self.selected]
            self.display()

    def pause(self):
        font = pygame.font.Font(None, 72)
        text = font.render("PAUSED (P to resume)", True, (255, 255, 255))
        rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
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
        """Volume up/down and return."""
        opts = ["Volume ↑", "Volume ↓", "Back"]
        sel  = 0
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            # render
            self.screen.fill((10, 10, 10))
            for i, o in enumerate(opts):
                color = (255,255,0) if i==sel else (200,200,200)
                txt = self.font.render(o, True, color)
                r = txt.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i*60))
                self.screen.blit(txt, r)

            # show current volume
            vol_txt = self.font.render(f"Vol: {int(sound_manager.get_volume()*100)}%", True, (180,180,180))
            vrect   = vol_txt.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 80))
            self.screen.blit(vol_txt, vrect)

            pygame.display.flip()

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sel = (sel - 1) % len(opts)
                    if event.key == pygame.K_DOWN:
                        sel = (sel + 1) % len(opts)
                    if event.key == pygame.K_RETURN:
                        choice = opts[sel]
                        if choice == "Volume ↑":
                            sound_manager.increase_volume(0.1)
                        elif choice == "Volume ↓":
                            sound_manager.decrease_volume(0.1)
                        elif choice == "Back":
                            return
