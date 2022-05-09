# Sum of the first n Numbers

def sumn(n): # function to sum the first n numbers
    sumn = 0 # initialize the sum
    for i in range(1, n+1): # for loop to iterate through the range
        sumn = sumn + i # add the number to the sum
    return sumn # return the sum

num = int(input("Please enter a Number: ")) # ask user to input a number
print(sumn(num)) # print the sum