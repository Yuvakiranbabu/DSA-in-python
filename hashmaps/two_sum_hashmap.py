#two sum using hashmap


#nums = [2, 7, 11, 15], target = 9

storage=
def two_sum(nums,target):
    for index,value in enumerate(nums):
        complement = target - value
        if complement in storage:
            



