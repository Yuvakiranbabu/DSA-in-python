#time complexity big O(n^2)
def print_numbers(n):
    for i in range(n):
        for j in range(n):
                for k in range(n):
                    print (i,j,k)

    
print_numbers(3)

#O(log n) example of this is binary search this reduces the data by 50% everytime we go through the algortihm