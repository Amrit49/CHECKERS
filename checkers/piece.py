import pygame.draw
from .constants import *


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calculate_pos()

    def calculate_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        if not self.king:
            self.king = True

    def draw_piece(self, screen):
        radius = SQUARE_SIZE // 2 - 15
        pygame.draw.circle(screen, GREY, (self.x, self.y), radius + 2)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
        if self.king:
            screen.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_pos()

    # def __repr__(self):
    #     return self.color

