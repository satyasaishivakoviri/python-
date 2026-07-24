'''
______ CONDITION STATEMENTS

IF CONDITION

--> the 'if' condition is use to check weather the given statement is true or false

example:

age = int(input("enter your age: "))
if age >= 18:
    print(f'your age is {age} and your eligible to vote')

ELSE CONDITION

--> else is the fall-back statement when if statment is false else will execute

example:

age = int(input("enter your age: "))
if age >= 18:
    print(f'your age is {age} and your eligible to vote')
else:
    print(f'your age is {age} ,not eligible and you have to wait till {18 - age} more years')

example2:

num = int(input("enter any number: "))
if num % 2 == 0:
    print(f"your entered number is {num} and it is even number")
else:
    print(f"your entered number is {num} and it is odd number")

example3:

vol_ = input("enter only single letter: ")
if vol_ in "AEIOUaeiou":
    print(f"{vol_} is a vowel")
else:
    print(f"{vol_} is not a vowel")

example4:

pal = input("enter anything: ")
if pal[::-1] == pal:
    print(f"{pal} is a palendrome")
else:
    print(f"{pal} is not a palendrome")

ELIF CONDITION

--> elis is used to check another condition if the previous if or elif condition is false

example1:

marks = int(input("enter marks: "))
if marks >= 90:
    print("O grade")
elif marks >= 80:
    print("A+ grade")
elif marks >= 65:
    print("A grade")
elif marks >= 35:
    print("pass")
else:
    print("fail")

example2:

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greater then {num2} and {num3}")
elif num2 > num3:
    print(f"{num2} is greater then {num3}")
else:
    print(num3)

NESTED IF CONDTION

-->




'''
details = {"ATMPIN": "1234"}
atm = input("enter your pin: ")
if len(atm) == 4:
    if atm == details["ATMPIN"]:
        op_ = int(input("select options from \n 1.withdraw \n 2.check balance"))
        elif op_ == 1
        print("balance")
    else:
        print("pin is incorrect")
else:
    print("enter correct pin")
        

