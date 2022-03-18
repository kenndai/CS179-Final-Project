import queue
from re import S

from numpy import append
from problem import *

nodes_expanded = 0
def offload(ship : ShipProblem):
    node_queue = queue.PriorityQueue()

    start_num_offload = len(ship.offloads)
    start_num_load = len(ship.loads)

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
    return


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
            {'coordinate': ['02', '01'], 'weight': 1, 'text': 'John Deere Parts (call Sue at Ohio office)'},
            {'coordinate': ['01', '02'], 'weight': 2, 'text': 'John Deere Parts (call Sue at Ohio office)'},
            {'coordinate': ['02', '02'], 'weight': 10, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            {'coordinate': ['01', '03'], 'weight': 4, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            ]
    ship = ShipProblem(grid= grid, offloads = [{'coordinate': ['01', '01'], 'weight': 5, 'text': 'John Deere Parts (call Sue at Ohio office)'},
                                               {'coordinate': ['01', '02'], 'weight': 2, 'text': 'John Deere Parts (call Sue at Ohio office)'}])

    while (len(ship.offloads) > 0):
        ship = offload(ship)
        for step in get_steps(ship):
            print(step)
        ship = ShipProblem(grid=ship.grid, offloads=ship.offloads)
        print(f"Nodes expanded {nodes_expanded}")

main()