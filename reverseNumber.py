# Program to find the reverse of a number

# def reversenum(num): # function to find the reverse of a number
#     rev = 0 # initialize the reverse
#     while num > 0: # while loop to find the reverse
#         rev = rev * 10 + num % 10 # get the last digit
#         num //= 10 # // is floor division
#     return rev # return the reverse

# num1 = int(input("please input a number: ")) # ask user to input a number
# print(reversenum(num1)) # print the reverse

# The program to find the reverse of a number using string slicing

def reversenum(num): # function to find the reverse of a number
    num = str(num) # convert the number to a string
    rev = num[::-1] # use string slicing to find the reverse
    return int(rev) # return the reverse

num2 = int(input("please input a number: ")) # ask user to input a number
print(reversenum(num2)) # print the reverse