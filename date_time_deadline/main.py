from convert_date import convert_to_date
import calculate_remaining_days
from datetime import datetime


def main():
    user_input = input("Enter your goal and its deadline DATE\n")
    user_list = user_input.split(":")
    # user_input[1] = int(user_list[1])
    dead_line = user_list[1]
    print(type(user_list[0]))
    print(user_list)
    # date1 = datetime.strptime(user_list[1], "%d.%m.%Y")
    # date2 = date1 - datetime.today()

    # print(datetime.strptime(user_list[1], "%d.%m.%Y"))
    dead_line_date = convert_to_date(dead_line)
    remaining_days = calculate_remaining_days.calculate_days(dead_line_date)

    # print("Dear User! Time remaining for your goal to ", user_list[0], date2.days, "days")
    print("Dear User! Time remaining for your goal to ", user_list[0], remaining_days.days, "days")


main()
