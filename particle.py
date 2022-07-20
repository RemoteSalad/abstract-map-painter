import pygame as pg

class Particle:
    def __init__(self, coord = (150,150), size = 20, color = (0, 0, 255), thickness = 1):
        self.x = coord[0] #x
        self.y = coord[1] #y
        self.size = size
        self.color = color
        self.thickness = thickness

    def display(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)
