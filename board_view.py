import pygame
from board import Board

class BoardView:

    def __init__(self, width, height, cell_size=50):
        # visual dimensions of the board
        self.cell_size = cell_size
        self.width = width * self.cell_size * 2
        self.height = height * self.cell_size * 2
        self.screen = pygame.display.set_mode((self.width, self.height))

    # draw the state of a given board
    def display(self, model):
        self.screen.fill("white")
        for i in range(0, model.height):
            for j in range(0, model.width):
                color = model.board[i][j].rgb
                pygame.draw.rect(self.screen, color, 
                                 (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
        pygame.display.flip()