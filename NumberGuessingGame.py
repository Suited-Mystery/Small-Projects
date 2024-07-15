import random

very_easy_wins = 0
easy_wins = 0
medium_wins = 0
hard_wins = 0
extreme_wins = 0

very_easy_guesses = 0
easy_guesses = 0
medium_guesses = 0
hard_guesses = 0
extreme_guesses = 0

def personal_best_stats():
    print("\nPersonal Best Stats:")
    print("1. Very Easy Stats")
    print("2. Easy Stats")
    print("3. Medium Stats")
    print("4. Hard Stats")
    print("5. Extreme Stats")
    choice = input()
    if choice == "1":
        print(f"Win(s) in Very Easy Difficulty: {very_easy_wins}\nGuesses: {very_easy_guesses}")
    elif choice == "2":
        print(f"Win(s) in Easy Difficulty: {easy_wins}\nGuesses: {easy_guesses}")
    elif choice == "3":
        print(f"Win(s) in Medium Difficulty: {medium_wins}\nGuesses: {medium_guesses}")
    elif choice == "4":
        print(f"Win(s) in Hard Difficulty: {hard_wins}\nGuesses: {hard_guesses}")
    elif choice == "5":
        print(f"Win(s) in Extreme Difficulty: {extreme_wins}\nGuesses: {extreme_guesses}")
    else:
        print("Please enter a valid choice")


def number_guessing_game():
    while True:
        print("Choose game difficulty:")
        print("1. Very Easy")
        print("2. Easy")
        print("3. Medium")
        print("4. Hard")
        print("5. Extreme")
        answer = input("Choice: ")
        if answer == "1":
            attempts = 0
            num_to_guess = random.randint(1, 10)
            print("Im thinking of a number between 1 to 10")
            while True:
                num_guess = input("Take a guess: ")
                try:
                    num_guess = int(num_guess)
                except ValueError:
                    print("Please enter a number")
                    continue
                attempts += 1

                if num_guess > num_to_guess:
                    print("Too high")
                elif num_guess < num_to_guess:
                    print("Too low")
                else:
                    global very_easy_guesses
                    if very_easy_guesses == 0:
                        very_easy_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {attempts} guesses")
                    elif attempts < very_easy_guesses:
                        very_easy_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {very_easy_guesses} guesses")
                    else:
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour personal best is {very_easy_guesses} guesses")
                    global very_easy_wins 
                    very_easy_wins += 1
                    print(f"You now have {very_easy_wins} win(s) in Very Easy Difficulty")
                    main()
        elif answer == "2":
            attempts = 0
            num_to_guess = random.randint(1, 50)
            print("Im thinking of a number between 1 to 50")
            while True:
                num_guess = input("Take a guess: ")
                try:
                    num_guess = int(num_guess)
                except ValueError:
                    print("Please enter a number")
                    continue
                attempts += 1

                if num_guess > num_to_guess:
                    print("Too high")
                elif num_guess < num_to_guess:
                    print("Too low")
                else:
                    global easy_guesses
                    if easy_guesses == 0:
                        easy_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {attempts} guesses")
                    elif attempts < easy_guesses:
                        easy_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {easy_guesses} guesses")
                    else:
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour personal best is {easy_guesses} guesses")
                    global easy_wins
                    easy_wins += 1
                    print(f"You now have {easy_wins} win(s) in Easy Difficulty")
                    main()
        elif answer == "3":
            attempts = 0
            num_to_guess = random.randint(1, 100)
            print("Im thinking of a number between 1 to 100")
            while True:
                num_guess = input("Take a guess: ")
                try:
                    num_guess = int(num_guess)
                except ValueError:
                    print("Please enter a number")
                    continue
                attempts += 1

                if num_guess > num_to_guess:
                    print("Too high")
                elif num_guess < num_to_guess:
                    print("Too low")
                else:
                    global medium_guesses
                    if medium_guesses == 0:
                        medium_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {attempts} guesses")
                    elif attempts < medium_guesses:
                        medium_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {medium_guesses} guesses")
                    else:
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour personal best is {medium_guesses} guesses")
                    global medium_wins
                    medium_wins += 1
                    print(f"You now have {medium_wins} win(s) in Medium Difficulty")
                    main()
        elif answer == "4":
            attempts = 0
            num_to_guess = random.randint(1, 500)
            print("Im thinking of a number between 1 to 500")
            while True:
                num_guess = input("Take a guess: ")
                try:
                    num_guess = int(num_guess)
                except ValueError:
                    print("Please enter a number")
                    continue
                attempts += 1

                if num_guess > num_to_guess:
                    print("Too high")
                elif num_guess < num_to_guess:
                    print("Too low")
                else:
                    global hard_guesses
                    if hard_guesses == 0:
                        hard_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {attempts} guesses")
                    elif attempts < hard_guesses:
                        hard_guesses = attempts
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {hard_guesses} guesses")
                    else:
                        print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour personal best is {hard_guesses} guesses")
                    global hard_wins
                    hard_wins += 1
                    print(f"You now have {hard_wins} win(s) in Hard Difficulty")
                    main()
        elif answer == "5":
            attempts = 0
            num_to_guess = random.randint(1, 1000)
            if medium_wins < 10 and hard_wins < 2:
                print("You need at least 10 medium wins and 2 hard wins in order to play in this difficulty")
            else:
                print("Im thinking of a number between 1 to 1000")
                while True:
                    num_guess = input("Take a guess: ")
                    try:
                        num_guess = int(num_guess)
                    except ValueError:
                        print("Please enter a number")
                        continue
                    attempts += 1

                    if num_guess > num_to_guess:
                        print("Too high")
                    elif num_guess < num_to_guess:
                        print("Too low")
                    else:
                        global extreme_guesses
                        if extreme_guesses == 0:
                            extreme_guesses = attempts
                            print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {attempts} guesses")
                        elif attempts < extreme_guesses:
                            extreme_guesses = attempts
                            print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour new personal best is {extreme_guesses} guesses")
                        else:
                            print(f"\nCongratulations! You have guessed the number in {attempts} attempt(s).\nYour personal best is {extreme_guesses} guesses")
                        global extreme_wins
                        extreme_wins += 1
                        print(f"You now have {extreme_wins} win(s) in Extreme Difficulty")
                        main()

def main():
    while True:
        print("\nWelcome to The Number Guessing Game!")
        print("Choose an option:")
        print("1. Play")
        print("2. View Stats")
        print("3. Quit")
        answer = input()

        if answer == "1":
            number_guessing_game()
        elif answer == "2":
            personal_best_stats()
        elif answer == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()