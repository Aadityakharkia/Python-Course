'''
fruit = ["Apple","Orange","Pineapple"]
for fruit in fruit:
    print(fruit)

'''
'''a= input("Input a list of student heights ").split()
print(a)
for n in range(0,len(a)):
    a[n]= int(a[n])
b=0 
 Remove sum(a) and put 0 if you want to use loop
c=0 
 Remove len(a) and put 0 if you want to use loop
for i in range(0,len(a)):\
    b= b + a[i]
for j in a:
    c += 1
print(round(b/c))'''

'''a= input("Input a list of student marks ").split()
print(a)
for n in range(0,len(a)):
    a[n]= int(a[n])
b=0
for i in range(0,len(a)):
    if b<a[i]:
        b= a[i]

print(b)'''

'''b=-0
for i in range(1,101):
    if i%2==0:
        b += i
print(b)'''

# or 

'''b=0
for i in range(2,101,2):
    b += i
print(b)'''

# Fizz Buzz Game
'''
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0 and i%5!=5:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    else:
        print(i)
'''