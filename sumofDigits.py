#program to find the sum of the digits of a number

# def sumdigits(num): # function to sum the digits of a number
#     sum = 0 # initialize the sum
#     while num > 0: # while loop to find the sum of the digits
#         sum += num % 10 # get the last digit
#         num //= 10 # // is floor division
#     return sum # return the sum

# num1 = int(input("please input a number: ")) # ask user to input a number
# print(sumdigits(num1)) # print the sum

# another way to calculate the sum of the digits using list slicing

def sumdigits(num): # function to sum the digits of a number
    sum = 0 # initialize the sum
    num = str(num) # convert the number to a string
    for i in num: # for loop to iterate through the string
        sum += int(i) # add the number to the sum
    return sum # return the sum

num2 = int(input("please input a number: ")) # ask user to input a number
print(sumdigits(num2)) # print the sum

