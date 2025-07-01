podium='lando norris'
f1_drivers=['lando norris','max verstappen','george','hamilton','oscar','leclerc']
'''
if podium in f1_drivers:
    print(f"{podium} is on the podium")
print(f"{podium} is not on the podium")
'''
# linear search function

def linear_search(list,winner):
    for name in list:
        if name == winner:
            return(f"{winner} is on the podium")
        else:
            return (f"{winner} is not on the podium")

print(linear_search(f1_drivers,podium))


