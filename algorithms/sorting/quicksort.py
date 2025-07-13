import random

def quicksort(numbers):
    if len(numbers)<=1:
        return numbers
    
    pivot=random.choice(numbers)
    left=[i for i in numbers if i<pivot]  #list comprehension
    right=[i for i in numbers if i>pivot]
    middle=[i for i in numbers if i==pivot]


    # for i in range(len(numbers)):
    #     if numbers[i]<pivot:
    #         left.append(numbers[i])

    # for i in range(len(numbers)):
    #     if numbers[i]>pivot:
    #         right.append(numbers[i])

    # for i in range(len(numbers)):
    #     if numbers[i]==pivot:
    #         middle.append(numbers[i])

    return quicksort(left)+middle+quicksort(right)


numbers = [94, 3, 4, 5, 2, 6, 21]
print(quicksort(numbers))

