#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/22/section/11

food = input("Enter food item name:\n")
price = float(input("Enter item price:\n"))
qty = int(input("Enter item quantity:\n"))

total1 = price * qty

print("RECEIPT")
print(f"{qty} {food} @ ${price:.2f} = ${total1:.2f}")

food2 = input("Enter second food item name:\n")
price2 = float(input("Enter item price:\n"))
qty2 = int(input("Enter item quantity:\n"))

total2 = price2 * qty2

print(f"{qty2} {food2} @ ${price2:.2f} = ${total2:.2f}")

total_cost = total1 + total2
print(f"Total cost: ${total_cost:.2f}")

gratuity = total_cost * 0.15
grand_total = total_cost + gratuity

print(f"15% gratuity: ${gratuity:.2f}")
print(f"Total with tip: ${grand_total:.2f}")
