#sum of n natural numbers

def sumn(listn):
    sumn = 0
    for i in range(len(listn)):
        sumn = sumn + listn[i]
    return sumn

listn = []
numn = int(input("Please input number of elements: "))
print("Please enter the elements: ")
for i in range(0, numn):
    ele = int(input())
    listn.append(ele)
    
print(sumn(listn))