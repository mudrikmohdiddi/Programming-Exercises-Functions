"""1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, and then converts that distance to
miles. The conversion formula is as follows:
Miles = Kilometers * 0.6214"""
def km_to_mile(k):
    return k*0.6214
km=float(input("Please enter km:"))
print("Mile=",km_to_mile(km))
    
