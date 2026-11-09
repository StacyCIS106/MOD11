quantity = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price: "))
def calculate_total(quantity, unit_price):
    global total
    total = quantity * unit_price
    global tax
    tax = total * 0.07

    return total + tax

total = calculate_total(quantity, unit_price)
print("Total Price:", total)
print("Tax:", tax)
print("Total Price with Tax:", total + tax)