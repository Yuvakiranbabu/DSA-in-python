F1_drivers=['lando','max','charles','hamilton','george']

#del F1_drivers[2]
#print(F1_drivers)

#slicing
'''
print(F1_drivers[0:])
print(F1_drivers[:5])
print(F1_drivers[0:5:2])

print(F1_drivers.pop(3))#using pop we can store the deleted item
print(F1_drivers)


#we can delete multiply items from list using del and slicing
del F1_drivers[0:2]
print(F1_drivers)
'''
#we can use remove function when the know the element itself no need for index

F1_drivers.remove("george")
print(F1_drivers)