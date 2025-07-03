# # #get input of how many days temperature we need


# # no_of_days=int(input("Enter the number of days you need to calculate: "))
# # temperatures=[]
# # for i in range(1,no_of_days+1):
# #     temp=float(input(f"Enter day{i}'s highest recorder temperature: "))
# #     temperatures.append(temp)

# # average_temp=round(sum(temperatures)/len(temperatures))#round functions rounds the float value 
# # print(average_temp)


# # def max_product(arr):
# #     maxi=0
# #     for i in range(len(arr)):
# #         for j in range(i+1,len(arr)):
# #             new_max=arr[i]*arr[j]
# #             if new_max>maxi:
# #                 maxi=new_max
# #     return maxi
        

# # arr = [11, 7, 3, 40, 9, 10] 
# # print(max_product(arr))

# # def middle(lst):
# #     new_lst=[]
# #     for i in range(1,len(lst)-1):
# #         new_lst.append(lst[i])
        
# #     return new_lst

# # myList = [1,1, 2, 3, 4,4]
# # print(middle(myList))  # [2,3]
    


# def first_second(my_list):
#     first=0
#     second=0
#     for i in range(len(my_list)):
#         if my_list[i]>first:
#             first=my_list[i]
            
#     my_list.remove(first)
#     for i in range(len(my_list)):
#         if my_list[i]>second:
#             if first!=my_list[i]:
#                 second=my_list[i]
    
            
#     return first,second

# myList = [84,85,86,87,85,90,90,85,83,23,45,84,1,2,0]
# print(first_second(myList))


# def remove_duplicates(arr):
#     seen=set()
#     result=[]
#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#     return result

# print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))