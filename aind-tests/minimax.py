
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
        game = copy.deepcopy(self)
        x, y = move
        self.board[x][y] = 1
        self.player_loc[self.parity] = move
        self.parity ^= 1
        
    
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
        pass

g = GameState()