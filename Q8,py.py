"""8. Stadium Seating
There are three seating categories at a stadium. For a softball game, Class A seats cost $15,
Class B seats cost $12, and Class C seats cost $9. Write a program that asks how many tickets
for each class of seats were sold, and then displays the amount of income generated from
ticket sales."""
def ticket(a,b,c):
    class_a=a*15
    class_b=b*12
    class_c=c*9
    return f"The amount of income from ticket sales={class_a+class_b+class_c}"
ca=float(input("Please enter the number of ticket sales of Class A seats:"))
cb=float(input("Please enter the number of ticket sales of Class B seats:"))
cc=float(input("Please enter the number of ticket sales of Class C seats:"))
print(ticket(ca,cb,cc))
