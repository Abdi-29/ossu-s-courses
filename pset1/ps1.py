annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

r = 0.04
portion_down_payment = 0.25 * total_cost
current_saving = 0
annual_return = current_saving * r / 12
portion_saved = (annual_salary / 12) * portion_saved
month = 0

while(portion_down_payment >= current_saving):
    
    current_saving += (current_saving * r / 12) + portion_saved
    month += 1
print('Number of months: ', month)    