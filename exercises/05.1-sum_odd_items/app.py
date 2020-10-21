arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds():
 totalSum=0
 for number in range(0,len(arr)):
     if (arr[number] % 2 !=0):
        totalSum=totalSum + arr[number]
     print (totalSum)
print(sumOdds())


