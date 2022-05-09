# Program to check whether a number is odd or even

def oddeven(n):
    if n % 2 == 0:
        print("Even")
    else: 
        print("Odd")

num = int(input("Please enter a number: "))
oddeven(num)