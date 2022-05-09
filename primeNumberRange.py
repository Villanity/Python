# find weather a number is prime or not in a given range

def primecheck(a, b): # function to check if a number is prime
    count = 0 # initialize the count
    listprime = [] # initialize the list
    for i in range(a, b+1): # for loop to iterate through the range
        for j in range(2, i): # for loop to check if the number is prime
            if i % j == 0: # if the number is divisible by another number
                count += 1 # add 1 to the count
        if count != 0: # if the count is not 0
            pass # pass
        else: # if the count is 0
            listprime.append(i) # append the number to the list
        count = 0 # reset the count
    return print(listprime) # print the list
    
            

num1 = int(input("please input first number: ")) # ask user to input the first number
num2 = int(input("please input last number: ")) # ask user to input the last number
primecheck(num1, num2) # call the function