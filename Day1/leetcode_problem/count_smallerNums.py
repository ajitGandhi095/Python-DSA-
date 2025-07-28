# 1365. How many numbers are smaller than the current number

def smallerNumbersThenCurrent(lst):
    ans=[]
    for i in lst:
        count=0
        for j in lst:
            if j<i:
                count += 1
        ans.append (count)
    return ans

#main program
n= int(input("Enter How many number u want to add: "))
lst=[]
for i in range(1,n+1):
    val= int(input("Enter your {} number: ".format(i)))
    lst.append(val)

ans= smallerNumbersThenCurrent(lst)
print(ans)