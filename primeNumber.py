# find weather a number is prime or not

def primecheck(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count != 0:
        print("Not a Prime Number")
    else:
        print("Prime Number")
            

num = int(input("please enter a number: "))
primecheck(num)