# Find whether a number is Armstrong number or not in a given range

def armstrongNumber(a, b): # function to check if a number is armstrong number
    sum = 0 # initialize the sum
    listarm = [] # initialize the list
    for i in range(a, b+1): # for loop to iterate through the range
        i = str(i) # convert the number to a string
        for j in i: # for loop to iterate through the string
            sum += int(j) ** len(i) # add the number to the sum
        if sum == int(i): # if the sum is equal to the number
            listarm.append(i) # add the number to the list
        sum = 0 # reset the sum
    print(listarm) # print the list

num1 = int(input("Please enter first number: ")) # ask user to input a number
num2 = int(input("Please enter second number: ")) # ask user to input a number
armstrongNumber(num1, num2) # check if the number is armstrong number
