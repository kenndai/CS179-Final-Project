import queue
from problem import *

nodes_expanded = 0

## pass in initialized ShipProblem
def transfer(ship : ShipProblem):
    currShip = ship
    while len(currShip.offloads) < 0 and len(currShip.loads) < 0:
        ## get ship with one container offloaded
        currShip = offload(currShip)

        ## get a container to load
        load_container = currShip.loads().pop()
        print(f'Grab {load_container["text"]} from truck')
        ## get weight from front end
        load(load)

def offload(ship : ShipProblem):
    node_queue = queue.PriorityQueue()

    start_num_offload = len(ship.offloads)

    node_queue.put(ship)
    global nodes_expanded 
    nodes_expanded += 1
    while (1):
        if (node_queue.empty()):
            print("no solution: SIFT?")
            return -1
        else: 
            # get ship from top of queue
            top_ship = node_queue.get()

            # check if a container has been unloaded
            # if len(top_ship.loads) == 0 and len(top_ship.offloads) == 0:
            if len(top_ship.offloads) < start_num_offload:
                return top_ship
            else:
                ships = expand_node(top_ship)
                enqueue_nodes(queue = node_queue, ships = ships)

def load(ship : ShipProblem, weight = 0):
    ## pop a container from a ship's list of loads
    load_container = ship.loads.pop()

    offloads_in_column = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    for container in ship.offloads:
        column = container["coordinate"][1]
        offloads_in_column[column] += 1

    min_column = min(offloads_in_column, key=offloads_in_column.get)
    
    ## get the top container of the column with the fewest offload containers
    curr_top = ship.top_containers[min_column]
    if curr_top == None:
        new_y_coord = 1
    else:
        new_y_coord = curr_top["coordinate"][0] + 1

    ## need to update weight somehow

    ## place the load container on top of the previous top container
    load_container["coordinate"] = [new_y_coord, min_column]
    ship.grid.append(load_container)
    
    return ship

# calculates the amount of containers on top of a container to offload, including the container to offload
def offload_heuristic(ship : ShipProblem):
    containers_on_top = len(ship.offloads)

    for off_container in ship.offloads:
        for container in ship.grid:
            if container["coordinate"][1] != off_container["coordinate"][1]: continue
            if container["coordinate"][0] == off_container["coordinate"][0]:
                containers_on_top += 1
    return containers_on_top

def append_costs(ship : ShipProblem):
    gn = ship.distance_cost
    hn = offload_heuristic(ship)
    ship.function_cost = gn + hn
    return ship

def enqueue_nodes(queue, ships):
    for ship in ships:
        queue.put(append_costs(ship))
        global nodes_expanded
        nodes_expanded += 1
    return queue

def expand_node(ship : ShipProblem):
    new_ships = []
    columns_to_expand = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
    }
    for container in ship.offloads:
        column_num = container["coordinate"][1]
        if columns_to_expand[column_num] == 0:
            columns_to_expand[column_num] = 1
            new_ships += ship.move_crane(column_num, mode="offload")

    return new_ships

def get_steps(end_ship):
    steps = []
    ship = end_ship
    while ship.parent != None:
        steps.append(ship.change)
        ship = ship.parent
    steps.append(ship.change)
    steps.reverse()

    return steps

def main():
    grid = [{'coordinate': ['01', '01'], 'weight': 5, 'text': 'John Deere Parts (call Sue at Ohio office)'},
            {'coordinate': ['01', '02'], 'weight': 2, 'text': 'John Deere Parts (call Sue at Ohio office)'},
            {'coordinate': ['02', '02'], 'weight': 10, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            {'coordinate': ['01', '03'], 'weight': 4, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            ]

    ship = ShipProblem(grid = grid,
                       loads = [{'coordinate': ['00', '00'], 'weight': 0, 'text': 'loader'}],
                       offloads = [{'coordinate': ['01', '01'], 'weight': 5, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
                                   {'coordinate': ['01', '02'], 'weight': 2, 'text': 'John Deere Parts (call Sue at Ohio office)'}])

    # while (len(ship.offloads) > 0):
    #     ship = offload(ship)
    #     for step in get_steps(ship):
    #         print(step)
    #     ship = ShipProblem(grid=ship.grid, offloads=ship.offloads)
    #     print(f"Nodes expanded {nodes_expanded}")

    ship = load(ship)
    for container in ship.grid:
        print(container)

main()