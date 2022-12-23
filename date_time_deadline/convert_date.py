from datetime import datetime
from birdseye import eye


@eye
def convert_to_date(date):
    # print(type("akash"))
    date1 = datetime.strptime(date, "%d.%m.%Y")
    # print(type(date))
    return date1

# # user_date = int(30.12.2022)
# date = input("Enter date")
# print(datetime.strptime("20.12.2022", "%d.%m.%Y"))
# # print(datetime(2022, 12, 20))

print(convert_to_date("30.12.2022"))
