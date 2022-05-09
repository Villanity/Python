# Program to find the sum of the numbers given in a range

def sumrange(a, b): # function to sum the range
    sumrange = 0 # initialize the sum 
    for i in range(a, b+1): # for loop to iterate through the range
        sumrange = sumrange + i # add the number to the sum
    return sumrange # return the sum

first_num = int(input("Please input the starting number: ")) # ask user to input the first number
second_num = int(input("Please input the last number: ")) # ask user to input the last number

print(sumrange(first_num, second_num)) # print the sum