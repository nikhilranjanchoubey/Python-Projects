## Inputs we need from the user
## Total rent
## Total food ordered for snacking
## Charge per unit
## Prsons living in room/flat

## Output
## Total amount you've to pay is 

rent = int(input ("Enter your hostel/flat rent = "))
food = int(input ("Enter the amount of food ordered = "))
electricity_spend = int(input ("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the total no. of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)