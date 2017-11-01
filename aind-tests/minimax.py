from copy import deepcopy

class GameState:

    def __init__(self):
        self.num_rows = 3
        self.num_cols = 2
        self.board = [[0] * self.num_cols for i in range(self.num_rows)]
        self.board[2][1] = 1
        self.parity = 0
        self.player_loc = [None, None]
        print(self.board)
    
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        game = deepcopy(self)
        x, y = move
        game.board[x][y] = 1
        game.player_loc[self.parity] = move
        game.parity ^= 1
        return game
        
    
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        current_loc = self.player_loc[self.parity]
        if not current_loc:
            return [(x, y) for x in range(self.num_rows) for y in range(self.num_cols) if self.board[x][y] != 1 ]


print("Creating empty game board...")
g = GameState()

print("Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print("Found {} legal moves.".format(len(p1_empty_moves or [])))

print("Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))

print("Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()
if (0, 0) in set(p2_empty_moves):
    print("Failed\n  Uh oh! (0, 0) was not blocked properly when " +
          "player 1 moved there.")
else:
    print("Everything looks good!")