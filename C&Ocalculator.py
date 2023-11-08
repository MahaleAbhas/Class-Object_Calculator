class Calculator:
    def add(self,a,b):
        ans=a+b
        print("Addition Of Two Number:",ans)


    def sub(self,a,b):
        ans=a-b
        print("SubStraction Of Two Number:",ans)


    def mul(self,a,b):
        ans=a*b
        print("Multiplication Of Two Number:",ans)


    def div(self,a,b):
        ans=a/b
        print("Division Of Two Number:",ans)
cal=Calculator()

while True:
    ch=int(input("\nCalculation Of Two Number\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exits\nEnter Your Choice:"))
    

    if ch==1:
        x=int(input("Enter The First Number:"))
        y=int(input("Enter The Second Number:"))

        cal.add(x,y)

    elif ch==2:
        x=int(input("Enter The First Number:"))
        y=int(input("Enter The Second Number:"))

        cal.sub(x,y)


    elif ch==3:
        x=int(input("Enter The First Number:"))
        y=int(input("Enter The Second Number:"))

        cal.mul(x,y)


    elif ch==4:
        x=int(input("Enter The First Number:"))
        y=int(input("Enter The Second Number:"))

        cal.div(x,y)

    elif ch==5:
        break

    else:
        print("Please Enter Correct Number....")
        






























    
