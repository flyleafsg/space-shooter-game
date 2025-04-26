# main.py
# main.py (excerpt)
sound = SoundManager()
menu  = Menu(screen)

choice = menu.run()
if choice == "Quit":
    pygame.quit()
    sys.exit()
elif choice == "Settings":
    menu.settings(sound)
    # once back from settings, go to menu again
    choice = menu.run()
    if choice != "Start Game":
        pygame.quit()
        sys.exit()

# now proceed into your game loop…
