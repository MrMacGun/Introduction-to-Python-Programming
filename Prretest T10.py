stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

numstocks = int(input())

def calculate_total_cost():
    # Accept the number of shares to be purchased
    num_shares = int(input("Enter the number of stocks to purchase: "))
    
    total_cost = 0.0
    
    # Loop to accept stock selections
    for _ in range(num_shares):
        stock_selection = input("Enter stock symbol: ")
        if stock_selection in stocks:
            total_cost += stocks[stock_selection]
        else:
            print(f"Stock symbol '{stock_selection}' not found. Skipping...")
    
    # Output the total cost formatted to two decimal places
    print(f"Total price: ${total_cost:.2f}")

# Call the function to execute
calculate_total_cost()