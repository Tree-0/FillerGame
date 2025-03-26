from board import Board
from board_view import BoardView
import pygame
import random
import time

class BoardController:

    def __init__(self, board=None):
        self.model = board if board else Board()
        self.view = BoardView(self.model.width, self.model.height)
    
    def run(self):
        pygame.init()
        available_colors = set(self.model.team_colors)

        running = True
        while running:
            time.sleep(1)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # player must choose color not being used by either player
            for c in self.model.player_colors:
                print(c)
                available_colors.discard(c)
            print(f"available colors: {available_colors}")

            colors = self.model.make_move(random.choice(list(available_colors)))
            # restore the color the player previously was
            available_colors.add(colors['old'])
            
            self.view.display(self.model)

            if self.model.is_game_over():
                running = False

        pygame.quit()