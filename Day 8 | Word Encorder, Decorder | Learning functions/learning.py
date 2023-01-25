'''
# Simple Function

def greet():
    print("Hello")
    print("How are you")
    print("Good")
    
greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

greet_with_name("Aaditya")

# Function with more than 1 input

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Aaditya","Dhanbad") # Positional Argument
greet_with(name="Aaditya",location="Dhanbad") # Keyword Arguments


# Painting Challenge
import math

def a(height, width,cover):
    area = height*width
    cans = math.ceil(area/cover)
    print(f"You may require {cans} to pain the building")
h= int(input("Height of the wall: \n"))
w = int(input("Width of the wall: \n"))
coverage = 5
a(height=h, width = w, cover = coverage)



# Prime Number Checker

n= int(input("Please enter a number: \n"))
def prime(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime==True:
        print("The Number is a prime number")
    else:
        print("The Number is not a prime number")
prime(number=n)

'''