import pygame as pg

class MainGame:
    def __init__(self):
        # constants
        self.TIMER: int

        # variables
        self.head = (100, 100, 50, 50)

        self.time_passed = 0

    def start(self):
        self.TIMER = pg.USEREVENT + 1
        pg.time.set_timer(self.TIMER, 1000)

    def update(self, screen):
        pg.draw.rect(screen, "purple", self.head)

        if self.time_passed == 1:
            print(f"a second passed")
            self.time_passed = 0

    def event(self, e):
        if e.type == self.TIMER:
            self.time_passed += 1