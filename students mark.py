class Student:
    pass
S1=Student()
S2=Student()

S1.name=input("Enter student1 name:")
S1.mark1=int(input("Enter tamil mark:"))
S1.mark2=int(input("Enter english mark:"))
S1.mark3=int(input("Enter maths mark:"))
   
S2.name=input("Enter student2 name:")
S2.mark1=int(input("Enter tamil mark:"))  
S2.mark2=int(input("Enter english mark:"))
S2.mark3=int(input("Enter maths mark:"))

Total1=S1.mark1+S1.mark2+S1.mark3
Average1=S1.mark1+S1.mark2+S1.mark3/3

Total2=S2.mark1+S2.mark2+S2.mark3
Average2=S2.mark1+S2.mark2+S2.mark3/3
print("Student Name:",S1.name)
print("Total Mark:",Total1)
print("Average Mark:",Average1)

print("Student Name:",S2.name)
print("Total Mark:",Total2)
print("Average Mark:",Average2)