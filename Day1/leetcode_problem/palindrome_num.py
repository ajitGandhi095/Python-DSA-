# 9. Palindrome Number

def palindromeNum(num):
    temp= num
    reverse=0
    while temp>0:
        r= temp%10
        temp //= 10
        reverse= reverse * 10 + r
    if num==reverse:
        return True
    else:
        return False

#main program
num= int(input("Enter your number: "))
ans= palindromeNum(num)
print(ans)