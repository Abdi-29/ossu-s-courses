annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

r = 0.04
portion_down_payment = 0.25 * total_cost
current_saving = 0
annual_return = current_saving * r / 12
month = 0

while(portion_down_payment >= current_saving):
    monthly = annual_salary / 12
    current_saving += (monthly * portion_saved) + (current_saving * r / 12)
    if month >= 6 and month % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)
    month += 1
print('Number of months: ', month)    