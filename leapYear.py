# check if the given year is leap year or not

def leapcheck(y): # function to check whether a year is leap year or not
    if y % 4 == 0: # if the year is divisible by 4
        print("It's a Leap year") # print "It's a Leap year"
    else: # if the year is not divisible by 4
        print("Not a Leap year") # print "Not a Leap year"

year = int(input("Please enter the year: ")) # ask user to input a year
leapcheck(year) # call the function