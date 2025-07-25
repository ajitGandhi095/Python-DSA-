age= int(input("enter your age: "))

if(age>=18):
    test=input("Enter pass/fail: ").lower()
    if(test == "pass"):
        print("Elegible for driving license")
    else:
        print("Not Elegible for driving license")
else:
    print("Not elegible for driving license")