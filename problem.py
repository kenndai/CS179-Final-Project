class ShipNode:
    __slots__ = ["distance_cost", "ship_state", "parent_ship_state"]

    def __init__(self, distance_cost, ship_state, parent_ship_state = None):
        self.distance_cost = distance_cost
        self.ship_state = ship_state
        self.parent_ship_state = parent_ship_state

class ShipProblem:

    __slots__ = ["initial_state", "total_moves"]

    def __init__(self, consensed_manifest = None):
        self.initial_state = [
            {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '02'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '06'], 'weight': 2500, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            {'coordinate': ['01', '11'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '12'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['02', '06'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['03', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['05', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}]

        # self.initial_state = condensed_manifest

        ## set total_moves to 1 so operations begin with an odd move
        self.total_moves = 1
        

    # define operations to move a container to another column
    ## Odd moves: pick up
    ## Even moves: place down

    ## position crane over first column
    def move_crane_first(self, ship_state : ShipNode.ship_state):
        new_states = []
        top_container = None
        curr_top_y = -1
        for container in ship_state:
            x_coord = int(container["coordinate"][1])
            if x_coord != 1: continue
            y_coord = int(container["coordinate"][0])

            ## find the top container in the first column
            ## if column is EMPTY or highest contianer is NAN, skip
            if container["text"] == "NAN": continue
            if y_coord > curr_top_y:
                curr_top_y = y_coord
                top_container = container

        if curr_top_y == -1: return
        for i in range(2, 5):
            new_states.append()

        return top_container

    ## position crane over first column
    def move_crane_second(self, ship_state : ShipNode.ship_state):

        return

    ## position crane over first column
    def move_crane_third(self, ship_state : ShipNode.ship_state):

        return

    ## position crane over first column
    def move_crane_fourth(self, ship_state : ShipNode.ship_state):

        return


ship_state = [
            {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '02'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '06'], 'weight': 2500, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            {'coordinate': ['01', '11'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '12'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['02', '06'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}]

problem2 = ShipProblem()
ship_problem = problem2.initial_state

print(problem2.move_crane_first(ship_problem))