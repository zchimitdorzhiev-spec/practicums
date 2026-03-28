def seconds_since_new_year(datetime_str):
    datetime_str = datetime_str.strip()

    if ' ' not in datetime_str or '/' not in datetime_str or ':' not in datetime_str:
        return None

    try:
        date_part, time_part = datetime_str.split()
    except ValueError:
        return None

    try:
        month, day, year = date_part.split('/')
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return None

    try:
        hour, minute, second = time_part.split(':')
        hour = int(hour)
        minute = int(minute)
        second = int(second)
    except ValueError:
        return None

    if month < 1 or month > 12:
        return None

    def is_leap_year(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    days_in_month = [31, 29 if is_leap_year(year) else 28,
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day < 1 or day > days_in_month[month - 1]:
        return None

    if year < 1 or year > 9999:
        return None

    if hour < 0 or hour > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
        return None

    days_passed = 0

    for m in range(1, month):
        days_passed += days_in_month[m - 1]

    days_passed += day - 1
    total_seconds = (days_passed * 24 * 3600) + (hour * 3600) + (minute * 60) + second
    print(total_seconds)
    return total_seconds


if __name__ == "__main__":
    result1 = seconds_since_new_year("01/01/2024 00:00:00")
    print(f"Результат: {result1}\n")

    result2 = seconds_since_new_year("12/28/2024 00:00:01")
    print(f"Результат: {result2}\n")

    result3 = seconds_since_new_year("13/01/2024 12:00:00")
    print(f"Результат: {result3}\n")

    result4 = seconds_since_new_year("02/30/2024 12:00:00")
    print(f"Результат: {result4}\n")