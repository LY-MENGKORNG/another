# def findIndexOfSeven(array):
#     cut = 0
#     for i in range(len(array) - cut):
#         if array[i] == 7 :
#             array.pop(i)
#             cut = 2
#     return array
# Array = eval(input())
# print(findIndexOfSeven(Array))


# def checkList(array):
#     res = False
#     i = 0
#     while i < len(array) and not res:
#         if array[i] > 10 and array[i] < 16:
#             res = True
#     return res
# num = eval(input())
# print(checkList(num))




def listofName(Name,Addname,Index):
    Name.pop(Index)
    Name.append(Addname)
    return Name
name = eval(input())
addName = input()
index = int(input())
print(listofName(name,addName,index))



# def addCharacter(array):
#     res = array.sort()
#     return res
# text = eval(input())
# print(addCharacter(text))



# def sortCharacter(array):
#     res1 = ""
#     finalResult = ""
#     isfound = False
#     if array != [] :
#         for i in range(len(array)):
#             res1 += array[i]
#             res2 =  sorted(res1)
#         res3 = res2[0]
#         for i in range(len(res2)):
#             if res3 != res2[i] or not isfound:
#                 finalResult += res2[i]
#                 res3 = res2[i]
#                 isfound = True
#     return sorted(finalResult)
# text = eval(input())
# print(sortCharacter(text))