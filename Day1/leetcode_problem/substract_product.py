# 1281. Subtract the Product and Sum of Digits of an Integer

def substractProductAndSum(num):
    temp= num
    product= 1
    sum= 0
    while temp>0:
        r= temp%10
        product= product * r
        sum= sum + r
        temp= temp // 10

    return product - sum

#main program
num= int(input("Enter Your Number: "))
ans= substractProductAndSum(num)
print(ans)
