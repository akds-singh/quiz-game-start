############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and dealer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the dealer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

# from art import logo
import random

from replit import clear

# print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Defining function to randomly select card(s).
def deal_card(times_count):
    random_card = []
    for i in range(times_count):
        random_card.append(random.choice(cards))
    return random_card


# Defining function to calculate the sum of cards values.
def card_score(selected_card):
    total_score = 0
    for value in selected_card:
        total_score += value

    if 11 in selected_card and total_score > 21:
        return total_score - 11 + 1
    else:
        return total_score


# Defining function to get the Status of the score i.e, is score under 21, over 21 or equal to 21.
def score_status(score):
    if score > 21:
        over_21 = True
        under_21 = False
        score_21 = False
        return over_21, under_21, score_21
    elif score == 21:
        over_21 = False
        under_21 = False
        score_21 = True
        return over_21, under_21, score_21
    else:
        over_21 = False
        under_21 = True
        score_21 = False
        return over_21, under_21, score_21


def black_jack():
    want_to_play = input("Want to play Black-Jack? Type 'y' for yes or 'n' for no: ")

    dealer_card = []
    mine_card = []
    dealer_score = []
    mine_score = []

    if want_to_play == 'y':
        dealer_card += deal_card(2)
        dealer_score = card_score(dealer_card)

        mine_card += deal_card(2)
        mine_score = card_score(mine_card)
    elif want_to_play == 'n':
        print("end the game:")

    print(f"Computer Card: {dealer_card} and computer Score: {dealer_score}")
    print(f"Your card: {mine_card} and Your Score: {mine_score}")

    score_under_21 = True
    while score_under_21:
        another_card = input("Enter 'y' to select next card or 'n' to Pass: ")

        if another_card == 'y':
            mine_card += deal_card(1)
            mine_score = card_score(mine_card)
        elif another_card == 'n':
            if dealer_score > mine_score:
                print("Computer win")
                break
            else:
                dealer_card += deal_card(1)
                dealer_score = card_score(dealer_card)

        print(f"Computer Card: {dealer_card} and computer Score: {dealer_score}")
        print(f"Your card: {mine_card} and Your Score: {mine_score}")

        print(score_under_21)

        over_21, score_under_21, score_21 = score_status(dealer_score)
        if score_21:
            print("Jack-pot , Computer win")
        elif over_21:
            print("Computer Lose: ")

        over_21, score_under_21, score_21 = score_status(mine_score)
        if score_21:
            print("jack-pot, You win")
        elif over_21:
            print("You lose: ")

        print(score_under_21)

    clear()
    black_jack()


black_jack()
