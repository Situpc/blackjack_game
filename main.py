import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

all_values = {"user_values": [], "computer_values": []}


def clear_list():
    all_values["user_values"] = []
    all_values["computer_values"] = []


def less_value_computer(number):
    if number < 17:
        random_card_appended("computer_values")
        add_all_values("computer_values")
        number = add_all_values("computer_values")


def card_check_values(user_key, user_values, computer_key, computer_values):

    if add_all_values(user_key) == 21:
        less_value_computer(add_all_values("computer_values"))

        display_final_cards_values(user_key, computer_key, user_values,
                                   computer_values)
        print("Blackjack! You win!")

    elif add_all_values(user_key) < 21 and add_all_values(computer_key) > 21:
        less_value_computer(add_all_values("computer_values"))

        display_final_cards_values(user_key, computer_key, user_values,
                                   computer_values)
        print("You win. The computer went over.")

    elif add_all_values(user_key) < 21 and add_all_values(
            user_key) > add_all_values(computer_key):
        less_value_computer(add_all_values("computer_values"))

        display_final_cards_values(user_key, computer_key, user_values,
                                   computer_values)
        print("You win. You were closer to 21!")

    elif add_all_values(user_key) < 21 and add_all_values(
            user_key) < add_all_values(computer_key):
        less_value_computer(add_all_values("computer_values"))

        display_final_cards_values(user_key, computer_key, user_values,
                                   computer_values)
        print("You lost. The computer is closer to 21!")

    elif add_all_values(computer_key) == add_all_values(computer_key):
        less_value_computer(add_all_values("computer_values"))

        display_final_cards_values(user_key, computer_key, user_values,
                                   computer_values)
        print("It's a draw.")

    clear_list()


def random_card_appended(key):
    return all_values[key].append(random.choice(cards))


def add_all_values(key):
    start_value = 0
    x = 0
    for numbers in all_values[key]:
        if start_value + 11 > 21 and numbers == 11:
            for i in range(len(all_values[key])):
                if all_values[key][i] == 11:
                    x += 1
                    if x <= 1:
                        all_values[key][i] = 1
                    elif x > 1:
                        all_values[key][i] = 1

                numbers = 1
        start_value += numbers
    return start_value


def display_final_cards_values(user_key, computer_key, user_values,
                               computer_values):

    print(
        f"Your final hand: {all_values[user_key]}, Your final score: {user_values}"
    )
    print(
        f"Computer's final hand: {all_values[computer_key]}, Computer's final score: {computer_values}"
    )


def display_cards_values(user_key, user_values):
    print(f"Your cards: {all_values[user_key]}, Current score: {user_values}")
    computer_first_card = all_values["computer_values"][0]
    print(f"Computer's first card: {computer_first_card}")


def start_blackjack():

    print(art.logo)
    for i in range(2):
        random_card_appended("user_values")
        random_card_appended("computer_values")

    display_cards_values("user_values", add_all_values("user_values"))


def the_while_loop():
    start_blackjack()
    user_choice = True
    while user_choice == True:
        user_dec = input("Press 'y' to get another card, type 'n' to pass:\n")

        if user_dec == "y":

            random_card_appended("user_values")
            add_all_values("user_values")

            display_cards_values("user_values", add_all_values("user_values"))

            if add_all_values("user_values") > 21:

                less_value_computer(add_all_values("computer_values"))

                display_final_cards_values("user_values", "computer_values",
                                           add_all_values("user_values"),
                                           add_all_values("computer_values"))

                print("You lose. You went over")

                clear_list()
                user_start()

            elif add_all_values("computer_values") == 21:

                display_final_cards_values("user_values", "computer_values",
                                           add_all_values("user_values"),
                                           add_all_values("computer_values"))

                print("The computer got BlackJack! You lose")

                clear_list()
                user_start()

        elif user_dec == "n":
            less_value_computer(add_all_values("computer_values"))

            card_check_values("user_values", add_all_values("user_values"),
                              "computer_values",
                              add_all_values("computer_values"))

            clear_list()
            user_choice = False
            user_start()


def user_start():
    user_decision = input(
        "Do you want to play blackjack? type 'y' for yes or type 'n' for no: \n"
    )
    if user_decision == 'y':
        the_while_loop()
    elif user_decision == 'n':
        print("We're done.")


user_start()
