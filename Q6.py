"""6. Body Mass Index
Write a program that calculates and displays a person’s body mass index (BMI). The
BMI is often used to determine whether a person is overweight or underweight for his
or her height. A person’s BMI is calculated with the following formula:
BMI _ weight _ 703 / height2
where weight is measured in pounds and height is measured in inches."""
def BMI(w,h):
    bmi=(w*703)/(h**2)
    if(bmi<18.5):
        return f"BMI={bmi}\nA person is underweight"
    elif(bmi>25):
        return f"BMI={bmi}\nA person is overweight"
    elif(bmi>=18.5 and bmi<=25):
        return f"BMI={bmi}\nA person is optimalweight"
wt=float(input("Please enter body weight:"))
ht=float(input("Please enter body height:"))
print(BMI(wt,ht))
