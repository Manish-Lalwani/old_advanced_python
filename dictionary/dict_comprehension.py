
#PRICES IN DOLLARS
price_dict = {
    "milk": 100,
    "bread": 50,
    "coffee": 30
}

print(f'PRICING BEFORE CONVERSION:\n {price_dict} \n')
one_dollar = 70 #price of one dollar in rupees

indian_price_dict = {key:value*one_dollar for (key,value) in price_dict.items()}
print(f'PRICING AFTER CONVERSION (RATE 70rs):\n {indian_price_dict} \n')


#if price of product greater than 30 convert to INdian rupees:
indian_price_dict2 = {key:value*one_dollar for (key,value) in price_dict.items() if value > 30}
print(f'PRICING AFTER CONVERSION(above 30):\n {indian_price_dict2} \n')