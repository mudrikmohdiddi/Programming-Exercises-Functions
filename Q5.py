"""5. Property Tax
A county collects property taxes on the assessment value of property, which is 60 percent
of the property’s actual value. For example, if an acre of land is valued at $10,000,
its assessment value is $6,000. The property tax is then 64￠ for each $100 of the assessment
value. The tax for the acre assessed at $6,000 will be $38.40. Write a program that
asks for the actual value of a piece of property and displays the assessment value and property tax."""
def taxes(n):
    av=n*0.6
    t=(64*av)/10000
    return f"The assessment value=${av}\nThe property tax=${t}"
actual_value=float(input("Please enter the actual value of property:$"))
print(taxes(actual_value))
