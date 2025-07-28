# 1431. Kids With the Greatest Number of Candies

def kidsWithCandies(candies, extraCandies):

    max_candies= max(candies)
    ans= []

    for i in candies:
        if i+extraCandies >= max_candies:
            ans.append(True)
        else:
            ans.append(False)
    
    return ans

    # OR

    # return([ (i+extraCandies)>= max(candies) for i in candies])
    
#main program
n= int(input("Enter number of kids u have: "))
candies=[]
for i in range(1, n+1):
    val= int(input("Enter {} kids candy number: ".format(i)))
    candies.append(val)
extraCandies= int(input("Enter How many extra candies u have: "))

ans= kidsWithCandies(candies, extraCandies)
print(ans)