import copy
class ShipProblem:

    __slots__ = ["distance_cost", "function_cost", "grid", "last_column", "top_containers"]

    def __init__(self, distance_cost = 0, grid = None, last_column = 0):
        self.distance_cost = distance_cost
        self.function_cost = 0
        self.grid = grid
        self.last_column = last_column

        self.top_containers = self.set_top_containers()

    def __lt__(self, other):
        return self.function_cost < other.function_cost

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
            curr_y = int(container["coordinate"][0])
            curr_x = int(container["coordinate"][1])

            top_x_container = top_containers[curr_x] 
            if top_containers[curr_x] == None or curr_y > int(top_x_container["coordinate"][0]):
                top_containers[curr_x] = container

        return top_containers

    ## position crane over a column and expand
    ## returns a list of ShipProblem instances
    def move_crane(self, column_num):
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
        top_y_coord = int(top_container["coordinate"][0])
        top_x_coord = int(top_container["coordinate"][1])

        # find the index of the container in the grid
        index_in_grid = self.grid.index(top_container)

        for i in range(1, 7):
            # skip the column you're moving away from
            if i == column_num: continue

            # makes a deepcopy of the ship's grid that will be modified, i hate python
            new_grid = copy.deepcopy(self.grid)

            # get top container of the i-th column
            i_top_container = self.top_containers[i]

            # place container in the first row of the i-th column
            if i_top_container == None:
                new_grid[index_in_grid]["coordinate"] = [1, i]
                manhattan_distance = abs(top_y_coord - 1) + abs(top_x_coord - i)
            # place container one higher than the top container in the i-th column
            else: 
                new_y_coord = int(i_top_container["coordinate"][0]) + 1
                new_grid[index_in_grid]["coordinate"] = [new_y_coord, i]    
                manhattan_distance = abs(top_y_coord - new_y_coord) + abs(top_x_coord - i)

            new_ships.append(ShipProblem(distance_cost = self.distance_cost + manhattan_distance, grid = new_grid, last_column = i))
        return new_ships