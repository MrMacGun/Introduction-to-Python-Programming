
#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

purchase = {
    'bananas': 1.85,
    'steak': 19.99,
    'cookies': 4.52,
    'celery': 2.81,
    'milk': 4.34
}

useritem = input()
numitems = int(input())
total = 0.00

if useritem in purchase:
    item_price = purchase[useritem]
    if item_price < 10:
        total = item_price * numitems
    elif 10 <= item_price <= 20:
        total = item_price * numitems * 0.95  # 5% discount
    else:  # item_price > 20
        total = item_price * numitems * 0.90  # 10% discount

    print(f'{useritem} ${total:.2f}')
else:
    print("Item not found.")