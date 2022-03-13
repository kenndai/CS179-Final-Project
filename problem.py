# class ShipNode:
#     __slots__ = ["distance_cost", "ship_grid", "parent_ship_grid"]

#     def __init__(self, distance_cost, ship_grid, parent_ship_grid = None):
#         self.distance_cost = distance_cost
#         self.ship_grid = ship_grid
#         self.parent_ship_grid = parent_ship_grid
import copy

from sqlalchemy import column
class ShipProblem:

    __slots__ = ["grid", "parent", "distance_cost", "top_containers"]

    def __init__(self, distance_cost = 0, grid = None, parent = None):
        self.distance_cost = distance_cost
        # self.grid = grid
        self.grid = [
            {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '02'], 'weight': 0, 'text': 'NAN'}, 
            {'coordinate': ['01', '06'], 'weight': 2500, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
            {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['02', '06'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['03', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['02', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
            {'coordinate': ['05', '01'], 'weight': 99999, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}]
        self.parent = parent

        self.top_containers = self.set_top_containers()

    ## finds and sets the top containers for all columns
    def set_top_containers(self):
        ship_grid = self.grid
        top_containers = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None
        }

        for container in ship_grid:
            curr_x = int(container["coordinate"][1])
            curr_y = int(container["coordinate"][0])

            top_x_container = top_containers[curr_x] 
            if top_containers[curr_x] == None or curr_y > int(top_x_container["coordinate"][0]):
                top_containers[curr_x] = container

        return top_containers

    ## position crane over a column and expand
    ## returns a list of grids
    # TODO: Return the manhattan distance
    def move_crane(self, column_num):
        new_grids = []

        # return if top container in a column is an unused slot or "NAN" container 
        if self.top_containers[column_num] == None or self.top_containers[column_num]["text"] == "NAN": 
            print("no container to grab")
            return [[]]

        # get the top container in the first column
        top_container = self.top_containers[column_num]
        # find the index of the container in the grid
        index_in_grid = self.grid.index(top_container)

        for i in range(1, 7):
            # skip the column you're moving away from
            if i == column_num: continue

            # makes a deepcopy of list, i hate python
            new_grid = copy.deepcopy(self.grid)

            # get top container of the i-th column
            i_top_container = self.top_containers[i]

            # place container in the first row of the i-th column
            if i_top_container == None:
                new_grid[index_in_grid]["coordinate"] = [1, i]
            # place container one higher than the top container in the i-th column
            else: 
                y_coord = int(i_top_container["coordinate"][0])
                new_grid[index_in_grid]["coordinate"] = [y_coord + 1, i]    
            
            new_grids.append(new_grid)
        return new_grids

problem2 = ShipProblem()

# for container in problem2.top_containers.values():
#     print(container)

for grid in problem2.move_crane(6):
    for container in grid:
        print(container)
    print()