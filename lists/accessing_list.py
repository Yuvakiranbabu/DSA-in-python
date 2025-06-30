#accessing and traversing a list 
F1_drivers=['lando','max','charles','hamilton','george']

#print(F1_drivers[0])#accessing a single element using index

print('oscar' in F1_drivers)#use "in" to check if element is present in list returns boolean value

#print(F1_drivers[-1])# gives the last element as output


'''using loop to traverse through the list'''

for i in F1_drivers:
    print(i)

for i in range(len(F1_drivers)):
    F1_drivers[i]=F1_drivers[i]+" checkered flag"
    print(F1_drivers[i])

