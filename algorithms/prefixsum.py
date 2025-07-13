# data structures in arrays
#find the sum of numbers from index range 3 to 6
numbers=[2,8,9,11,12,26,27]
#generating prefix sum

sums=[0]*(len(numbers)+1)
print(sums)
for i in  range(len(numbers)):
    sums[i+1]=sums[i]+numbers[i]
print(sums)    
rangesum=sums[6]-sums[3]
print(rangesum)