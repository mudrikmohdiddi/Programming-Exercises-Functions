"""10. Monthly Sales Tax
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 4 percent
and the county sales tax rate is 2 percent. Write a program that asks the user to enter the
total sales for the month. From this figure
following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)"""
def tax(sa):
	s=sa*0.04
	c=sa*0.02
	t=s+c
	return f"The county sales tax={c}\nThe state sales tax={s}\nThe total sales tax={t}  "
sa=float(input("Please enter the total sales for the month:"))
print(tax(sa))
