#A local pizza shop is selling a large pizza for $9.99. Given the number of pizzas to order as input, output the subtotal for the pizzas, and then output the total after applying a sales tax of 6%.

uint = int(input())
sub_total = uint * 9.99
sales_tax = sub_total + (sub_total * .06)

print(f'Subtotal: ${sub_total:.2f}')
print(f'Total due: ${sales_tax:.2f}')

