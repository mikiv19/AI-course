from enum import Enum
from typing import Self


class Symbols(Enum):
    X = "X"
    O = "O"
    UNPLACED = "i"

    def __str__(self):
        return self.value

    @classmethod
    def placed(cls) -> tuple[Self, Self]:
        return cls.X, cls.O


type Board = list[Symbols]


def minmax_decision(state: Board) -> int:
    def max_value(state_option: Board) -> int:
        if is_terminal(state_option):
            return utility_of(state_option)
        expected_value = -infinity
        for (a, s) in successors_of(state_option):
            expected_value = max(expected_value, min_value(s))
        return expected_value

    def min_value(state_option: Board) -> int:
        if is_terminal(state_option):
            return utility_of(state_option)
        expected_value = infinity
        for (a, s) in successors_of(state_option):
            expected_value = min(expected_value, max_value(s))
        return expected_value

    infinity = float('inf')
    action, state = max(successors_of(state), key=lambda a: min_value(a[1]))
    return action


def is_terminal(state: Board) -> bool:
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard.
    Ex: [Unplaced; Unplaced; Unplaced; Unplaced; X; Unplaced; Unplaced; Unplaced; Unplaced]
    :return:
    """
    raise NotImplementedError("Implement this function")


def utility_of(state: Board) -> int:
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard.
    Ex: [Unplaced; Unplaced; Unplaced; Unplaced; X; Unplaced; Unplaced; Unplaced; Unplaced]
    :return:
    """

    # For this function it might be beneficial to create helper functions to check different aspects of the board.
    # This can help to avoid making this function overly complicated.

    raise NotImplementedError("Implement this function")


def successors_of(state: Board) -> list[tuple[int, Board]]:
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard.
    Ex: [Unplaced; Unplaced; Unplaced; Unplaced; X; Unplaced; Unplaced; Unplaced; Unplaced]
    :return:
    """
    raise NotImplementedError("Implement this function")


def display(state: list[Symbols]) -> None:
    print("-----")
    for i in range(0, 3):
        for c in range(i * 3, i * 3 + 3):
            print("|", end="")
            symbol = c if state[c] == Symbols.UNPLACED else state[c]
            print(symbol, end="")
        print("|")


def main():
    board = [Symbols.UNPLACED] * 9
    while not is_terminal(board):
        board[minmax_decision(board)] = Symbols.X
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = Symbols.O
    display(board)


if __name__ == '__main__':
    main()
