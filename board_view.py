import pygame
from board import Board

class BoardView:

    def __init__(self, board:Board=None):
        self.cell_size = 50

        # Generate or pass in a existing model
        if not board:
            self.board_model = Board()
        else:
            self.board_model = board

        # visual dimensions of the board
        self.width = self.board_model.width * self.cell_size
        self.height = self.board_model.height * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    # draw the state of the board
    def display(self):
        # reset screen 
        self.screen.fill("white")

        # render new game state
        for i in range(0, self.board_model.height):
            for j in range(0, self.board_model.width):
                color = self.board_model.board[i][j].rgb
                pygame.draw.rect(self.screen, color, 
                                 (j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size))
        
        # display the new state
        pygame.display.flip()