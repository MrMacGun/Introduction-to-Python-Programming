def driving_cost(miles_per_gallon = float(), 
                 dollars_per_gallon = float(), 
                 miles_driven = float(0)):
    cost = dollars_per_gallon * (miles_driven / miles_per_gallon)
    return cost

if __name__ == '__main__':
    miles = float(input())
    dollars = float(input())

    print(f"{driving_cost(miles, dollars, 10):.2f}")
    print(f"{driving_cost(miles, dollars, 50):.2f}")
    print(f"{driving_cost(miles, dollars, 400):.2f}")