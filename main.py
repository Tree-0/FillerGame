import pygame
import random
import time 
from board import Board 
from board_view import BoardView

def main():

    pygame.init()
    board_view = BoardView()
    board_model = board_view.board_model

    available_colors = set(board_model.team_colors)

    running = True
    while running:
        time.sleep(1)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # player must choose color not being used by either player
        for c in board_model.player_colors:
            print(c)
            available_colors.discard(c)
        print(f"available colors: {available_colors}")

        colors = board_model.make_move(random.choice(list(available_colors)))
        # restore the color the player previously was
        available_colors.add(colors['old'])
        
        board_view.display()

        if board_model.is_game_over():
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()