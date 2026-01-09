value=int(input("Enter your value:"))
if value%8== 0 and value%11==0:
    print("Your value is divided by 8 and 11")
elif value%8 == 0 and value%11!= 0:
    print("Your value is divided by 8 and not divided by 11")
elif value%8!= 0 and value%11== 0:
    print("Your value is not divided by 8 and your value is divided by 11")
else:
    print("Your value is not divided by 8 and 11")