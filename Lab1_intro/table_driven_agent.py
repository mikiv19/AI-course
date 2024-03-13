from Enums import LocationState, Location, States, Action

type Percept = LocationState
type Percepts = list[Percept]

# USED FOR EXERCISE 1

total_percepts: Percepts = []

# Helper combos:
clean_A = (Location.A, States.CLEAN)
dirty_A = (Location.A, States.DIRTY)
clean_B = (Location.B, States.CLEAN)
dirty_B = (Location.B, States.DIRTY)

type LookupTable = dict[tuple[Percept, ...], Action]

table_definition: LookupTable = {
    (clean_A,): Action.RIGHT,
    (dirty_A,): Action.SUCK,
    (clean_B,): Action.LEFT,
    (dirty_B,): Action.SUCK,
    (clean_A, clean_A): Action.RIGHT,
    (clean_A, dirty_A): Action.SUCK,
    # ...
    (clean_A, clean_A, clean_A): Action.RIGHT,
    (clean_A, clean_A, dirty_A): Action.SUCK,
    (clean_A, dirty_A, clean_B): Action.LEFT,
    # ...
}


def LOOKUP(percepts: Percepts, table: LookupTable) -> Action:
    """
    Lookup appropriate action for percepts
    :return: Action from table or Action.NO_OP if no suitable action found
    """
    return table.get(tuple(percepts), Action.NO_OP)


def TABLE_DRIVEN_AGENT(percept: Percept) -> Action:  # Determine action based on table and percepts
    total_percepts.append(percept)  # Add percept
    return LOOKUP(total_percepts, table_definition)  # Lookup appropriate action for percepts


def run():  # run agent on several sequential percepts
    action_space = 14
    print(f"{"Action":{action_space}s}| Percepts")
    print(f"{TABLE_DRIVEN_AGENT(clean_A):{action_space}s}| {total_percepts}")
    print(f"{TABLE_DRIVEN_AGENT(dirty_A):{action_space}s}| {total_percepts}")
    print(f"{TABLE_DRIVEN_AGENT(clean_B):{action_space}s}| {total_percepts}")
    print(f"{TABLE_DRIVEN_AGENT(dirty_B):{action_space}s}| {total_percepts}")

if __name__ == '__main__':
    run()
