
numbers = [1,2,3,4]
new_list = [i+1 for i in numbers]
print(new_list)


name = "Aaditya"
new_list_1 = [letters for letters in name]
print(new_list_1)

new_list_2 = [2*(i) for i in range(0,5) if (i%2==0)]
print(new_list_2)

names = ["Alex","beth","Caroline","Dave","Elanor","Freddie"]
new_list_3 = [name.upper() for name in names if len(name)>5]
print(new_list_3)

numbers= [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

result = [num for num in numbers if num%2==0]
print(result)


with open("Exercise 3/file1.txt") as file1:
    list1 = file1.readlines()

with open("Exercise 3/file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)