from Enums import States, Location, Action, LocationState

type LocationMap = dict[Location, States]


# USED FOR EXERCISE 2 & 3 & HOMEWORK 1

class EnvironmentClass:
    def __init__(self, current_location: Location, states: LocationMap):
        self.current_location = current_location
        self.states = states


base_environment = EnvironmentClass(
    current_location=Location.A,
    states={
        Location.A: States.DIRTY,
        Location.B: States.DIRTY
    }
)


class Agent:
    def __init__(self, environment: EnvironmentClass):
        self.environment = environment

    def sensor(self) -> LocationState:
        location = self.environment.current_location
        return location, self.environment.states[location]

    def actuator(self, action: Action) -> None:
        location = self.environment.current_location
        if action == Action.SUCK:
            self.environment.states[location] = States.CLEAN
        elif action == Action.RIGHT and action in location.allowed_moves():
            self.environment.current_location = Location.B
        elif action == Action.LEFT and action in location.allowed_moves():
            self.environment.current_location = Location.A

    def evaluate(self) -> Action:
        """:return: The action that the agent has chosen to take. For printing purposes"""
        state = self.sensor()

        action = self.choose_action(state)

        self.actuator(action)

        return action

    @staticmethod
    def choose_action(state: LocationState) -> Action:
        if state[1] == States.DIRTY:
            return Action.SUCK
        if state[0] == Location.A:
            return Action.RIGHT
        if state[0] == Location.B:
            return Action.LEFT


def run(n) -> None:  # run the agent through n steps
    location_space = 10
    status_space = 8
    action_space = 7
    icon = "-> "

    agent = Agent(base_environment)

    # Setup for the output
    print(f"{'Current':{location_space + status_space + action_space}s}{icon}{'New':8s}")
    print(
        f"{'location':{location_space}s}{'status':{status_space}s}{'action':{action_space}s}{icon}{'location':{location_space}s}{'status':{status_space}s}")

    for i in range(1, n):
        (location, status) = agent.sensor()  # Sense Environment before action
        print(f"{location.name:{location_space}s}{status.name:{status_space}s}", end='')

        # Run the agent
        action = agent.evaluate()

        # Print final result
        (location, status) = agent.sensor()  # Sense Environment after action
        print(f"{action.name:{action_space}s}{icon}{location.name:{location_space}s}{status.name:{status_space}s}")


if __name__ == '__main__':
    run(10)
