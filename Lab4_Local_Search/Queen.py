import random
import time

from Lab4.ga import Individual, genetic_algorithm
from typing import Self

from Lab4.queens_fitness import fitness_fn_negative

p_mutation = 0.5
p_value_mutation = 0.5
num_of_generations = 100

type BoardView = tuple[int, int, int, int, int, int, int, int]


class Board(Individual):
    def __init__(self, gene: BoardView):
        self.gene = gene

    def get_fitness(self) -> float:
        raise NotImplementedError("get_fitness should be implemented in Queen.py.")

    def mutate(self) -> Self:
        raise NotImplementedError("mutate should be implemented in Queen.py.")

    def reproduce(self, other: Self) -> Self:
        raise NotImplementedError("reproduce should be implemented in Queen.py.")

    def __hash__(self):
        return hash(self.gene)

    @classmethod
    def create_random(cls) -> Self:
        gene = (1, 2, 3, 4, 5, 6, 7, 8)
        for i in range(8):
            gene = gene[:i] + tuple([random.randint(1, 8)]) + gene[i + 1:]
        return cls(gene)

    def __repr__(self) -> str:
        return f"Gene: {self.gene} - Fitness: {self.get_fitness()}"


def get_initial_population(count: int) -> set[Board]:
    """
    Randomly generate count individuals of 8 queens on a board.
    Note since it uses a set it disregards duplicate elements.
    """
    raise NotImplementedError("get_initial_population should be implemented in Queen.py.")


def test():
    print(Board((1, 2, 3, 4, 5, 6, 7, 8)).get_fitness())


def main():
    minimal_fitness = 0

    initial_population = get_initial_population(8)

    start_time = time.perf_counter_ns()
    fittest = None # call the genetic algorithm function here with the correct parameters
    end_time = time.perf_counter_ns()
    print(f"Fittest Individual: {fittest} - fitness: {fittest.get_fitness()}")
    elapsed_time = (end_time - start_time) / 10 ** 6
    print(f"total elapsed time: {elapsed_time} ms")


if __name__ == '__main__':
    main()
    # test()
