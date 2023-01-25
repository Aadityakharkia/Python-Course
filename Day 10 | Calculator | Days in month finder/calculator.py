# Calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Making Calculator App

def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a/b

operation = {"+":add,"-":substract,"*":multiply,"/":divide}
print("\n Welcome to Calculator Software ")
def calcu():
    num1 = int(input("Please enter the first number\n"))
    should = True

    while should:
        for i in operation:    
            print(i)    
        sign = input("Which operation do you want to do ")  
        num2 = int(input("Pleased enter the second number\n"))   
        calculation = operation[sign] 
        answer = calculation(num1,num2)
        
        print(f"{num1} {sign} {num2} = {answer}")
        a = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit or 's' to start a new calculation\n")
        if a == "y":
            num1 = answer
        elif a == "s":
            calcu()
        else:
            should = False

print(logo)            
calcu()
