"""9. Paint Job Estimator
A painting company has determined that for every 115 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $20.00 per
hour for labor. Write a program that asks the user to enter the square feet of wall space to
be painted and the price of the paint per gallon. The program should display the following
data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job"""
def paint(w,cg):
    hours=8*w/155
    no_g=w/155
    ch_labor=20*hours
    co_paint=no_g*cg
    tc=ch_labor+co_paint
    return f"The number of gallons of paint required={no_g}\nThe hours of labor required={hours}\nThe cost of the paint={no_g*cg}\nThe labor charges={ch_labor}\nThe total cost of the paint job={tc}"
w=float(input("Please enter the square feet of wall space be painted:"))
cg=float(input("Please enter the price of the paint per gallon:"))
print(paint(w,cg))
