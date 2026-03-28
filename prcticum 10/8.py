def convert_datetime(datetime_str):
    datetime_str = datetime_str.strip()

    if ' ' not in datetime_str or '/' not in datetime_str or ':' not in datetime_str:
        return

    try:
        date_part, time_part = datetime_str.split()
    except ValueError:
        return

    try:
        month, day, year = date_part.split('/')
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return

    try:
        hour, minute, second = time_part.split(':')
        hour = int(hour)
        minute = int(minute)
        second = int(second)
    except ValueError:
        return

    if month < 1 or month > 12:
        return

    days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day < 1 or day > days_in_month[month - 1]:
        return

    if year < 1 or year > 9999:
        return

    if hour < 0 or hour > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
        return

    if hour == 0:
        hour_12 = 12
        am_pm = "AM"
    elif hour < 12:
        hour_12 = hour
        am_pm = "AM"
    elif hour == 12:
        hour_12 = 12
        am_pm = "PM"
    else:
        hour_12 = hour - 12
        am_pm = "PM"

    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year % 100:02d}"
    time_str = f"{hour_12:02d}:{minute:02d}:{second:02d} {am_pm}"
    result = f"{day_str}.{month_str}.{year_str} {time_str}"
    print(result)


if __name__ == "__main__":
    convert_datetime("12/04/1990 13:12:12")
    convert_datetime("01/15/2023 00:05:30")
    convert_datetime("02/29/2020 12:00:00")
    convert_datetime("122/04/1990 13:12:12")
    convert_datetime("02/30/2021 13:12:12")
    convert_datetime("12/04/1990 25:12:12")
    convert_datetime("12/04/1990 13:61:12")
    convert_datetime("12/04/1990 13:12:99")
    convert_datetime("12-04-1990 13:12:12")
    convert_datetime("12/04/1990 13:12")