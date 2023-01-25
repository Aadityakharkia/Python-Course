import random
a= input("Please enter all the names seperated by comma  ")
b = a.split(",")
c=len(b) 
r = random.randint(0,c-1)
print(b[r])

row1 = ["😀","😀","😀"]
row2 = ["😀","😀","😀"]
row3 = ["😀","😀","😀"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the tresure ?? ")
horizontal = int(position[0])
vertical = int(position[1])

print(map[vertical-1])

