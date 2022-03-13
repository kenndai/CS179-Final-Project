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
            # get and pop list on top of queue
            top_node = node_queue.get()
            # get ShipNode from the list
            top_ship = top_node[1]

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

    # check if the ShipProblem is the initial ShipProblem, initial ShipProblem doesn't need a hn
    if (gn == 0): return [0, ship]

    hn = heuristic_cost(ship.grid)
    return [gn + hn, ship]


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

# Purpose: takes in a ShipNode and "expands it," returning new, valid ship grids.  
# returns a list of ShipNodes with new ship grids derived from the passed in ShipNode
# return value is passed into enqueueNodes()
def expand_node(ship : ShipProblem):
    # list that holds generated ShipNodes
    new_ship_nodes = []

    # each operation on ship grid returns a new ship grid
    for i in range(6):
        # move_crane returns a list of grids
        new_ship_grids = ship.move_crane(i)

        # TODO: Compare if new_ship_grid is the same as parent_ship_grid, if not, append to new_ship_nodes
        for new_ship_grid in new_ship_grids:
            new_ship_nodes.append(ShipProblem(distance_cost = ship.distance_cost + 1, ship_grid = new_ship_grid, parent_ship_grid = ship))

    return new_ship_nodes

def main():
    problem = ShipProblem()
    a_star(problem)

main()