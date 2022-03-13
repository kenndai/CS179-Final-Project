import queue
from problem import *

def a_star(ship : ShipProblem):
    node_queue = queue.PriorityQueue()

    # append a list containing the function cost and initial ship
    node_queue.put(append_cost(ship))

    while (1):
        if (node_queue.empty()):
            print("no solution: SIFT?")
            return -1
        else: 
            # get ship from top of queue
            top_ship = node_queue.get()

            # check if ship is balanced
            if (is_balanced(top_ship.grid)):
                return top_ship.grid
            else:
                enqueue_nodes(queue = node_queue, ships = expand_node(top_ship))
    return

# Purpose: attach a function cost to a ShipNode that the queue can sort by
# returns a list containing the function cost and the ShipNode
def append_cost(ship : ShipProblem):
    gn = ship.distance_cost
    if gn == 0: 
        ship.function_cost = 0
    else: 
        ship.function_cost = gn + heuristic_cost(ship.grid)
    return ship


# Purpose: takes in a ship grid from ShipNode and returns the heuristic cost
def heuristic_cost(ship_grid : ShipProblem.grid):
    return 1

# Purpose: takes in a ship grid from ShipNode and returns if the ship is balanced
def is_balanced(ship_grid : ShipProblem.grid):
    return 

# Purpose: takes in a new list of ShipNodes
def enqueue_nodes(queue, ships):
    for ship in ships:
        queue.put(append_cost(ship))
    return queue

# Purpose: takes in a ShipNode and "expands it," returning new, valid ship grids.  
# returns a list of ShipNodes with new ship grids derived from the passed in ShipNode
# return value is passed into enqueueNodes()
def expand_node(ship : ShipProblem):
    # list that holds generated ShipNodes
    new_ships = []

    # each operation on ship grid returns a new ship grid
    for i in range(1, 7):
        # move_crane returns a list of grids
        new_ship_grids = ship.move_crane(i)

        # TODO: Compare if new_ship_grid is the same as parent_ship_grid, if not, append to new_ships
        for new_ship_grid in new_ship_grids:
            if new_ship_grid == [[]]: continue
            new_ships.append(ShipProblem(distance_cost = ship.distance_cost + 1, grid = new_ship_grid, parent = ship))

    return new_ships

def main():
    grid = [
        {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
        {'coordinate': ['01', '02'], 'weight': 0, 'text': 'NAN'}, 
        {'coordinate': ['01', '06'], 'weight': 2500, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
        {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
        {'coordinate': ['02', '06'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
        {'coordinate': ['03', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
        {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
        {'coordinate': ['05', '01'], 'weight': 99999, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}]
    ship = ShipProblem(grid=grid)
    a_star(ship)

main()