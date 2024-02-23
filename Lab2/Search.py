from typing import Self, Any


# For this lab we will not be able to fully type the state
# The reason for this is that we wanted a fairly simple implementation for the searcher.
# But we still wanted this searcher to be able to handle all 3 different scenarios.
# Feel free to take it as a challenge to make a strongly typed implementation, that can handle all 3 scenarios.
# Consider doing something that could let the statespace generate the states, and decide what next possible states are.

class StateSpace:
    def __init__(self, state_space: dict = None):
        self.state_space = state_space

    def successor(self, state: Any):
        if self.state_space is None:
            print("No state space set")

        return self.state_space[state]


class Node:
    def __init__(self, state: Any, parent: Self = None, depth: int = 0):
        self.state = state
        self.parent_node = parent
        self.depth = depth

    def path(self) -> list[Self]:
        current_node = self
        path = [self]
        while current_node.parent_node:
            current_node = current_node.parent_node
            path.append(current_node)

        return path

    def expand(self, state_space: StateSpace):
        successors: list[Node] = []
        children = state_space.successor(self.state)
        for child in children:
            s = Node(child, self, self.depth + 1)
            successors = insert(s, successors)

        return successors

    def display(self) -> None:
        print(self)

    def __repr__(self):
        return f"State: {self.state} - Depth: {self.depth}"


def insert(node: Node, queue: list[Node], insert_as_first: bool = True) -> list[Node]:
    """
    Returns a copy of the queue with the node inserted (the fringe).
    It does not modify the input queue.
    Use the insert_as_first parameter to decide if the node should be inserted at the beginning or the end of the queue.
    """
    pass


def insert_all(nodes_to_add: list[Node], queue: list[Node], insert_as_first: bool = True) -> list[Node]:
    """
    Inserts all nodes from the input list, into the queue using the insert function defined in this script.
    Therefore, it will return a copy of the queue with the nodes inserted and not modify the original queue.
    """
    pass


def remove_first(queue: list[Node]) -> Node:
    """Removes the first element from the input list.
    The removed element will be returned."""
    # Hint this function is really short, and you can probably do it in one line
    pass


class Searcher:
    def __init__(self, initial_state, goal_state, state_space: StateSpace = None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.state_space = state_space

    def tree_search(self, insert_as_first: bool = True) -> list[Node]:
        """Search the tree for the goal state
        and return the path from the initial state to the goal state."""
        fringe: list[Node] = []
        initial_node = Node(self.initial_state)
        fringe = insert(initial_node, fringe)
        while fringe is not None:
            node = remove_first(fringe)
            if node.state == self.goal_state:
                return node.path()
            children = node.expand(self.state_space)
            fringe = insert_all(children, fringe, insert_as_first)
            print(f"Fringe: {fringe}")

    def run(self, insert_as_first: bool = True):
        path = self.tree_search(insert_as_first)
        print("Solution path:")
        for node in path:
            node.display()


if __name__ == '__main__':
    input_state_space = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': ['H', 'I', 'J'],
        'H': [],
        'I': [],
        'J': [],
    }

    searcher = Searcher('A', 'J', state_space=StateSpace(input_state_space))
    print("??-first")
    searcher.run(insert_as_first=True)
    print("????-first")
    searcher.run(insert_as_first=False)
