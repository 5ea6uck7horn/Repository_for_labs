money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital  # стартовый бюджет
i = 0
while budget + salary > spend * ((1 + increase) ** i):
    budget = budget + salary - spend * ((1 + increase) ** i)  # бюджет уменьшается каждый месяц
    i += 1  # ещё один месяц без долгов
print("Количество месяцев, которое можно протянуть без долгов:", i)
