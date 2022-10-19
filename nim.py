import random
list_a = []
name1 = "ok"
name2 = "ok"
curP = ""
a = 1
b = 1
def returnXor(list1):
    e = list1[0]
    f = list1[1]
    g = list1[2]
    h = list1[3]
    return e^f^g^h


for i in range(4):
    list_a.append(random.randint(1,6))

gameMode = int(input("Press 1 to play 2-player and 2 to play against computer: "))
if gameMode == 1:
    name1 = input("Enter, player 1: ")
    name2 = input("Enter name, player 2: ")
    curP = name1
elif gameMode == 2:
    name1 = input("Enter your name: ")
    name2 = "Computer"
    if returnXor(list_a) == 0:
        curP = name1
    else:
        curP = name2
    print (returnXor(list_a))
while True:
    print(list_a)
    print(curP + "'s turn")
    if gameMode == 1 or (gameMode == 2 and curP == name1):
        a = int(input("Enter the column: ")) - 1
        b = int(input("How many coins to remove: "))
        if (len(list_a) - a > 0):
            if (list_a[a] - b >= 0 and b > 0):
                list_a[a] = list_a[a] - b
                if (curP == name1):
                    curP = name2
                else:
                    curP = name1
    elif gameMode == 2 and curP == name2:
        for i in range(len(list_a)):
            rnd = False
            if list_a[i]>0:
                for j in range(1, list_a[i]+1):
                    list_a[i] -= j
                    if returnXor(list_a) != 0:
                        list_a[i] += j
                    elif returnXor(list_a) == 0:
                        rnd = True
                        curP = name1
                        break
            if rnd:
                break
    if list_a[0] + list_a[1] + list_a[2] + list_a[3] == 0:
        break
if (curP == name1):
    curP = name2
else:
    curP = name1

print (curP, " won.")
