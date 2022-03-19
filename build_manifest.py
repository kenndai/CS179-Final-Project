from problem import ShipProblem

def build_manifest(filename, ship : ShipProblem):
    container_lookup = {}
    for container in ship.grid:
        container_lookup[f'{container["coordinate"][0]}{container["coordinate"][1]}'] = container

    openfile = open(filename, "w")

    for y in range(1, 9):
        for x in range(1, 13):
            if container_lookup.get(f"{y}{x}"):
                container = container_lookup[f"{y}{x}"]
                openfile.write(f'[{prepend_zero_coord(y)},{prepend_zero_coord(x)}], {{{prepend_zero_weight(container["weight"])}}}, {container["text"]}\n')
            else:
                openfile.write(f"[{prepend_zero_coord(y)},{prepend_zero_coord(x)}], {{00000}}, NAN\n")
    openfile.truncate()

    return

def prepend_zero_coord(coord):
    if coord < 10: return '0' + str(coord)
    else: return str(coord)

def prepend_zero_weight(weight):
    if len(str(weight)) == 1: 
        return '0000' + str(weight)
    elif len(str(weight)) == 2: 
        return '000' + str(weight)
    elif len(str(weight)) == 3: 
        return '00' + str(weight)
    elif len(str(weight)) == 4: 
        return '0' + str(weight)
    else: 
        return str(weight)


def main():
    ship = ShipProblem(grid=[{'coordinate': [1, 1], 'weight': 0, 'text': 'NAN'}, {'coordinate': [1, 2], 'weight': 0, 'text': 'NAN'}, {'coordinate': [1, 4], 'weight': 4000, 'text': 'John Deere Parts (call Sue at Ohio office)'}, {'coordinate': [1, 6], 'weight': 6000, 'text': 'John Deere Parts (call Sue at Ohio office)'}, {'coordinate': [2, 1], 'weight': 3000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}, {'coordinate': [2, 6], 'weight': 1000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}, {'coordinate': [3, 1], 'weight': 5000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}, {'coordinate': [2, 4], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}, {'coordinate': [1, 3], 'weight': 2000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}, {'coordinate': [2, 2], 'weight': 7000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}])
    build_manifest("OUTBOUND.txt", ship = ship)

main()