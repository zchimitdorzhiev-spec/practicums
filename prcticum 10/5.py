def calculate_card_value():
    try:
        card_cost = float(input("Введите стоимость карты (5, 10, 25, 50, 100): "))
    except ValueError:
        print("Ошибка: введите числовое значение.")
        return None

    if card_cost == 5 or card_cost == 10:
        bonus = 0
        total_value = card_cost - bonus
    elif card_cost == 25:
        bonus = 3
        total_value = card_cost - bonus
    elif card_cost == 50:
        bonus = 8
        total_value = card_cost - bonus
    elif card_cost == 100:
        bonus = 20
        total_value = card_cost - bonus
    else:
        print("Недопустимая стоимость карты.")
        print("Допустимые значения: 5, 10, 25, 50, 100")
        return None

    print(f"Стоимость карты: ${card_cost:.2f}")
    print(f"Бонус: ${bonus:.2f}")
    print(f"Общая стоимость с бонусом: ${total_value:.2f}")

    return total_value


if __name__ == "__main__":
    result = calculate_card_value()