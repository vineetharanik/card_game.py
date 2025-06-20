import itertools
import random

# Setup deck and rank values
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
rank_value = {r: i+2 for i, r in enumerate(ranks)}
deck = list(itertools.product(ranks, suits))
random.shuffle(deck)

# Deal 5 cards each
player_hand = deck[:5]
computer_hand = deck[5:10]

# Initialize scores
player_score = 0
computer_score = 0

print("🎮 Welcome to the 5-Round Card Game!\n")

# Play 5 rounds
for round_num in range(1, 6):
    print(f"\n--- Round {round_num} ---")
    print("Your cards:")
    for i, card in enumerate(player_hand):
        print(f"{i + 1}. {card}")

    # Player chooses a card
    while True:
        try:
            choice = int(input("Choose a card to play (1-{}): ".format(len(player_hand)))) - 1
            if 0 <= choice < len(player_hand):
                break
            else:
                print("❌ Invalid choice, try again.")
        except ValueError:
            print("❌ Please enter a number.")

    player_card = player_hand.pop(choice)

    # Computer chooses a random card
    computer_card = computer_hand.pop(random.randint(0, len(computer_hand) - 1))

    print("🧍 You played:", player_card)
    print("🤖 Computer played:", computer_card)

    # Compare card values
    p_val = rank_value[player_card[0]]
    c_val = rank_value[computer_card[0]]

    if p_val > c_val:
        print("✅ You win this round!")
        player_score += 1
    elif p_val < c_val:
        print("❌ Computer wins this round!")
        computer_score += 1
    else:
        print("😐 It's a tie!")

    print(f"🎯 Score: You - {player_score} | Computer - {computer_score}")

# Final result
print("\n🏁 Game Over!")
if player_score > computer_score:
    print("🎉 You won the game!")
elif player_score < computer_score:
    print("💻 Computer won the game!")
else:
    print("🤝 It's a tie game!")
