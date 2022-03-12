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




