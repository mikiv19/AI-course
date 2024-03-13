from collections.abc import Iterable
from typing import Callable

# This is based on the game Nim, where each player must in turn select a pile to split.
# The result of the split must be 2 piles of different sizes

type Piles = list[int]


def alpha_beta_decision(state: Piles) -> list[int]:
    infinity = float('inf')

    def max_value(state_option: Piles, alpha: float, beta: float) -> int:
        if is_terminal(state_option):
            return utility_of(state_option)
        expected_value = -infinity
        for successor in successors_of(state_option):
            expected_value = max(expected_value, min_value(successor, alpha, beta))
            if expected_value >= beta:
                return expected_value
            alpha = min(alpha, expected_value)
        return expected_value

    def min_value(state_option: Piles, alpha: float, beta: float) -> int:
        if is_terminal(state_option):
            return utility_of(state_option)
        v = infinity

        for successor in successors_of(state_option):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v

    state = argmax(
        successors_of(state),
        lambda a: min_value(a, infinity, -infinity)
    )
    return state


def is_terminal(state: Piles) -> bool:
    """
    Takes in a state and returns True if the state is terminal, False otherwise.
    A state is terminal if all piles are of size 1 or 2
    """
    raise NotImplementedError("Implement this function")


def utility_of(state: Piles) -> int:
    """
    Takes in a terminal state and outputs +1 if the computer has won, -1 if the player has won
    And 0 if the state is not terminal.
    The player makes the first move, and the game starts with 1 pile.
    """
    raise NotImplementedError("Implement this function")


def successors_of(state: Piles) -> list[Piles]:
    """
    Given a state, returns a list of all possible states that can be reached from the input state.
    A move consists of splitting a single pile. The successors are the states that can be reached after one move.
    """
    raise NotImplementedError("Implement this function")


def split_pile_options(pile: int) -> list[Piles]:
    """
    Given a pile, returns a list of all possible splits.
    Since the pile can only be split once, all output lists will have 2 elements.
    The pile split must not result in two piles of the same size.
    """
    raise NotImplementedError("Implement this function")


def argmax(iterable: Iterable, func: Callable[[Piles], int]):
    return max(iterable, key=func)


def computer_select_pile(state: Piles) -> Piles:
    return alpha_beta_decision(state)


def user_select_pile(list_of_piles: Piles) -> Piles:
    """
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    """
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("What is the number of the pile you want to split?")
        print("The pile must have more than 2 stones")
        print(f"Choose a number between 1 and {len(list_of_piles)}")
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        print_str = f"Where should the first split be (from 1 to {max_split}"
        if list_of_piles[i] % 2 == 0:
            print_str += f", but not {list_of_piles[i] // 2}"

        print_str += ")?"
        print(print_str)

        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [7]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)
            print("The computer has split a pile")

    print("    Final state is {}".format(state))


if __name__ == '__main__':
    main()
