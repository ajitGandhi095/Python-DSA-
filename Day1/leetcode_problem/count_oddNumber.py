# Count Odd numbers in an interval range

def countOddNumber(low, high):
    # ans= 0
    # for val in range(low, high+1):
    #     if(val%2!=0):
    #         ans += 1
    # return ans

    # OR

    return (high+1)//2 - (low//2)

#main program
low= int(input("Enter Your Starting Value: "))
high= int(input("Enter Your Ending Value: "))

result= countOddNumber(low, high)
print(result)