from Enums import States, Location, Action, LocationState

type LocationMap = dict[Location, States]

# USED FOR HOMEWORK 2

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


class StatefulReflexAgent:
    def __init__(self):
        self.model: LocationMap = {
            Location.A: States.UNKNOWN,
            Location.B: States.UNKNOWN
        }  # Initially ignorant

        self.state: LocationState = (Location.UNKNOWN, States.UNKNOWN)
        self.last_action: Action = Action.NO_OP

    def match_rule(self) -> Action:  # Match rule for a given state
        percept = self.state

        # Rule 1: If location is Dirty then Suck
        if percept[1] == States.DIRTY:
            return Action.SUCK

        # Rule 2: If all locations are clean then NO_OP
        if self.model[Location.A] == self.model[Location.B] == States.CLEAN:
            return Action.NO_OP

        # Rule 3: If location is Clean then move to the next location
        if percept[0] == Location.A:
            return Action.RIGHT

        if percept[0] == Location.B:
            return Action.LEFT

    def update_state(self, percept: LocationState) -> None:
        location, status = percept
        self.model[location] = status  # Update the model state

    def sensors(self, environment: EnvironmentClass) -> tuple[Location, States]:  # Sense Environment
        location = environment.current_location
        return location, environment.states[location]

    def actuators(self, requested_action: Action, environment: EnvironmentClass) -> None:  # Modify Environment
        location = environment.current_location

        # Improved strat:
        if requested_action not in location.allowed_moves():
            return

        if requested_action == Action.SUCK:
            environment.states[location] = States.CLEAN
        elif requested_action == Action.RIGHT:
            environment.current_location = Location.B
        elif requested_action == Action.LEFT:
            environment.current_location = Location.A

    def act(self, environment: EnvironmentClass) -> Action:
        percept = self.sensors(environment)
        self.state = percept
        self.update_state(percept)
        action = self.match_rule()
        self.actuators(action, environment)
        return action


def run(n):  # run the agent through n steps
    location_space = 10
    status_space = 8
    action_space = 7
    icon = "-> "

    # Setup for the output
    print(f"{'Current':{location_space + status_space + action_space}s}{icon}{'New':8s}")
    print(
        f"{'location':{location_space}s}{'status':{status_space}s}{'action':{action_space}s}{icon}{'location':{location_space}s}{'status':{status_space}s}")

    agent = StatefulReflexAgent()
    for i in range(1, n):
        (location, status) = agent.sensors(base_environment)  # Sense Environment before action
        print(f"{location.name:{location_space}s}{status.name:{status_space}s}", end='')

        action = agent.act(base_environment)
        (location, status) = agent.sensors(base_environment)  # Sense Environment after action
        print(f"{action.name:{action_space}s}{icon}{location.name:{location_space}s}{status.name:{status_space}s}")


if __name__ == '__main__':
    run(20)
