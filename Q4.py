"""4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses."""
def monthly_and_annual_cost(a,b,c,d,e,f):
    return f"Total monthly cost={a+b+c+d+e+f}\nTotal annual cost={(a+b+c+d+e+f)*12}"
l=float(input("Please enter monthly loan payment:"))
i=float(input("Please enter monthly insurance:"))
g=float(input("Please enter monthly gas:"))
o=float(input("Please enter monthly oil:"))
t=float(input("Please enter monthly tires:"))
m=float(input("Please enter monthly maintenance:"))
print(monthly_and_annual_cost(l,i,g,o,t,m))
