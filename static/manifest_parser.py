userFile = "CunardBlue.txt"

def parse(userFile):
    condensedManifest = []

    with open(userFile, "r") as openFile:
        
        for i, line in enumerate(openFile): 
            cleanLine = line.strip().split(", ")

            # swap x and y coordinate positions
            x_coord = int(cleanLine[0][4:-1]) - 1
            y_coord = int(cleanLine[0][1:3]) - 1

            # remove brackets from weight and convert to int
            cleanLine[1] = int(cleanLine[1][1:-1])

            # skip over empty slots
            if cleanLine[2] == 'UNUSED': 
                continue

            container = {
                "xy-coordinate": [],
                "weight": 0,
                "text": "",

            }
            container["xy-coordinate"] = [x_coord, y_coord]
            container["weight"] = cleanLine[1]
            container["text"] = cleanLine[2]
            condensedManifest.append(container)

    return condensedManifest
for container in parse(userFile):
    print(container)