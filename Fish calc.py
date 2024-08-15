# A = length of fish 
# B = girth of fish
fish_list = []
weight_list = []

def get_number(prompt):        #prompt user(?)
    while True:                 #creates loop
        try:           #it tries to change it to a float 
            value = input(prompt).strip()         #strip is to get rid of any blank spaces
            number = float(value)           # Directly convert the input to float
            return number             #return num to get_number
        except ValueError:            #if all else fails
            print("Invalid number. Please enter a valid integer or float.")

# Input for fish1
fish_list.append(input("Enter name of the fish: "))
A = get_number("Enter fish1 length: ")
B = get_number("Enter fish1 girth: ")

# Input for fish2
fish_list.append(input("Enter name of the fish: "))
A2 = get_number("Enter fish2 length: ")
B2 = get_number("Enter fish2 girth: ")

# Displaying the results
print(f"Fish1: A = {A}, B = {B}")
print(f"Fish2: A = {A2}, B = {B2}")
print(f"Fish list: {fish_list}")

#rounding to 2 decimal place
Weight = round((B * B * A) / 800, 2)
print("Weight of Fish1:", Weight)
weight_list.append(Weight)

Weight2 = round((B2 * B2 * A2) / 800, 2)
print("Weight of Fish2:", Weight2)
weight_list.append(Weight2)

#if
if Weight <= 41:
    print("Fish1: Small fish")
elif Weight <=99:
    print("Fish1: Medium Fish")
elif Weight <=174:
    print("Fish1: Big fish")
else:
    print("Fish1: Giant fish")
 
#if.2
if Weight2 <= 41:
    print("Fish2: small fish")
elif Weight2 <=99:
    print("Fish2: Medium Fish")
elif Weight2 <=174:
    print("Fish2: Big fish")
else:
    print("Fish2: Giant fish")