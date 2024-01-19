"""3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a
program that asks the user to enter the replacement cost of a building and then displays
the minimum amount of insurance he or she should buy for the property."""
def house_cost(c):
    return f"Minimum amount of insurance={c*0.8}"
h=float(input("Please enter cost of a building:"))
print(house_cost(h))
