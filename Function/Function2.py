# Exercise1
        # Create the fucntion multiply number1 and number2
        # example:multiply(2,3) it will return 6
# def multiply(n1,n2):
#     return n1 * n2
# number1 = int(input("Enter here :"))
# number2 = int(input("Enter here :"))
# print(multiply(number1,number2))


# -----------------------------Part1-----------------------------
# exercise2
        # Create the function name productFromTo 
        # -startNumber: allow user input
        # -endNumber: allow user input
        # ----xample----
        # start number:2
        # end number:4
        # This result is 24 (becuase that 2x3x4 = 24)
        # Note:You need to apply the previously of function multiply()
# def multiply(n1,n2):
#     return n1 * n2
# def productFromTo(start,end):
#     total = 1
#     while start <= end:
#         total = multiply(total,start)
#         start += 1
#     return total
# startnumber = int(input("Start number : "))
# endnumber = int(input("End number : "))
# print("This result is : " + str(productFromTo(startnumber,endnumber)))



# -----------------------------Part2-----------------------------
    # Exercise1 
    # Create the function allow the user enter word and character to remove
    # -function: removeCharacter(word,char)
    # -param: word and char
    # ----xample----
    # Enter a word:abcbdb
    # Enter charater to remove:b
    # Result:acd
# def  removeCharacter(word,char):
#     res = ""
#     for i in range(len(word)):
#         if word[i] != char:
#             res += word[i]
#     return res
# Word = input("Enter word : ")
# Char = input("Enter char : ")
# print(removeCharacter(Word,Char))



# Exercise2 
    # Note:You need to use or apply the function removeCharacter()
    # ----xample----
    # Enter a word:abcbdb
    # Enter charater to remove:b
    # Result:acd
    # Do you want to continue (Y/N)?:Y
    # Enter a word:a-b-c-d
    # Enter charater to remove:-
    # Result:abcd
    # Do you want to continue (Y/N)?:N
# 
# def  removeCharacter(word,char):
#     res = ""
#     for i in range(len(word)):
#         if word[i] != char:
#             res += word[i]
#     return res
# isY = True
# while isY:
#     Word = input("Enter word : ")
#     Char = input("Enter char : ")
#     print(removeCharacter(Word,Char))
#     question = input("Do you want to continue (Y/N)?: ")
#     if question.lower() != 'y':
#         isY = False



# -----------------------------Part3-----------------------------
    # Exercise1
    # Create the function allow the user enter word and character to count
    # -function: countCharacter(word,char)
    # -param: word and char
    # ----xample----
    # Enter a word:abcbdb
    # Enter charater to count:b
    # The character b occurs 3 times in the word.
# 
# def countCharacter(word,char):
#     count = 0
#     for i in range(len(word)):
#         if word[i] == char:
#             count += 1
#     return count
# Word = input("Enter : ")
# Char = input("Enter : ")
# print("The character",Char, "occurs "+ str(countCharacter(Word,Char)) + " times in the word.")



# Exercise2
    # Note:You need to use or apply the function removeCharacter()
    # ----xample----
    # Enter a word:abcbdb
    # Enter charater to count:b
    # The character b occurs 3 times in the word.
    # Do you want to continue (Y/N)?:Y 
    # Enter a word:a-b-c-d-e
    # Enter charater to count:-
    # The character b occurs 4 times in the word.
    # Do you want to continue (Y/N)?:N
# 
# def countCharacter(word,char):
#     count = 0
#     for i in range(len(word)):
#         if word[i] == char:
#             count += 1
#     return count
# isY = True
# while isY :
#     Word = input("Enter : ")
#     Char = input("Enter : ")
#     print("The character",Char, "occurs "+ str(countCharacter(Word,Char)) + " times in the word.")
#     question = input("Do you want to continue (Y/N)?: ")
#     if question.lower() != 'y':
#         isY = False
