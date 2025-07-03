# def pair_sum(myList, sum):
#     count=0
#     pair=[]
#     for i in range(len(myList)):
#         for j in range(i+1,len(myList)):
#             count=myList[i]+myList[j]
#             if count==sum:
#                 pair.append(f'{myList[i]}+{myList[j]}')
#     return pair
# print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))



# def contains_duplicate(nums):
#     duplicate=False
#     for i in range(len(nums)):
#         if nums[i] in nums[i+1:]:
#             duplicate=True
#     return duplicate

# num = [1,2,3,4,5]
# print(contains_duplicate(num))

# def permutation(list1,list2):
#     if len(list1)!=len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     print(list1,list2)
#     if list1==list2:
#         return True
#     else:
#         return False
    
# print(permutation(['acb'],['cab']))


# listt=[75,4,3,3,2]
# listt.sort()

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def rotate(matrix):
    n=len(matrix)
    #transpose
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    print(matrix)
    for row in matrix:
        row.reverse()
    return matrix

print(rotate(matrix))