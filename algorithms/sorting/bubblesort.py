numbers = [94, 3, 4, 5, 2, 6, 21]
for i in range(1,len(numbers)):#number of times needed to loop to sort
    for j in range(0,len(numbers)-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

print(i)
print(numbers)

        