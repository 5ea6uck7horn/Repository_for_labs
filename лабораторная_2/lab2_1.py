money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital  # стартовый бюджет
i = 0
while budget > spend:
    increased_spend = spend * ((1 + increase) ** i)  # траты растут каждый месяц, кроме самого первого
    budget = budget + salary - increased_spend  # бюджет уменьшается каждый месяц
    i += 1  # ещё один месяц без долгов
print("Количество месяцев, которое можно протянуть без долгов:", i)
