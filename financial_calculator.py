import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("\n")
print("investment   - to calculate the amount of interest you'll earn on interest")
print("bond         - to calculatethe amount you'll have to pay on a home loan")


choice = str(input(""))

up = choice.upper()

#Investment
if up == "INVESTMENT":
     P = float(input("Enter amount of deposit:"))
     rate = float(input("Enter interest rate:"))
     years= float(input("Enter number of years you plan to invest:"))
     interest = str(input("Simple or compound interest:"))
     r=rate/100
     
     if interest == "simple":
         A = P*(1+rate*years)
     elif interest == "compound":
         A= P*math.pow((1+r),years)
         A = round(A,2)
         print(f"Total amount once interest is applied is R:{A}")            


#Mortgage 
x=0
if up == "BOND":
     L = float(input("Enter present value:"))
     rate = float(input("Enter annual interest rate:"))
     n= float(input("Enter number of months you plan to repay bond:"))#months
     
     i = rate *.01
     i = i/12
     
     print(i) #.005
     r=1/(1+i)
     print(r) #.995
     r=round(r,3)


     m=n+1





     top=1-r
     var = math.pow(r,m)
     bottom = r-var

     p = L *(top/bottom)
     p=round(p,2)

     print(p)     
     
     print(f"The amount to be repaid on a home loan each month is R{p}")
