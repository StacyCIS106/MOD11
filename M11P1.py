quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
discount = float(input("Enter the discount: "))
def calculate_total(quantity, price, discount):
    global discount_amount
    discount_amount = quantity * price * discount
    global discount_price
    discount_price = quantity * price - discount_amount
    return discount_price, discount_amount
discount_price, discount_amount = calculate_total(quantity, price, discount)
print("Discount Price:", discount_price)
print("Discount Amount:", discount_amount)