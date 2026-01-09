class Employee:
     def __init__(self):
          self.name=""
          self.id=0
          self.location=""
     def a(self):
        
          your_choice=int(input("ENTER EMPLOYEE NUMBER(1-7):"))
          if 1<=your_choice<=7:
               print("Ok,Collect Employee Information")
               return your_choice
          else:
               print("Invalid Number")
     
     def employee1(self):
           self.name= "SIVARANJANI"
           self.id=123
           self.location="CHENNAI"
           self.display()
     def employee2(self):
           self.name="SRINITHI"
           self.id=124
           self.location="TRICHY"
           self.display()
     def employee3(self):
           self.name= "SHALINI"
           self.id=125
           self.location="MADURAI"
           self.display()
     def employee4(self):
           self.name= "MALLEESHWARI"
           self.id=126
           self.location="CHENNAI"
           self.display()
     def employee5(self):
           self.name= "JAISON"
           self.id=128 
           self.location="KERALA"
           self.display()
     def employee6(self):
           self.name= "LENIN"
           self.id=129
           self.location="MADURAI"
           self.display()
     def display(self):
          print("NAME:",self.name)
          print("ID:",self.id)
          print("LOCATION:",self.location)
while True:
 emp=Employee()
 choice=emp.a()
 if choice==1:
           emp.employee1()
 elif choice==2:
           emp.employee2()
 elif choice==3:
           emp.employee3()
 elif choice==4:
           emp.employee4()
 elif choice==5:
           emp.employee5()
 elif choice==6:
      emp.employee6()