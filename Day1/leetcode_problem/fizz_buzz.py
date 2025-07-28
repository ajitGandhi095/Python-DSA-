"""
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true

"""

def fizzBuzz(lst):
    print(lst)
    lst1=[]

    for val in lst:
        print(val)
        if(val%3==0 and val%5==0):
            lst1.append("FizzBuzz")
        elif(val%3==0):
            lst1.append("Fizz")
        elif(val%5==0):
            lst1.append("Buzz")
        else:
            lst1.append(val)
    return lst1

#main Program
n= int(input("How many number you want to insert: "))
lst=[]
for i in range(1,n+1):
    val= int(input("Enter {} number: ".format(i)))
    lst.append(val)

result= fizzBuzz(lst)
print(result)
