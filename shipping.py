weight = 1.5

#Ground Shipping
if weight <= 2:
  cost_ground = 20 + (weight * 1.50)
elif weight <= 6:
  cost_ground = 20 + (weight * 3.00)
elif weight <= 10:
  cost_ground = 20 + (weight * 4.00)
else:
  cost_ground = 20 + (weight * 4.75)

#Ground Premium Shipping
cost_of_premium_ground_shipping = 125.00

#Drone Shipping
if weight <= 2:
  cost_drone = 0 + (weight * 4.50)
elif weight <=6:
  cost_drone = 0 + (weight * 9.00)
elif weight <= 10:
  cost_drone = 0 + (weight * 12.00)
else:
  cost_drone = 0 + (weight * 14.25)

print("Ground Shipping Premium: $" + str(cost_of_premium_ground_shipping))
print("Ground Shipping: $" + str(round(cost_ground, 2)))
print("Drone Shipping: $" + str(round(cost_drone, 2)))
