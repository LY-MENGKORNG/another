# Exercise-1 :
# def sum(n1,n2):
#     return ":" + str(n1 + n2)
# def countCharacter(text):
#     a = 0
#     b = 0
#     c = 0 
#     d = 0
#     for i in range(len(text)):
#         if text[i] == 'a':
#             a += 1
#         elif text[i] == 'b':
#             b += 1
#         elif text[i] == 'c':
#             c += 1
#         elif text[i] == 'd':
#             d += 1
#     return "a:" + str(a) + "\n" + "b:" + str(b) + "\n" + "c:" + str(c) + "\n" + "d:" + str(d)
# Text = input()
# print(countCharacter(Text))



# Exercise- 2:
# def power(number1,number2):
#     res = 1
#     for i in range(number2):
#         res *= number1
#     return res
# first = int(input())
# second = int(input())
# print(power(first,second))



# Exercise-3 :
# def reverse(string):
#     res = ""
#     for i in range(len(string)):
#         res += string[len(string) - (i + 1)]
#     return res
# text = input()
# print(reverse(text))



# Exercise-4 :
# def Multiply(n1,n2):
#     return n1*n2
# def proccess(first,end):
#     total = 1
#     if first > end:
#         return 0
#     else :
#         while first <= end:
#             total = Multiply(total,first)
#             first += 1
#         return total
# First = int(input())
# End = int(input())
# print(proccess(First,End))



# Exercise-5 :
# def cotainsOneA(string):
#     isA = "HAS-NOT-A"
#     i = 0
#     isfound = False
#     while i < len(string) and not isfound:
#         if string[i].lower() == 'a':
#             isA = "HAS-A"
#             isfound = True
#         i += 1
#     return isA
# text = input()
# print(cotainsOneA(text))



# Exercise-6 :
# def sum(num1,num2):
#     return num1 + num2
# n1 = int(input())
# n2 = int(input())
# print(sum(n1,n2))



# Exercise-7 :
# def isValueInRange(value,min,max):
#     if value >= min and value <= max:
#         return "CORRECT"
#     else:
#         return "ERROR"
# Value = int(input())
# Min = int(input())
# Max = int(input())
# print(isValueInRange(Value,Min,Max))



# Exercise-8 :
# def cotains(word,Character,Character2):
#     res = 0
#     for i in range(len(word)):
#         if word[i].upper() == Character.upper() :
#             res += 1
#         elif word[i].upper() == Character2.upper():
#             res += 1
#     if res == 1:
#         return "VALID"
#     else:
#         return "NOT VALID"
# Word = input()
# Character = input()
# Character2 = input()
# print(cotains(Word,Character,Character2))



# Exercise-9 :
