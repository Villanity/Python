# Find the greatest of three numbers 

# def greatestThree(a, b, c):
#     max_num = 0
#     if a > b and a > c:
#         max_num = a
#     elif b > c :
#         max_num = b
#     else:
#          max_num = c
#     return max_num

first_num = int(input("Enter the First Number: ")) # ask user to input the first number
second_num = int(input("Enter the Second Number: ")) # ask user to input the second number
third_num = int(input("Enter the Third Number: ")) # ask user to input the third number

print(max(first_num, second_num, third_num)) # print the greatest number

# print(greatestThree(first_num, second_num, third_num))

