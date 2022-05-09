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

first_num = int(input("Enter the First Number: "))
second_num = int(input("Enter the Second Number: "))
third_num = int(input("Enter the Third Number: "))

print(max(first_num, second_num, third_num))

# print(greatestThree(first_num, second_num, third_num))

