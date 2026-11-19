import pygame as pg

class MainGame:
    def __init__(self):
        self.Head = (100, 100, 50, 50)

    def start(self):
        ...

    def update(self, screen):
        pg.draw.rect(screen, "purple", self.Head)



    def event(self, e):
        ...