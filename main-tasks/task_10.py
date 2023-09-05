prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'],
         ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

def prods_total(products):
    total_stock = 0
    for prod in products:
        stock = int(prod[2])
        total_stock += stock
    return total_stock

total_stock = prods_total(prods)
print("The total stock in the company is:", total_stock)

# total_stock = 0
# for prod in prods:
#     stock = int(prod[2])
#     total_stock += stock
#     result=("The total stock in the company is:", total_stock)
# print(result)