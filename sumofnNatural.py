#sum of n natural numbers

def sumn(listn): # function to sum the first n numbers
    sumn = 0 # initialize the sum
    for i in range(len(listn)): # for loop to iterate through the range
        sumn = sumn + listn[i] # add the number to the sum
    return sumn # return the sum

listn = [] # initialize the list
numn = int(input("Please input number of elements: ")) # ask user to input the number of elements
print("Please enter the elements: ") # print "Please enter the elements"
for i in range(0, numn): # for loop to iterate through the range
    ele = int(input()) # ask user to input the elements
    listn.append(ele) # append the elements to the list
    
print(sumn(listn)) # print the sum