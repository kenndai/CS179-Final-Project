class ShipNode:
    def __init__(self, distance_cost, ship_state, parent_ship_state = None):
        __slots__ = [distance_cost, ship_state, parent_ship_state]

        self.distance_cost = distance_cost
        self.ship_state = ship_state
        self.parent_ship_state = parent_ship_state

class ShipProblem:
    # load 
    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]

    # define operations to move a container to another column