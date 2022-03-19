from calendar import c
import copy
from json import loads
class ShipProblem:

    __slots__ = ["distance_cost", "function_cost", "grid", "last_column", "mass", "top_containers", "parent", "change",
                 "loads", "offloads"]

    def __init__(self, distance_cost = 0, grid = None, mass = 0, last_column = 0, parent=None, change="Start", loads = [], offloads = []):
        self.distance_cost = distance_cost
        self.function_cost = 0
        self.grid = self.int_coords(grid)
        self.mass = self.calculate_mass(mass)
        self.last_column = last_column
        self.parent = parent
        self.change = change
        self.loads = self.int_coords(loads)
        self.offloads = self.int_coords(offloads)
        self.top_containers = self.set_top_containers()

    def __lt__(self, other):
        return self.function_cost < other.function_cost

    def calculate_mass(self, mass):
        # if a mass was passed in, assign that mass
        if mass != 0: return mass 

        # sum up weight of all containers
        calculated_mass = 0
        for container in self.grid:
            calculated_mass += container["weight"]
        return calculated_mass

    def int_coords(self, containers):
        if containers == []:
            return containers
        if isinstance(containers[0]["coordinate"][0], int) and isinstance(containers[0]["coordinate"][1], int):
            return containers

        for container in containers:
            container["coordinate"][0] = int(container["coordinate"][0]) 
            container["coordinate"][1] = int(container["coordinate"][1]) 
        return containers

    ## finds and sets the top containers for all columns
    def set_top_containers(self):
        ship_grid = self.grid

        top_containers = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
            10: None,
            11: None,
            12: None,
        }

        for container in ship_grid:
            curr_y = container["coordinate"][0]
            curr_x = container["coordinate"][1]

            top_x_container = top_containers[curr_x] 
            if top_containers[curr_x] == None or curr_y > top_x_container["coordinate"][0]:
                top_containers[curr_x] = container

        return top_containers

    ## position crane over a column and expand
    ## returns a list of ShipProblem instances
    def move_crane(self, column_num, mode = None):
        # dont expand a column where you last placed a container, redundant
        if column_num == self.last_column: 
            return [[]]

        # return if top container in a column is an unused slot or "NAN" container 
        if self.top_containers[column_num] == None or self.top_containers[column_num]["text"] == "NAN": 
            # print("no container to grab")
            return [[]]

        new_ships = []

        # get the top container in the desired column
        top_container = self.top_containers[column_num]
        top_y_coord = top_container["coordinate"][0]
        top_x_coord = top_container["coordinate"][1]

        if mode == "offload":
            top_coords = [top_y_coord, top_x_coord]
            for index, container in enumerate(self.offloads):
                if top_coords == container["coordinate"]:
                    new_grid = copy.deepcopy(self.grid)
                    new_offloads = copy.deepcopy(self.offloads)

                    new_grid.pop(new_grid.index(container))
                    new_offloads.pop(index)

                    change = {
                        "name" : top_container["text"],
                        "orig" : [top_y_coord, top_x_coord],
                        "new" : "TRUCK",
                        "minutes": 8 - top_y_coord + 2
                    }

                    return [ShipProblem(grid=new_grid, mass=self.mass-container["weight"], parent=self, loads=self.loads, offloads=new_offloads, change=change)]

        # find the index of the container in the grid
        index_in_grid = self.grid.index(top_container)

        for i in range(1, 13):
            # skip the column you're moving away from
            if i == column_num: continue

            # get top container of the i-th column
            ith_top_container = self.top_containers[i]

            # makes a deepcopy of the ship's grid that will be modified, i hate python
            new_grid = copy.deepcopy(self.grid)

            if ith_top_container == None: 
                new_y_coord = 1
            elif ith_top_container["coordinate"][0] == 10:
                continue
            else: 
                new_y_coord = ith_top_container["coordinate"][0] + 1
            
            # assigns new coordinate: 
            # y is either 1 or 1 higher than the highest
            # x is i
            new_grid[index_in_grid]["coordinate"] = [new_y_coord, i]


            # get the highest container between current column and target column
            manhattan_distance = 0
            highest_between = self.get_highest_between(self.top_containers, column_num, i)
            if highest_between == None:
                manhattan_distance += self.manhattan_distance([top_y_coord, top_x_coord], [new_y_coord, i])
            else:
                y_between = highest_between["coordinate"][0]
                x_between = highest_between["coordinate"][1]
                manhattan_distance += self.manhattan_distance([top_y_coord, top_x_coord], [y_between + 1, x_between])
                manhattan_distance += self.manhattan_distance([y_between + 1, x_between], [new_y_coord, i])

            change = {
                "name" : top_container["text"],
                "orig" : [top_y_coord, top_x_coord],
                "new" : new_grid[index_in_grid]["coordinate"],
                "minutes": manhattan_distance
            }

            new_ships.append(ShipProblem(distance_cost = self.distance_cost + manhattan_distance, grid = new_grid, 
                                         mass = self.mass, last_column = i, parent = self, change = change,
                                         loads = self.loads, offloads = self.offloads))

        return new_ships

    ## calculate the total amount of containers on top of the containers you want to unload
    ## try not to add to the total amount of containers on top if possible
    # expand the columns of containers we want to unload, choose cheapest, done with queue 

    def load_container(self, container):
        return

    def offload_container(self, container):
        return

    # returns the highest container between two columns
    # start_column is column_num and end_column = i
    def get_highest_between(self, top_containers, start_column, end_column):
        if abs(start_column - end_column) <= 1: 
            return None

        highest_between = None
        highest_y_between = 0

        min_column = min(start_column, end_column)
        max_column = max(start_column, end_column)

        for key in range(min_column + 1, max_column):
            container = top_containers[key]
            if container == None: continue
            curr_y = container["coordinate"][0]
            if curr_y > highest_y_between:
                highest_y_between = curr_y
                highest_between = container

        return highest_between

    def manhattan_distance(self, coordinate1, coordinate2):
        return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])

