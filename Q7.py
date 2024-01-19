"""7. Calories from Fat and Carbohydrates
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
calories from fat = fat grams * 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs = carb grams * 4
The nutritionist asks you to write a program that will make these calculations."""
def calories(f,c):
    cf=f*9
    cc=c*4
    return f"Calories from Fat ={cf}\nCalories from Carbohydrates ={cc}"
nf=float(input("Please enter the number of fat grams:"))
nc=float(input("Please enter the number of carbohydrate grams:"))
print(calories(nf,nc))
    
