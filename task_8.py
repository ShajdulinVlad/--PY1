money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

#  В случае, если мы полагаемся только на подушку безопасности
while money_capital >= spend:
    month += 1
    money_capital += (salary - spend)
    spend *= (1 + increase)
print(month)

#  В случае, если расходы идут после получения зарплаты
"""while (money_capital + salary) >= spend:
    month += 1
    money_capital += (salary - spend)
    spend *= (1 + increase)
print(month)"""
