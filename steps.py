from a_star import *
def main():
    condensed_manifest = [
                        {'coordinate': ['01', '01'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['01', '02'], 'weight': 6000, 'text': 'TEst1'}, 
                        {'coordinate': ['01', '04'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['02', '04'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['03', '04'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['04', '04'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['05', '04'], 'weight': 0, 'text': 'NAN'}, 
                        {'coordinate': ['01', '06'], 'weight': 6000, 'text': 'TEst2'}, 
                        {'coordinate': ['02', '06'], 'weight': 6000, 'text': 'TEst3'}, 
                        {'coordinate': ['03', '06'], 'weight': 6000, 'text': 'TEst4'}, 
                        ]

    ship = ShipProblem(grid=condensed_manifest)
    steps = get_steps(a_star(ship))

    for step in steps:
        if step == "Start": continue
        # print(f'Move {step["name"]} at {step["orig"]} to {step["new"]} Minutes: {step["minutes"]}')
        print(step)
    
main()