monthes = ["январь", "февраль", "март",
           "апрель", "май", "июнь",
           "июль", "август", "сентябрь",
           "октябрь", "ноябрь", "декабрь"]

dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #days in month


def sim(dim): #steps in month
    with open('input.txt', 'r', encoding='utf-8') as sf:
        steps = [int(line.strip()) for line in sf.readlines()]

    monthly_averages = []
    start_idx = 0

    for days in dim:
        # Берем шаги за текущий месяц
        month_steps = steps[start_idx:start_idx + days]
        # Вычисляем среднее (целочисленное деление //)
        avg = sum(month_steps) // days
        monthly_averages.append(avg)
        # Сдвигаем индекс начала следующего месяца
        start_idx += days
    return monthly_averages

with open('output.txt', 'w', encoding='utf-8') as bh:
    for i, j in zip(dim, monthes):
        a = i.sim()
        bh.write(f'{j}, {a}')