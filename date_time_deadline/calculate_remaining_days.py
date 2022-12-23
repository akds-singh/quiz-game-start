from datetime import datetime


def calculate_days(date):
    remaining_days = date - datetime.today()
    return remaining_days


# print(calculate_days(datetime.strptime("30.12.2022", "%d.%m.%Y")))
# d1 = calculate_days((datetime.strptime("30.12.2022", "%d.%m.%Y")))
# print(d1.days)