# check if the given year is leap year or not

def leapcheck(y):
    if y % 4 == 0:
        print("It's a Leap year")
    else: 
        print("Not a Leap year")

year = int(input("Please enter the year: "))
leapcheck(year)