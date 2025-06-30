def numbers(num):
    biggestnumber=num[0]
    for i in range(1,len(num)):
        if num[i]>=biggestnumber:
            biggestnumber=num[i]
    return biggestnumber

            
print(numbers([1,26,333,44]))