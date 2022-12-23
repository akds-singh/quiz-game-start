# Program for calculater

import evaluate
from casting import my_casting_1, my_casting_2


def main():
    user_input = input("Please Enter two value to evaluate add, multiply, subtract, divide\n")
    user_list = user_input.split(" ")

    user_list[0] = my_casting_1(user_list[0])
    user_list[1] = my_casting_2(user_list[1])
    print(user_list)
    print("[0] ", user_list[0])
    print("[1] ", user_list[1])

    print("Added Value = ", evaluate.add(user_list[0], user_list[1]))
    print("Multiplied value = ", evaluate.multiply(user_list[0], user_list[1]))
    print("Subtracted value = ", evaluate.subtract(user_list[0], user_list[1]))
    print("Divided value = ", evaluate.divide(user_list[0], user_list[1]))


main()
