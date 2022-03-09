
def parse(userFile):
    condensedManifest = []

    with open("data/" + userFile, "r") as openFile:
        
        for i, line in enumerate(openFile): 
            cleanLine = line.strip().split(", ")

            # don't swap x and y coordinate positions
            y_coord = cleanLine[0][4:-1]
            x_coord = cleanLine[0][1:3]

            # remove brackets from weight and convert to int
            cleanLine[1] = int(cleanLine[1][1:-1])

            # skip over empty slots
            if cleanLine[2] == 'UNUSED': 
                continue

            # name of container is the "text" without the brackets
            name = ""
            bracket_index = cleanLine[2].find('(')
            if bracket_index != -1:
                name = cleanLine[2][0:bracket_index]
            else:
                name = cleanLine[2]

            container = {
                "coordinate": [],
                "weight": 0,
                "text": "",
                "name": "",
            }
            
            container["coordinate"] = [x_coord, y_coord]
            container["weight"] = cleanLine[1]
            container["text"] = cleanLine[2]
            container["name"] = name

            condensedManifest.append(container)

    return condensedManifest