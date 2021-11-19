# calculating my BMI
my_height =int(input("enter the height in cm "))
my_weight =int(input("Enter the Weight in kg "))
my_bmi = my_weight /(my_height/100*my_height/100)
print("MY BMI is Calculated",  my_bmi) 
if my_bmi < 16.0:
   print("severly underweight")
elif my_bmi <= 18.4:
    print ("Underweigt")
elif my_bmi <= 24.9:
    print ("Normal")
elif my_bmi <= 29.9:
    print ("Overweight")
elif my_bmi <= 34.9:
    print ("Moderately obese")
elif my_bmi <=39.9:
    print ("Severly obses")
elif my_bmi>40.0:
    print ("Mobidly obses")






