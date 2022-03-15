from a_star import *
def main():
    condensed_manifest = [
                        {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['01', '02'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['02', '02'], 'weight': 4000, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
                        {'coordinate': ['01', '06'], 'weight': 6000, 'text': 'John Deere Parts (call Sue at Ohio office)'}, 
                        {'coordinate': ['02', '01'], 'weight': 3000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
                        {'coordinate': ['02', '06'], 'weight': 1000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
                        {'coordinate': ['03', '01'], 'weight': 4000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
                        {'coordinate': ['04', '01'], 'weight': 6000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
                        {'coordinate': ['01', '03'], 'weight': 3000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'},
                        {'coordinate': ['05', '01'], 'weight': 1000, 'text': 'John Deere Oversized Tires(call Sue at Ohio office)'}]


    ship = ShipProblem(grid=condensed_manifest)
    steps = get_steps(a_star(ship))

    for step in steps:
        if step == "Start": continue
        print(f'Move {step["name"]} at {step["orig"]} to {step["new"]}')
    
main()