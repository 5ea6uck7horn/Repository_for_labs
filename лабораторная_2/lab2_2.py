salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

minimal_needed_budget = 0
for i in range(months):
    increased_spend = spend * ((1 + increase) ** i)
    minimal_needed_budget += increased_spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(-1 * minimal_needed_budget // 1 * -1))

