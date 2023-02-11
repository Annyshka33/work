# import itertools
from datetime import date, timedelta


def calculate_working_dates(date_start, date_end, days_work, days_skip):
    dates = []
    if days_work == 0: return dates
    while date_start <= date_end:
        days_work_range = min(days_work, (date_end - date_start).days + 1)
        dates += [str(date_start + timedelta(days=i)) for i in range(days_work_range)]
        date_start += timedelta(days = days_work + days_skip)
    return dates


tests = [(date(2022, 4, 20), date(2022, 4, 23), 1, 1),
         (date(2022, 4, 25), date(2022, 6, 26), 0, 4),
         (date(2022, 5, 14), date(2022, 5, 24), 1, 95),
         (date(2022, 5, 14), date(2022, 5, 24), 100, 9),
         (date(2023, 2, 10), date(2023, 2, 25), 2, 1)]
for date_start, date_end, days_work, days_skip in tests:
    print("\nПочаткова дата:", date_start)
    print("Кінцева дата:", date_end)
    print("Робочі дні:", days_work)
    print("Дні відпочинку:", days_skip)
    working_dates = calculate_working_dates(date_start, date_end, days_work, days_skip)
    print("Робочі дати:", working_dates)
