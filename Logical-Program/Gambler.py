import random

stake = int(input("Enter stake: "))
goal = int(input("Enter goal: "))
trials = int(input("Enter number of trials: "))
bet = int(input("Enter bet amount: "))

wins = 0
total_win = 0
total_loss = 0

for i in range(trials):
    cash = stake
    print("\n--- Trial", i + 1, "started ---")

    if cash <= 0:
        print("No money to play.")
    else:
        while cash > 0:
            if random.random() < 0.5:
                cash += bet
                total_win += bet
                print("Won:", bet, ", Current Cash:", cash)
            else:
                cash -= bet
                total_loss += bet
                print("Lost:", bet, ", Current Cash:", cash)

            if cash >= goal:
                break

    print("Trial", i + 1, "ended with cash:", cash)

    if cash >= goal:
        print("Result: win")
        wins += 1
    else:
        print("Result: loss ")

print("\nFinal Results ----------------------")
print("Total Wins:", wins)
print("Total Loss Trials:", trials - wins)
print("Total Winning Amount:", total_win)
print("Total Losing Amount:", total_loss)
