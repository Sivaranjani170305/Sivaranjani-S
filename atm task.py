class ATM:
    def __init__(self,pin,balance):
         self.pin=pin 
         self.balance=balance
    def check(self):
           your_pin=int(input("enter your pin:"))
           if your_pin==self.pin:
             print("login successfully")
             return True
           else:
             print("invalid pin")
             print("collect your card")
             return False 
    def choice(self):
     print("/.. ATM choice../") 
     print("1.deposit")
     print("2.withdraw")
     print("3.balance")
     print("4.pinchange")
     print("5.transfer")
     print("6.exit") 

    def deposit(self):
        amount=int(input("enter your deposit amount:"))
        if amount>0:
         self.balance+=amount
         print("your amount is deposited")
        else:
         print("invalid amount")
         print("current balance:" , self.balance)


    def withdraw(self):
     amount=int(input("Enter your withdraw amount:"))
     if amount <= 0:
        print("invalid amount")
     elif amount > self.balance:
       print("Insufficient balance")
         
     else:
        self.balance-=amount
        print("withdraw:", amount)
        print("curent balance:",self.balance)
        print("Collect your cash")

    def balancecheck(self):
         print("current balance:",self.balance) 

    def changepin(self):
       current=int(input("Enter your current pin:"))
       new=int(input("Enter your new pin:"))
       confirm=int(input("Enter your confirm pin:"))
       if new==confirm:
        print("your pin is changed:", new)
        self.pin==new
       else:
          print("invalid")
    def transfer(self):
         amount=int(input("Enter transfer amount:"))
         if amount<=self.balance:
            num=int(input("Account Number:"))
            code=input("Enter IFSC Code:")
            print("Transaction Sucessfully")
            self.balance-=amount

         else:
            print("Insufficient balance")

    
    def run(self):
         if not self.check():
           return
         while True:
             self.choice()
             choice=int(input("Enter your choice:")) 
             if choice==1:
              self.deposit()
             elif choice==2:
              self.withdraw()
             elif choice==3:
              self.balancecheck()
             elif choice==4:
              self.changepin()
             elif choice==5:
                self.transfer()
             elif choice==6:
               print("/...THANK YOU COLLECT YOUR CARD.../")
               break
             else:
              print("your choice is invalid")
                
a=ATM(pin=1212 , balance=7000)
a.run()