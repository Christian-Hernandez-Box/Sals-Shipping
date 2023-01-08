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