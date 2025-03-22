#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/22/section/10


lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave_nectar:.2f} cup(s) agave nectar")

desired_servings = float(input("\nHow many servings would you like to make?\n"))


scaling_factor = desired_servings / servings

adjusted_lemon_juice = lemon_juice * scaling_factor
adjusted_water = water * scaling_factor
adjusted_agave_nectar = agave_nectar * scaling_factor

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{adjusted_lemon_juice:.2f} cup(s) lemon juice")
print(f"{adjusted_water:.2f} cup(s) water")
print(f"{adjusted_agave_nectar:.2f} cup(s) agave nectar")

gallons_lemon_juice = adjusted_lemon_juice / 16
gallons_water = adjusted_water / 16
gallons_agave_nectar = adjusted_agave_nectar / 16

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{gallons_lemon_juice:.2f} gallon(s) lemon juice")
print(f"{gallons_water:.2f} gallon(s) water")
print(f"{gallons_agave_nectar:.2f} gallon(s) agave nectar")
