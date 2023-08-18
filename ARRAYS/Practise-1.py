# # Exercise-1 :
        # We want to check if the array of numbers is containing the negative number, we count it.
        # We print:
        # -	Number of negative of negative number if we found,
        # -	Otherwise print -1
# 
# def countNegNum(Arrayofnumber):
#     count= 0
#     for i in range(len(Arrayofnumber)):
#         if Arrayofnumber[i] < 0:
#             count += 1
#     if count == 0:
#         return -1
#     else :
#         return count
# n = eval(input())
# print(countNegNum(n))



# Exercise-2 :
        # We want to find the index of the minimum number.
# 
# def getIndexMinNumber(array):
#     res = array[0]
#     for i in range(len(array)):
#         if res < array[i] :
#             res = array[i]
#             index = i
#     return index
# MyArray = eval(input("Enter here :"))
# print(getIndexMinNumber(MyArray))



# Exercise-2.1 :
        # We need to find the minimum number first,
        # then we need to find the index of that minimum number.
        # we have an empty array,we return None.
# 
# def getIndexMinNumber(array):
#     if len(array) > 0:
#         res = array[0]
#         index = 0
#         for i in range(len(array)):
#             if res > array[i]:
#                 res = array[i]
#                 index = i
#         return index
# MyArray = eval(input("Enter here :"))
# print(getIndexMinNumber(MyArray))



# Exercise-3 :
        # find Index of first number 5 in array.
# 
# def getIndexOfNumberFive(array):
#     if len(array) > 0:
#         isFive = False
#         i = 0
#         while i < len(array) and not isFive:
#             if array[i] == 5:
#                 index = i
#                 isFive = True
#             i += 1
#         if isFive:
#             return index
# MyArray = eval(input("Enter here :"))
# print(getIndexOfNumberFive(MyArray))



# Exercise-4 :
