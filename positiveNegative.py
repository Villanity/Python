#program to check if a number is positive or negative

def posneg(n): # function to check if a number is positive or negative
    if n > 0: # if the number is positive
        print("Positive") # print "Positive"
    elif n < 0: # if the number is negative
        print("Negative") # print "Negative"
    else: # if the number is 0
        print("It's 0") # print "It's 0"

num = int(input("Please enter a number: ")) # ask user to input a number
posneg(num) # call the function