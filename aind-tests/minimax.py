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
        # if player first move, return the whole board
        if not current_loc:
            return [(x, y) for x in range(self.num_rows) for y in range(self.num_cols) if self.board[x][y] != 1 ]

        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in rays:
            _x, _y = current_loc
            while 0 <= _x + dx < self.num_rows and 0 <= _y + dy < self.num_cols:
                _x, _y = _x + dx, _y + dy
                if self.board[_x][_y]:
                    break
                moves.append((_x, _y))
        return moves



def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    legal_moves = gameState.get_legal_moves()
    return len(legal_moves) == 0


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1
    v = min(map(lambda m: max_value(gameState.forecast_move(m)), gameState.get_legal_moves()))
    return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1
    v = max(map(lambda m: min_value(gameState.forecast_move(m)), gameState.get_legal_moves()))
    return v

def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    move = max(gameState.get_legal_moves(), key=lambda m: min_value(gameState.forecast_move(m)))
    return move

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