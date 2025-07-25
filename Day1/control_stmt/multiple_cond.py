marks= int(input("Enter your marks: "))

if marks>100:
    print("Plz enter valid marks between 1 to 100")
elif marks >=90 and marks<=100:
    print("Excellent")
elif marks>=70 and marks<90:
    print("Good")
elif marks>=40 and marks<70:
    print("Fair")
else:
    print("Bad")
