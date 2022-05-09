#program to check if a number is positive or negative

def posneg(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("It's 0")

num = int(input("Please enter a number: "))
posneg(num)