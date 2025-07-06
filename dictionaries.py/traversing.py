formula1_drivers={
    "mclaren 1":"lando norris",
    "mclaren 2":"oscar piastri",
    "ferrari 1":"charles leclerc",
    "ferrari 2":"lewis hamilton"
}

def traverse_dict(dict):
    for key in dict:
        print(f'{key} - {dict[key]}')

traverse_dict(formula1_drivers)