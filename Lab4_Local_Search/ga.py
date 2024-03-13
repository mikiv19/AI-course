import random
from typing import Self
from abc import ABC, abstractmethod

default_p_mutation = 0.8
default_num_of_generations = 30
max_population_size = 100

type Population = set[Individual]


class Individual(ABC):
    @abstractmethod
    def get_fitness(self) -> float:
        """Return the fitness of the individual"""
        pass

    @abstractmethod
    def mutate(self):
        """Mutate the individual"""
        pass

    @abstractmethod
    def reproduce(self, other: Self) -> Self:
        """Reproduce the individual with another individual"""
        pass

    def __lt__(self, other: Self) -> bool:
        return self.get_fitness() < other.get_fitness()

    def __repr__(self):
        return f"Fitness: {self.get_fitness()}"


# noinspection DuplicatedCode
def genetic_algorithm(population: Population,
                      minimal_fitness: float,
                      num_of_generations: int = default_num_of_generations,
                      should_trim_population: bool = False,
                      p_mutation=default_p_mutation) -> Individual | None:
    generation: int = 0
    fittest_individual: Individual | None = None

    for generation in range(num_of_generations):
        print(f"Generation {generation}:")
        print_population(population)

        new_population: Population = set()

        for i in range(len(population)):
            mother, father = random_selection(population)
            child = mother.reproduce(father)

            if random.uniform(0, 1) < p_mutation:
                child = child.mutate()

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        if should_trim_population:
            population = trim_population(population, max_population_size)

        fittest_individual = get_fittest_individual(population)

        if minimal_fitness <= fittest_individual.get_fitness():
            break

    print(f"Final generation {generation}:")
    print_population(population)

    return fittest_individual


def print_population(population: Population) -> None:
    if len(population) > 10:
        print(
            f"Population too large to print {len(population)}, fittest individual: {get_fittest_individual(population)}")
        return

    for individual in population:
        print(individual)


def random_selection(population: Population) -> tuple[Individual, Individual]:
    """
    Compute fitness contribution of each individual in population according to the individuals fitness and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population.
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """
    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.

    raise NotImplementedError("Random selection has not yet been implemented")

    # mother = pick_individual(fit_sum, ordered_population)
    # father = pick_individual(fit_sum, ordered_population)

    return mother, father


def pick_individual(total_fitness_sum: float, ordered_population: list[Individual]):
    """Randomly generate a number for the chosen fitness and pick an individual based on the number."""

    raise NotImplementedError("Pick individual has not yet been implemented")

    return ordered_population[-1]


def get_fittest_individual(from_population: Population) -> Individual:
    # We can do the thing below because the Individual class has the __lt__ method
    return max(from_population)


def trim_population(population: Population, desired_length: int) -> Population:
    """
    Trim the population to the desired length by removing the least fit individuals.
    """
    if len(population) <= desired_length:
        return population

    population_list = sorted(population, reverse=True)
    population_list = population_list[:desired_length]

    return set(population_list)
