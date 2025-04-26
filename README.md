space_shooter/
│
├── assets/
│   ├── player.png
│   ├── bullet.png
│   ├── alien.png
│   └── background.jpg
│
├── data/
│   └── progress.json      # for saving high‐scores & level
│
├── main.py                # game loop, event handling
├── settings.py            # constants (screen size, speeds, file paths)
├── player.py              # Player sprite class
├── bullet.py              # Bullet sprite class
├── alien.py               # Alien sprite class & level logic
└── logger.py              # functions to read/write progress.json
