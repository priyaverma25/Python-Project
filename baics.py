# inputs we need from the user 
#  Total rent 
#  Toal food ordered for snacking
# Electricity units spend
# Charge per unit of electricity
# Number of people living in the hostel/flat
#  Output 
# Total amount you've to pay is 

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of people living in the hostel/flat = "))

total_electricity = electricity_spend * charge_per_unit
output = (food + rent + total_electricity) // persons
print("Each person has to pay:", output)
