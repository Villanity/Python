# find weather a number is prime or not in a given range

def primecheck(a, b):
    count = 0
    listprime = []
    for i in range(a, b+1):
        for j in range(a, i-1):
            if i % j == 0:
                count += 1
        if count != 0:
            pass
        else:
            listprime.append(i)
    return print(listprime)
    
            

num1 = int(input("please input first number: "))
num2 = int(input("please input last number: "))
primecheck(num1, num2)