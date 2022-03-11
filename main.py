from ast import operator
import queue
from problem import *

def a_star(problem: ShipProblem):
    node_queue = queue.PriorityQueue()

    # initial ShipNode has distance cost of 0, initial problem state, and no parent state
    initial_ship_node = ShipNode(distance_cost = 0, ship_state = problem.initial_state)

    # append a list containing the function cost and initial ShipNode 
    node_queue.put(append_cost(initial_ship_node))

    while (1):
        if (node_queue.empty()):
            print("no solution: SIFT?")
            return -1
        else: 
            # get and pop list on top of queue
            top_node = node_queue.get()
            # get ShipNode from the list
            top_ship_node = top_node[1]

            # check if ship is balanced
            if (is_balanced(top_ship_node.ship_state)):
                return top_ship_node
            else:
                enqueue_nodes(queue = node_queue, ship_nodes = expand_node(top_node))
    return

# Purpose: attach a function cost to a ShipNode that the queue can sort by
# returns a list containing the function cost and the ShipNode
def append_cost(ship_node : ShipNode):
    gn = ship_node.distance_cost

    # check if the ShipNode is the initial ShipNode, initial ShipNode doesn't need a hn
    if (gn == 0): return [gn, ship_node]

    hn = heuristic_cost(ship_node.ship_state)
    return [gn + hn, ship_node]


# Purpose: takes in a ship state from ShipNode and returns the heuristic cost
def heuristic_cost(ship_state):
    return 1

# Purpose: takes in a ship state from ShipNode and returns if the ship is balanced
def is_balanced(ship_state):
    return 

# Purpose: takes in a new list of ShipNodes
def enqueue_nodes(queue, ship_nodes):
    for ship_node in ship_nodes:
        queue.put(append_cost(ship_node))

# Purpose: takes in a ShipNode and "expands it," returning new, valid ship states.  
# returns a list of ShipNodes with new ship states derived from the passed in ShipNode
# return value is passed into enqueueNodes()
def expand_node(ship_node : ShipNode):
    # list that holds generated ShipNodes
    new_ship_nodes = []

    # list of operations to generate new ship states
    operations = []

    # each operation on ship state returns a new ship state
    for operation in operations:
        new_ship_state = operation(ship_node.ship_state)
        # TODO: Compare if new_ship_state is the same as parent_ship_state, if not, append to new_ship_nodes
        # TODO: Change how much the distance_cost is incremented
        new_ship_nodes.append(ShipNode(distance_cost = ship_node.distance_cost + 1, ship_state = new_ship_state, parent_ship_state = ship_node))

    return new_ship_nodes

def main():
    problem = ShipProblem()
    a_star(problem)

main()