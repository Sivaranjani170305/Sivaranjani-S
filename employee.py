class Employee:
    pass
E1=Employee() 
E2=Employee()
print("/....EMPLOYEE SALARY CALCULATION..../")
print("/..SALARY OF EMPLOYEE 1../")
E1.name=input("Enter employee1 name:")
E1.basicsalary=int(input("Enter the basic salary of employee1:"))
E1.hra=int(input("Enter the hra amount of employyee1:"))
E1.aw=int(input("Enter the aw amount of employee1:"))
print("/...SALARY OF EMPLOYEE 2../")
E2.name=input("Enter employee2 name:")
E2.basicsalary=int(input("Enter the basic salary of employee2:"))
E2.hra=int(input("Enter the hra amount of employyee2:"))
E2.aw=int(input("Enter the aw amount of employee2:"))
Totalsalary1=E1.basicsalary+E1.hra+E1.aw
Totalsalary2=E2.basicsalary+E2.hra+E2.aw
print("Employee 1 Name:", E1.name)
print("Total salary of employee 1:", Totalsalary1)
print("Employee 2 Name:", E2.name)
print("Total salary of employee2:", Totalsalary2)
if(Totalsalary1>Totalsalary2):
    print("Employee 1 value is big")
else:
    print("Employee 2 value is big")