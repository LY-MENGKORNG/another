# Question - 1
    # [ARRAY] Sum Values In Array
# 
# def sum(array1,array2):
#     res1 = 0
#     res2 = 0
#     for i in range(len(array1)):
#         res1 += array1[i]
#     for i in range(len(array2)):
#         res2 += array2[i]
#     return str(res1) + "\n" + str(res2)
# Array1 = eval(input())
# Array2 = eval(input())
# print(sum(Array1,Array2))



# Question - 2
    # [ARRAY] Number of Times 8 Apears in Array
# 
# def numberOfEight(array):
#     res = 0
#     for i in range(len(array)):
#         if array[i] == 8:
#             res += 1
#     if res == 0:
#         res = -1
#     return res
# Array = eval(input())
# print(numberOfEight(Array))



# Question - 3
    # [ARRAY] Find Item in Array at given index
# 
# def FindArray(array):
#     Index = 0
#     for i in range(len(array)):
#         if array[i] == "rady":
#             Index = i
#     return Index
# Array = ["ronan","rady","PNC"]
# print(FindArray(Array))



# Question - 4
    # [ARRAY] Count Even and Odd Numbers In Array
# 
# def EvenandOdd(array):
#     even = 0
#     odd =0
#     for i in range(len(array)):
#         if int(array[i]) % 2 == 0:
#             even += 1
#         elif (array[i]) % 2 != 0:
#             odd += 1
#     return "EVEN:" + str(even) + "\n" + "ODD:" + str(odd)
# Array = eval(input())
# print(EvenandOdd(Array))



# Question - 4.1
    # [ARRAY] Count Even Numbers In Array
# 
def countEven(array):
    evenNumber = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            evenNumber += 1
    return evenNumber
Array = eval(input())
print(countEven(Array))