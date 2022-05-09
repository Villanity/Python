# Find whether a number is Armstrong number or not

def armstrongNumber(num): # function to check if a number is armstrong number
    sum = 0 # initialize the sum
    num = str(num) # convert the number to a string
    for i in num: # for loop to iterate through the string
        sum += int(i) ** 3 # add the number to the sum
    if sum == int(num): # if the sum is equal to the number
        print("Armstrong Number") # print the message
    else: # if the sum is not equal to the number
        print("Not an Armstrong Number") # print the message

num1 = int(input("Please enter a number: ")) # ask user to input a number
armstrongNumber(num1) # check if the number is armstrong number