# Sum of the first n Numbers

def sumn(n):
    sumn = 0
    for i in range(1, n+1):
        sumn = sumn + i
    return sumn

num = int(input("Please enter a Number: "))
print(sumn(num))