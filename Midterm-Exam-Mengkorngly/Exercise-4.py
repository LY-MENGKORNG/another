i = 0
res = ""
isfound = False
while i < 3 and not isfound :
    num = int(input("Enter Number :"))
    if num == 68:
        res = "YOU WON!"
        isfound = True
    elif i < 2:
        print("ENTER NUMBER AGAIN")
    i += 1
if isfound == False:
    res = "YOU LOST"
print(res)