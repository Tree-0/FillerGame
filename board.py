###  
### Board class. This class represents the game board. The board holds a 2D array of TeamColor enums.
### This is the model of the game. The board is responsible for keeping track of the game state, including
### board state, current player, player-owned territories, etc.
### 

import random
from team_color import TeamColor

class Board:

    # TODO FUTURE: Add a parameter to specify the number of players

    def __init__(self, height:int=7, width:int=8, num_colors:int=6, autofill=True):
        self.height = height
        self.width = width

        # default 0, 2D array of TeamColor enums
        self.board = [[TeamColor(0) for x in range(width)] for y in range(height)]

        # Number of colors to use (can't exceed number of offered colors)
        self.num_colors = min(num_colors, len(TeamColor)) 
        # List of colors enums to use
        self.team_colors = [TeamColor(i) for i in range(num_colors)] 
        # Current color of all players
        self.player_colors = [TeamColor(0),TeamColor(0)]

        if autofill:
            self.populate_board()
            self.player_colors[0] = self.board[height-1][0]
            self.player_colors[1] = self.board[0][width-1]

        # Sets of territory that each player owns.
        # Players start with one square each in opposite corners of the board.
        self.territories = [set([(height-1, 0)]), set([(0, width-1)])]
        
        # territory not yet claimed by a player (the starting board)
        self.unclaimed_territory = set([(i, j) for i in range(height) for j in range(width)]) 

        # this player's turn to move
        self.current_player = 0

        
    # Populate the board with random colors ensuring no adjacent squares have the same color
    def populate_board(self) -> None:
        for i in range(0, self.height):
            for j in range(0, self.width):
                available_colors = set(self.team_colors)
                if i > 0:
                    available_colors.discard(self.board[i-1][j])
                if j > 0:
                    available_colors.discard(self.board[i][j-1])
                self.board[i][j] = random.choice(list(available_colors))

    # Print the board
    def print_board(self) -> None:
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.board[i][j].value, end=' ')
            print()

    # Check if the game is over
    def is_game_over(self) -> bool:
        return len(self.unclaimed_territory) == 0
    
    # Determine winning player at any stage in the game 
    # This is simply who has the largest territory.
    def winning_player(self) -> int:
        max_index, max_sublist = max(enumerate(self.territories), key=lambda pair: len(pair[1]))
        print(f"Current winner: Player {max_index}, with {len(max_sublist)} cells")
        return max_index 
    
    # current_player makes a move (changing color), and updating the board
    # Returns a dictionary {old, new} with the colors the player changed between
    def make_move(self, color_change:int) -> tuple:
        new_color = TeamColor(color_change)
        print(f'PLAYER {self.current_player} changing to {new_color.name}')

        # change colors and expand territories
        player_set = self.territories[self.current_player]
        new_cells = set()

        # print(f"PLAYER {self.current_player} SET")
        # print(player_set)
        for cell in player_set:
            row, col = cell[0], cell[1]
            self.board[row][col] = new_color # change color

            # check adjacent
            rowdir = [0, 1, 0, -1]
            coldir = [-1, 0, 1, 0]

            for rx, cx in zip(rowdir, coldir):
                # bounds check
                if row + rx < 0 or col + cx < 0 or row + rx >= self.height or col + cx >= self.width:
                    continue
                
                # color match, expand zone
                if self.board[row + rx][col + cx] == new_color and (row + rx, col + cx) in self.unclaimed_territory:
                    new_cells.add((row + rx, col + cx))
                    self.unclaimed_territory.remove((row + rx, col + cx))

        # add all new cells
        player_set.update(new_cells)

        # return the color the player changed between
        color_switch = {
            "old": self.player_colors[self.current_player],
            "new": new_color
        }

        # officially save new player color 
        self.player_colors[self.current_player] = new_color

        # turn complete, switch players
        self.current_player = 0 if self.current_player else 1

        return color_switch

