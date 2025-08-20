# find the repeated integer

nums=[1,2,3,4,6,5]
dup_check={}

def duplicate_num(nums):
    for i in nums:
        if i in dup_check:
            return True
        else:
            dup_check[i] = 1

    return False

print(duplicate_num(nums))