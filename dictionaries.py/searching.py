formula1_drivers={
    "mclaren 1":"lando norris",
    "mclaren 2":"oscar piastri",
    "ferrari 1":"charles leclerc",
    "ferrari 2":"lewis hamilton",
    "red bull":"max verstappen"
}

def search(dict,value):
    for key in dict:
        if dict[key]==value:
            return key, value
        
    return 'this driver is not in the dictionary'

print(search(formula1_drivers,"max verstappen"))