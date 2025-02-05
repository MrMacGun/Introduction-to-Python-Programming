import math                     

# Step 1: Input the height, width, and cost of one paint can
height = float(input())
width = float(input())
paint_cost = float(input())

# Step 1: Calculate the wall's area
wall_area = height * width

# Step 1: Output the wall's area
print(f"Wall area: {wall_area:.1f} sq ft")

# Step 2: Calculate the amount of paint needed
paint_needed = wall_area / 350

# Step 2: Output the paint needed
print(f"Paint needed: {paint_needed:.3f} gallons")

# Step 3: Calculate the number of cans needed (rounding up)
cans_needed = math.ceil(paint_needed)

# Step 3: Output the number of cans needed
print(f"Cans needed: {cans_needed} can(s)")

# Step 4: Calculate paint cost, sales tax, and total cost
paint_cost_total = cans_needed * paint_cost
sales_tax = paint_cost_total * 0.07
total_cost = paint_cost_total + sales_tax

# Step 4: Output the paint cost, sales tax, and total cost
print(f"Paint cost: ${paint_cost_total:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")
