# 
# otherwise = False
# i = 0
# while i < 5:
#     num = int(input("Enter Number :"))
#     if (num >= 10 and num >= 30) and not otherwise:
#         res = "WON"
#     else:
#         res = "LOST"
#         otherwise = True
#     i += 1
# print(res)



# Function :
def check(number):
    otherwise = False
    if (num >= 10 and num >= 30) and not otherwise:
        res = ("WON")
    else :
        res = ("LOST")
        otherwise = True
for i in range(5):
    num = int(input("Enter here :"))
    print(check(num))