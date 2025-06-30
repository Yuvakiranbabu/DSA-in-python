F1_drivers=['lando','max','charles','hamilton','george']

print(F1_drivers)
F1_drivers[-1]='kimi antonelli'
print(F1_drivers)

F1_drivers.insert(3,'daniel ricciardo')#can insert element at any position
print(F1_drivers)

F1_drivers.append('carlos sainz')#used to insert element at end
print(F1_drivers)

rookie_drivers=['lawson','bortoleto','alonso']
F1_drivers.extend(rookie_drivers)#used to append a list to a list
print(F1_drivers)
