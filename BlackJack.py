import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def blackjack():
    player_hand = []
    computer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while computer_score!= 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if player_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif player_score == computer_score:
        return "It's a draw!"
    elif player_score == 0:
        return "Blackjack! You win!"
    elif computer_score == 0:
        return "Computer got a Blackjack. You lose!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

print(blackjack())