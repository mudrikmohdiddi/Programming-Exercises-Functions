"""2. Sale Tax Program Refactoring
Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that exercise you
were asked to write a program that calculates and displays the county and state sales tax
on a purchase. If you have already written that program, redesign it so the subtasks are in
functions. If you have not already written that program, write it using functions."""
"""p=float(input("Please enter the amount of a purchase:"))
statetax=p*0.04
countytax=p*0.02
totaltax=statetax+countytax
totalsale=p+totaltax
print("The amount of the purchase is:",p)
print("The state sales tax is:",statetax)
print("The county sales tax is:",countytax)
print("The total sales tax is:",totaltax)
print("The total sales is:",totalsale)"""
def purchase(p):
    return f"state sales tax={p*0.04}\ncounty sales tax={p*0.02}"
print(purchase(2000))
