# Sals-Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project I built a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
Here are the prices:
```
Ground Shipping
---------------
Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Ground Shipping Premium
-----------------------
Flat charge: $125.00

Drone Shipping
--------------
Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00
```
```
# Program Intro & Initial Data Capture
print("Hello! Welcome to Sal's Shipping! Please tell us your package's weight to see the cost of each shipping option available.")
weight = int(input())
print("Thank you! One second as we process this request.")

# Delay Program 3 Seconds
import time
time.sleep(3)

# Ground Shipping Calculation
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
elif weight >= 10:
  cost_ground = weight * 4.75 + 20

# Ground shipping premium calculation
cost_ground_premium = 125

# Drone Shipping Calculation
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.0
elif weight <= 10:
  cost_drone = weight * 12.0
elif weight >= 10:
  cost_drone = weight * 14.25

# Program Output w/ Shipping Costs Given X Package Weight
print("Here is the shipping cost for each available shipping option, with a package weight of:", weight, "lbs.")
print("Ground Shipping $", cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)
print("Drone Shipping $", cost_drone)
print("Thank you for using Sal's Shipping!")
```
