# Program to find the sum of the numbers given in a range

def sumrange(a, b):
    sumrange = 0 
    for i in range(a, b+1):
        sumrange = sumrange + i
    return sumrange

first_num = int(input("Please input the starting number: "))
second_num = int(input("Please input the last number: "))

print(sumrange(first_num, second_num))