# Program to check whether a number is odd or even

def oddeven(n): # function to check whether a number is odd or even
    if n % 2 == 0: # if the number is even
        print("Even") # print "Even"
    else: # if the number is odd
        print("Odd") # print "Odd"

num = int(input("Please enter a number: ")) # ask user to input a number
oddeven(num) # call the function