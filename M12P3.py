last_name = input("Enter the salesperson's last name: ")
sales = float(input("Enter the sales amount: "))
def calculate_commission(sales):
    if sales > 100000:
        commission = sales * 0.10
    elif sales <= 100000:
        commission = sales * 0.05
    nextyear_target = sales * .05

    return nextyear_target, commission
nextyear_target, commission = calculate_commission(sales)
print("Next Year Target:", nextyear_target)
print("Commission:", commission)
print("Salesperson Last Name:", last_name)