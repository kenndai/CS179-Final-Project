class Node:
    def __init__(self, coordinate, name=None, text=None, weight=None):
        self.coordinate = coordinate
        self.name = name
        self.text = text
        self.weight = weight

class Ship:
    def __init__(self):
        self.grid = []
        self.makeGrid()

    def makeGrid(self):
        self.grid = []
        for i in range(10):
            row = []
            for j in range(12):
                row.append(Node([i, j]))
            self.grid.append(row)
                
    def makeBufferGrid():
        return 0

    def fillGrid(self, manifest):
        for element in manifest:
            x_coord = int(element["coordinate"][0]) - 1
            y_coord = int(element["coordinate"][1]) - 1
            self.grid[x_coord][y_coord].name = element["name"]
            self.grid[x_coord][y_coord].text = element["text"]
            self.grid[x_coord][y_coord].weight = element["weight"]

    def balance(self):
        if not self.checkIfBalance():
            return True
        else:
            return False

    def checkIfBalance(self):
        left_sum = 0
        right_sum = 0
        for i in range(10):
            for j in range(12):
                if j < 6:
                    left_sum += self.grid[i][j]
                else:
                    right_sum += self.grid[i][j]
        #check if left or right sum are not 0, cannot divide by 0, return -1 if so
        if left_sum == 0 and right_sum == 0:
            return True
        elif left_sum == 0 and right_sum != 0:
            return -1
        elif left_sum != 0 and right_sum == 0:
            return -1
        else:
            num = left_sum/right_sum
            if num >= .9 or num <= .1:
                return True
            else:
                return False




