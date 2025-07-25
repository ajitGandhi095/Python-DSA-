temp= float(input())

if temp>50:
    print("Extreme Hot")
elif temp>=25 and temp<50:
    print("Hot")
elif temp>=10 and temp<=25:
    print("Cold")
else:
    print("Extreme cold")