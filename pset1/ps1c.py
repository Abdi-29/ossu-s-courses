# user input
annual_salary = float(input('Enter your annual salary: '))
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
steps = 0
current_savings = 0
low = 0
high = 10000
guess_rate = (high + low)//2
while abs(current_savings - total_cost*portion_down_payment) >= 100:
    current_savings = 0
    for_annual_salary = annual_salary
    rate = guess_rate/10000
    for month in range(36):
        if month % 6 == 0 and month > 0:
            for_annual_salary += for_annual_salary*semi_annual_raise
        monthly_salary = for_annual_salary/12
        current_savings += monthly_salary*rate+current_savings*r/12
    if current_savings < total_cost*portion_down_payment:
        low = guess_rate
    else:
        high = guess_rate
    guess_rate = (high + low)//2
    steps += 1
    if steps > 13:
        break
if steps > 13:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:', rate)
    print('Steps in bisection search:', steps)  