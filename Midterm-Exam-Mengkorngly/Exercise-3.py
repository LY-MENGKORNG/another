text = input("Enter here :")
res = ""
sum = 0
for i in range(len(text)):
    if text[i] != " ":
        res += text[i]
    elif res == '10' or res == '12':
        res = ""
    elif res != "":
        sum += int(res)
        res = ""
if res != "":
    sum += int(res)
if sum == 20:
    res = "WON"
else :
    res = "LOST"
print(res)