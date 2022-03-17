import queue
from problem import *

nodes_expanded = 0
def a_star(ship : ShipProblem):
    node_queue = queue.PriorityQueue()

    # append a list containing the function cost and initial ship
    node_queue.put(append_cost(ship))
    global nodes_expanded 
    nodes_expanded += 1

    while (1):
        if (node_queue.empty()):
            print("no solution: SIFT?")
            return -1
        else: 
            # get ship from top of queue
            top_ship = node_queue.get()

            # check if ship is balanced
            if (is_balanced(top_ship)):
                return top_ship
            else:
                enqueue_nodes(queue = node_queue, ships = expand_node(top_ship))
    return

# Purpose: attach a function cost to a ShipNode that the queue can sort by
# return the ShipProblem with its assigned function cost
def append_cost(ship : ShipProblem):
    gn = ship.distance_cost
    if gn == 0: 
        ship.function_cost = 0
    else: 
        ship.function_cost = gn + heuristic_cost(ship)
    return ship


# Purpose: takes in a ShipProblem and returns the heuristic cost
# heurisitc measured in estimated minutes to move all containers necessary
def heuristic_cost(ship : ShipProblem):
    left_mass = 0
    right_mass = 0
    balanced_mass = ship.mass / 2
    left_containers = []
    right_containers = []

    for container in ship.grid:
        x_coord = int(container["coordinate"][1])
        if (x_coord <= 3): 
            left_mass += container["weight"]
            left_containers.append(container)
        else: 
            right_mass += container["weight"]
            right_containers.append(container)

    ## find number of containers to move
    if left_mass < right_mass:
        defecit = balanced_mass - left_mass
        defecit_side = "left"
        # sort the right side in descending order
        sorted_containers = sorted(right_containers, key= lambda i : i["weight"], reverse = True)
    else: 
        defecit = balanced_mass - right_mass
        defecit_side = "right"
        # sort the left side in descending order
        sorted_containers  = sorted(left_containers, key= lambda i : i["weight"], reverse = True)

    container_shifts = 0
    computed_minutes = 0
    remaining_defecit = defecit

    for container in sorted_containers:
        if container["weight"] <= remaining_defecit:
            container_shifts += 1
            remaining_defecit -= container["weight"]

            ## manhattan cost is abs(x_coord - target_x_coord) 
            if defecit_side == "left":
                computed_minutes += abs(int(container["coordinate"][1]) - 3)
            elif defecit_side == "right":
                computed_minutes += abs(int(container["coordinate"][1]) - 4)

    # if no containers can be moved, function cost infinity
    if container_shifts == 0:
        return float("inf")

    if remaining_defecit > balanced_mass * 0.05:
        return float("inf")

    return computed_minutes

# Purpose: takes in a ship grid from a Ship and returns if the ship is balanced
def is_balanced(ship : ShipProblem):
    left_mass = 0
    right_mass = 0
    balanced_mass = ship.mass / 2

    for container in ship.grid:
        x_coord = int(container["coordinate"][1])
        if (x_coord <= 3): left_mass += container["weight"]
        else: right_mass += container["weight"]

    return (abs(left_mass - right_mass) / balanced_mass) <= 0.1

# Purpose: takes in a new list of ShipNodes
def enqueue_nodes(queue, ships):
    for ship in ships:
        queue.put(append_cost(ship))
        global nodes_expanded
        nodes_expanded += 1
    return queue

# Purpose: takes in a ShipNode and "expands it," returning new, valid ship grids.  
# returns a list of ShipNodes with new ship grids derived from the passed in ShipNode
# return value is passed into enqueueNodes()
def expand_node(ship : ShipProblem):
    # list that holds generated ShipNodes
    all_new_ships = []

    # each operation on ship grid returns a new ship grid
    for i in range(1, 7):
        # move_crane returns a list of ShipProblems
        new_ships = ship.move_crane(i)
        if new_ships == [[]]: continue
        all_new_ships += new_ships

    return all_new_ships

def get_steps(end_ship):
    steps = []
    ship = end_ship
    while ship.parent != None:
        steps.append(ship.change)
        ship = ship.parent
    steps.append(ship.change)
    steps.reverse()

    return steps

# def main():
#     grid = [
#             {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
#             {'coordinate': ['01', '02'], 'weight': 0, 'text': 'NAN'}, 
#             {'coordinate': ['02', '02'], 'weight': 4000, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
#             {'coordinate': ['01', '06'], 'weight': 6000, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
#             {'coordinate': ['02', '01'], 'weight': 3000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
#             {'coordinate': ['02', '06'], 'weight': 1000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
#             {'coordinate': ['03', '01'], 'weight': 5000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
#             {'coordinate': ['04', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
#             {'coordinate': ['01', '03'], 'weight': 2000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
#             {'coordinate': ['05', '01'], 'weight': 7000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}]
#     ship = ShipProblem(grid=grid)
#     end_ship = a_star(ship)

#     steps = get_steps(end_ship)
#     for step in steps:
#         print(step)
#     print(f"Nodes expanded {nodes_expanded}")

# main()