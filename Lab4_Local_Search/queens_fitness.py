"""
Chessboard module
"""

def fitness_fn_negative(board_view: tuple[int, ...]):
    """
    Compute the number of conflicting pairs, negated.
    For a solution with 5 conflicting pairs the return value is -5, so it can
    be maximized to 0.

    This fitness function have already been quite optimized, but feel free to
    try to optimize it further.
    You can always start with analysing the Big O notation of the function.
    """

    n = len(board_view)
    fitness = 0
    for column, row in enumerate(board_view):
        for other_column in range(column + 1, n):
            # Horizontal
            # (to the right of me, diagonal above, diagonal below)
            # collisions = (row, row + (column - other_column), row - (column - other_column))
            # if individual[other_column] in collisions:
            #     contribution += 1

            # if individual[other_column] == row:
            #     contribution += 1
            #     # continue

            # # Diagonals
            dx = abs(column - other_column)
            dy = abs(row - board_view[other_column])
            if dx == dy or dy == 0:
                fitness += 1

    return - fitness


# We do not use the positive fitness function, but it is retained for reference
# in addition, it shows an alternative way to approach the problem
def fitness_fn_positive(state):
    '''
    Compute the number of non-conflicting pairs.
    '''

    def conflicted(state, row, col):
        for c in range(col):
            if conflict(row, col, state[c], c):
                return True

        return False

    def conflict(row1, col1, row2, col2):
        return (
            row1 == row2 or
            col1 == col2 or
            row1 - col1 == row2 - col2 or
            row1 + col1 == row2 + col2
        )

    fitness = 0
    for col in range(len(state)):
        for pair in range(1, col + 1):
            if not conflicted(state, state[pair], pair):
                fitness = fitness + 1
    return fitness
