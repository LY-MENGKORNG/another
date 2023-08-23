# Exercise-1 :
# def isEqual(array1,array2):
#     if len(array1) == len(array2) :
#         Equal = True
#         res = "EQUAL"
#         i = 0
#         while i < len(array1) and Equal:
#             if array1[i] != array2[i] :
#                 Equal = False
#                 res = "NOT EQUAL"
#             i += 1
#         return res
#     else :
#         res = "NOT EQUAL"
#     return res
# text1 = eval(input())
# text2 = eval(input())
# print(isEqual(text1,text2))


# EXERCICE-2 :
def numberOfCompare(array):
    sum = 0
    if len(array) > 0:
        for i in range(len(array) - 1):
            if array[i] < array[i+1]:
                sum += 1
        return sum
    else :
        return 0
Array = eval(input("Enter here :"))
print(numberOfCompare(Array))



# EXERCICE-3 :
# def sum(n1,n2):
#     return n1 + n2
# def sumFromTo(between):
#     if len(between) == 2:
#         total = 0
#         if between[0] <= between[1] :
#             while between[0] <= between[1]:
#                 total = sum(between[0],total)
#                 between[0] += 1
#             return total
#         else :
#             return total
#     else:
#         return "You got Error!"
# MyNumber = eval(input("Enter :"))
# print(sumFromTo(MyNumber))



# EXERCICE-4 :
# def sum(afterfound,next):
#     return afterfound + next
# def sumBetweenNumberTwo(array):
#     total = 0
#     isfound = False
#     for i in range(len(array)):
#         if array[i] != 2 and isfound :
#             total = sum(array[i],total)
#         elif array[i] == 2 and not isfound:
#             isfound = True
#         else :
#             isfound = False
#     return total
# Myarray = eval(input("Enter :"))
# print(sumBetweenNumberTwo(Myarray))