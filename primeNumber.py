# find weather a number is prime or not

def primecheck(n): # function to check if a number is prime
    count = 0 # initialize the count
    for i in range(2, n): # for loop to check if the number is prime
        if n % i == 0: # if the number is divisible by another number
            count += 1 # add 1 to the count
    if count != 0: # if the count is not 0
        print("Not a Prime Number") # print "Not a Prime Number"
    else: # if the count is 0
        print("Prime Number") # print "Prime Number"
            
num = int(input("please enter a number: ")) # ask user to input a number
primecheck(num) # call the function