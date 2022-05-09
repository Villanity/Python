# Find if a Number is Palindrome or not

def palindromecheck(num): # function to check if a number is palindrome
    num_new = str(num) # convert the number to a string
    rev_num = num_new[::-1] # use string slicing to find the reverse
    if num_new == rev_num: # if the number is palindrome
        print("Plaindrome") # print the message
    else: # if the number is not palindrome
        print("Not a Palindrome") # print the message

num1 = int(input("Please enter a number: ")) # ask user to input a number
palindromecheck(num1) # check if the number is palindrome