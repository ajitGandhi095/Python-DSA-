# 2520. Count the Digits That Divide a Number
def countDigits(num):
    temp= num
    count=0

    while temp>0:
        # find the last digit of the number
        r= temp%10
        if(num%r == 0):
            count += 1
        # Remove the last digit from temp
        temp//=10
    return count

#main program
n= int(input("Enter your number: "))
ans= countDigits(n)
print(ans)