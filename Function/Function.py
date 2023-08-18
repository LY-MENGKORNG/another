
# Example 1 :
# def myage(number , age):
#     return (number * number) / age
# print(myage(10 , 5))


# Example 2 :
# def find(string):
#     count =  0
#     for i in range(len(string)):
#         if string[i].lower() == 'a':
#             count += 1
#     return count
# text = input()
# print(find(text))


# Example 3 :
# def maxnumber(string) :
#     big = int(string[0])
#     for i in range(len(string)):
#         if int(string[0]) < int(string[i]) :
#             big = int(string[i])

#     return big
# num = input("Enter :")
# print(maxnumber(num))


# Example 4 :
# def text(string) :
#     print("Hello " + string + "!")
#     print("Good night sweet dreams")
#     print("Good Bye!"+"\n")
# text("mnus")
# text("animal")
# text("god")



# Exercise-6 :
# def removeMinuses(word):
#     res = ""
#     reason = ""
#     i = 0
#     for i in range(len(word)):
#         if word[i] != '-':
#             res += word[i]
#         i += 1
#     return res

# isYes = True
# while isYes:
#     text = input("Enter here :")
#     print("Word without minus :",removeMinuses(text))
#     reason = input("Do you want to continue (Y/N)? :")
#     if reason.lower() == 'n':
#         isYes = False


# Exercise-7 :
# def sum(num1,num2):
#     return num1 + num2
# n1 = int(input("Enter number 1 :"))
# n2 = int(input("Enter number 2 :"))
# print("The sum is :",sum(n1,n2))



# Exercise-8 :
# def sum(n1, n2):
#     return n1 + n2

# numberOfTimes = int(input("Number of times:"))
# result = 0
# for i in range(numberOfTimes):
#     number = int(input("Value " + str(i + 1) + ": "))
#     if i == 0:
#         prevuisValue = number
#     else:
#         prevuisValue = sum(prevuisValue, number)
#     result = prevuisValue
# print(result)



#       Exercise-9 (<---Special--->)
# def sum(n1,n2):
#     return n1 + n2
# def sumFromTo(Start,End):
#     total = 0
#     while Start <= End:
#         total = sum(total,Start)
#         Start += 1
#     return total
# Startnumber = int(input("Start value: "))
# Endnumber = int(input("End value: "))
# print("The sum of numbers between " + str(Startnumber) + " and " + str(Endnumber) + " is: " + str(sumFromTo(Startnumber,Endnumber)))




# Exercise-10 :
# def sum(n1,n2):
#     return n1 + n2
# def numberOfUpperCases(word):
#     res = 0
#     for i in range(len(word)):
#         if word[i].isupper():
#             res = sum(res,1)
#     return res
# text = input("Enter here :")
# print("Number of uppercase letters : " + str(numberOfUpperCases(text)))



# Exercise-11 :
# def getComment(grade):
#     if grade > 10:
#         res = "Good"
#     else :
#         res = "Bad"
#     return res
# num = int(input("Enter :"))
# print(getComment(num))


# Exercise-12 :
        # banana -> 2 $
        # apple  -> 5 $
        # orange -> 1 $
# 
# def getPrice(fruitName):
#     if fruitName == "banana":
#         return 2
#     elif fruitName == "apple":
#         return 5
#     elif fruitName == "orange":
#         return 1
#     else :
#         return "I don't know!"
# text = input("Enter :")
# print(text + " price is:" + str(getPrice(text)) + " $")



# Exercise-13 :
# def getAbsolute(number):
#     if number < 0:
#         res = -1 * number
#     else:
#         res = str(number)
#     return res
# num = int(input("Enter :"))
# print(getAbsolute(num))



# Exercise-14 : 
# 1.create a function to print the message "HELLO WEB2024A"
# example:when we call name function sayHello() it will display "HELLO WEB2024A"
# def sayHello(string):
#     return string
# print(sayHello("HELLO WEB2024C"))


# Exercise-15 :
        # 2.create the function to get the name of student.
        # example:getName("Yon") it will return "I am Yon"
        # 	getName("Rady") it will return "I am Rady"
# def getName(string):
#     return "I am "+ string
# text = input("Enter your name :")
# print(getName(text))


# Exercise-16 :
    # 3.create the function to get the first name and last name
    # example:getFullName("Yon","Yen") it will return "My name is Yon Yen"
    # 	getFullName("Rady","Y") it will return "My name is Rady Y"
# def getFullname(first,last):
#     return first + " " + last
# firstname = input("Enter :")
# Lastname = input("Enter :")
# print(getFullname(firstname,Lastname))



# Exercise-17 :
    # 4.create the function to sum the number.
    # example:sumNumber(2,3) it will return 5
    # example:sumNumber(10,15) it will return 25
# def sumNumber(firstNumber,lastNumber):
#     return firstNumber + lastNumber
# first = int(input("Enter :"))
# last = int(input("Enter :"))
# print("Sum of numbers is" +str(sumNumber(first,last)))



# Exercise-18 :
        # 5.create the function to subtract the number
        # example:substractNumber(15,10) it will return 5
# def substract(number1,number2):
#     return number1 - number2
# firstnumber = int(input("first : "))
# lastnumber = int(input("last : "))
# print(substract(firstnumber,lastnumber))



# Exercise-19 :
        # 6.create the function to multiply the number
        # example:multiplyNumber(4,5) it will return 20
# def multiply(firstnumber,lastnumber):
#     return firstnumber * lastnumber
# first = int(input("Enter first : "))
# last = int(input("Enter last : "))
# print(multiply(first,last))


# Exercise-20 :
        # 7.create the function to divide the number
        # example:divideNumber(10,2) it will return 5
# def divide(firstnumber,lastnumber):
#     return int(firstnumber / lastnumber)
# first = int(input("Enter first : "))
# last = int(input("Enter last : "))
# print(divide(first,last))



# Exercise-21 :
        # 8.create the function to check the condition greater or less than of number
        # example:comparisonNumber(3,1) it will return "3 is greater than 1"
        # 	comparisonNumber(3,4) it will return "3 is less than 4"
# def comparisonNumber(first,last):
#     if first > last :
#         return str(first) + " is greater than " + str(last)
#     elif last > first:
#         return str(first) + " is less than " + str(last)
# firstnumber = int(input("Enter first : "))
# lastnumber = int(input("Enter last : "))
# print(comparisonNumber(firstnumber,lastnumber))



# Exercise-22 :
        # 9.create the function to comparison number
        # example:comparisonNumber(3,1) it will return "3 is greater than 1"
        #     comparisonNumber(3,4) it will return "4 is greater than 3
# def comparisonNumber(first,last):
#     if first > last :
#         return str(first) + " is greater than " + str(last)
#     else:
#         return str(last) + " is greater than " + str(first)
# firstnumber = int(input("Enter first : "))
# lastnumber = int(input("Enter last : "))
# print(comparisonNumber(firstnumber,lastnumber))



# Exercise-23 :
        # 1.How to Remove number From a String in Python
        # Input:yon12rady23him2
        # output:yonradyhim
# def RemoveNumber(string):
#     res = ""
#     for i in range(len(string)):
#         if not string[i].isnumeric():
#             res += string[i]
#     return res
# text = input("Enter here :")
# print(RemoveNumber(text))



# Exercise-24 :
        # 2.Count avoid Spaces in string length
        # input:ab1 dc a
        # output:6
# def avoidSpace(string):
#     count = 0 
#     for i in range(len(string)):
#         if string[i] != " ":
#             count += 1
#     return count
# text = input("Enter here :")
# print(avoidSpace(text))




# Exercise-25 :
        # 3.Uppercase Half String
        # Input : abcd
        # Output : abCD
        # Explanation : Latter half of string is uppercased.
        # Input : abc
        # Output : abC
        # Explanation : Latter half of string is uppercased.
# def Uppercase(string):
#     res = ""
#     HalfString = int(len(string) / 2)
#     equal = False
#     for i in range(len(string)):
#         if i + HalfString < len(string):
#             res += string[i]
#         else :
#             res += string[i].upper()
#     return res
# text = input("Enter here :")
# print(Uppercase(text))



# Exercise-26 :
        # 4.Python program to capitalize the first and
        # last character of each word in a string
        # input:yen yon
        # output:Yen yoN
# def CapitalizE(string):
#     res = ""
#     for i in range(len(string)):
#         if i > 0 and i < len(string) -1 :
#             res += string[i]
#         else :
#             res += string[i].upper()
#     return res
# text = input("Enter here :")
# print(CapitalizE(text))



# Exercise-27 :
        # 5.Python program to check if a string has at least one
        # letter and one number.
        # input: 1abc
        # output: True
        # input:ab
        # output:False
# def check(string):
#     letter = 0
#     number = 0
#     for i in range(len(string)):
#         if string[i].isnumeric():
#             number += 1
#         else :
#             letter += 1
#     if letter > 0 and number > 0 :
#         res = True
#     else :
#         res = False
#     return res
# text = input("Enter here :")
# print(check(text))



# Exercise-28:
        # 6.Python Program to Accept the Strings Which
        # Contains all Vowels
        # Input : geeksforgeeks
        # Output : Not Accepted
        # All vowels except 'a','i','u' are not present

        # Input : ABeeIghiObhkUul
        # Output : Accepted
        # All vowels are present
# def Vowel(string):
#     isA = 0 
#     isE = 0
#     isI = 0
#     isO = 0
#     isU = 0
#     for i in range(len(string)):
#         if  string[i].lower() == 'a':
#             isA = 1
#         elif string[i].lower() == 'e':
#             isE = 1
#         elif string[i].lower() == 'i':
#             isI = 1
#         elif string[i].lower() == 'o':
#             isO = 1
#         elif string[i].lower() == 'u':
#             isU = 1
#     if isA == isE == isI == isO == isU == 1 :
#         return "Accepted"
#     else :
#         return "Not Accepted"
# text = input("Enter here :")
# print(Vowel(text))



# Exercise-29 :
        # 7.Python | Count the Number of matching characters
        # in a pair of string
        # Input : str1 = 'abcdef'
        #         str2 = 'defghia'
        # Output : 4
        # (i.e. matching characters :- a, d, e, f)

        # Input : str1 = 'aabcddekll12@'
        #         str2 = 'bb22ll@55k'
        # Output : 5
        # (i.e. matching characters :- b, 1, 2, @, k)
# def CountMatching(n1,n2):
#     return n1 + n2
# def proccess(string1,string2):
#     total = 0
#     isfound = False
#     for i in range(len(string1)):
#         for j in range(len(string2)):
#             if string2[j].lower() == string1[i] and not isfound:
#                 total = CountMatching(total,1)
#                 isfound = True
#         isfound = False
#     return total
# text1 = input("Enter here :")
# text2 = input("Enter here :")
# print(proccess(text1,text2))



# Exercise-30 :
        # 8.Write a Python program to print the index of a character in a string.
        # Sample string: w3resource
        # Expected output:
        # Current character w position at 0
        # Current character 3 position at 1
        # Current character r position at 2
        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # Current character c position at 8
        # Current character e position at 9
# def IndexofCharacter(string):
#     return "Current character " + string[i] + " position at " + str(i)
# text = input("Enter here :")
# for i in range(len(text)):
#     print(IndexofCharacter(text))
