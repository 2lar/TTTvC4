"""
The Agent class. Note that the agent has just a single minimax function.
The minimax function is used in a generic Game class
"""

class Agent:
    def __init__(self, game, selfPiece, opponentPiece):
        self.game = game
        self.MIN = -float('inf')
        self.MAX = float('inf')
        self.winscore =  10000000
        self.losescore = -10000000
        self.selfPiece = selfPiece          #AI
        self.opponentPiece = opponentPiece  #HUMAN


    '''
    This is the function you must complete
    Inputs -
    1. self (Agent object reference)
    2. board (2d array)
    3. depth (float)
    4. maximizingPlayer (bool)
    5. alpha (float)
    6. beta (float)

    Outputs -
    1. score (float)
    2. next_move (type discussed below)

    Notes
    1. Need to create general implementation that considers all move types - tuple or float
    2. We use depth here to measure how far down we need to keep going, we stop at depth = 0
    3. Need to consider the different situations when game is over
    4. Prioritize winning in fewest moves
    5. next_move is the best possible move from valid_moves based on alpha-beta pruning. 
       Do not need to focus on its type, since it differs based on game, just find best move from valid_moves
    '''
    def minimax(self, board, depth, maximizingPlayer, alpha, beta):
        if self.game.is_winner(board, self.selfPiece):
            return None, self.winscore + depth
        if self.game.is_winner(board, self.opponentPiece):
            return None, self.losescore - depth
        if depth == 0 or self.game.is_full(board):
            return None, self.game.heuristic_value(board, self.selfPiece if maximizingPlayer else self.opponentPiece)

        best_score = self.MIN if maximizingPlayer else self.MAX
        best_move = None
        for move in self.game.get_valid_moves(board):
            new_board = self.game.play_move(board, move, self.selfPiece if maximizingPlayer else self.opponentPiece)
            forgamepy, score = self.minimax(new_board, depth - 1, not maximizingPlayer, alpha, beta)
            if maximizingPlayer:
                if score > best_score:
                    best_score, best_move = score, move
                alpha = max(alpha, score)
            else:
                if score < best_score:
                    best_score, best_move = score, move
                beta = min(beta, score)

            if beta <= alpha:
                break

        return best_move, best_score