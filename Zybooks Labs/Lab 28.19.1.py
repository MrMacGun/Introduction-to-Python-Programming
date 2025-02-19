#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/19

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

sum_of_products = 0

for i in range(len(list1)):
    sum_of_products += list1[i] * list2[i]

print(sum_of_products)

