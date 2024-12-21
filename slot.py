# python slot mmachine

import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "💰", "⭐"]
    # results = []
    # for symbol in symbols:
    #     results.append(random.choice(symbol))

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")
    

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "💰":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0


def main():
    balance = 1000

    print("************************")
    print("Welcome to vegas Slot!")
    print("Symbol: 🍒 🍉 🍋 💰 ⭐")
    print("************************")


    while balance > 0:
        print(f"current balance: ${balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input! Please enter a number.")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost your bet.")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()
        
        if play_again != "Y":
            break


    print("*********************************************************")
    print(f"Thank you for playing! Your final balance is ${balance}.")
    print("*********************************************************")


if __name__ == "__main__":
    main()