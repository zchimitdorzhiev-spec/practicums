def sale():
    price = int(input('Введите сумму покупки: '))
    sale_percent = 0

    print('У вас есть дисконтная карта?')
    discontcard = input()
    if discontcard.lower() == 'да':
        sale_percent += 0.05

    print('Сегодня праздничный день?')
    public_holiday = input()
    if public_holiday.lower() == 'да':
        sale_percent += 0.03

    if 5000 <= price < 15000:
        sale_percent += 0.03
    elif 15000 <= price < 20000:
        sale_percent += 0.05
    elif 20000 <= price < 30000:
        sale_percent += 0.07
    elif price >= 30000:
        sale_percent += 0.1

    if sale_percent > 0.15:
        sale_percent = 0.15

    total_price = price * (1 - sale_percent)

    print(f'Сумма со скидкой: {total_price:.2f} руб.')
    print(f'Скидка составила: {sale_percent * 100:.0f}%')

    return total_price


sale()