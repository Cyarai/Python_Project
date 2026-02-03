import random

def number_guessing(): 

    secret_number = random.randint(1, 5)
    attempt = 0

    print("""             Think a number between 1 - 20!\n""")

    while True:
        try:
            guess = int(input("Enter your Guess Number: "))
            attempt += 1

            if guess < 1 or guess > 5:
                print("Your Guess are Outside the Ranged of Number!")
            elif guess < secret_number:
                print("Too Low! Try again!")
            elif guess > secret_number:
                print("Too High! Try Again!")
            else:
                print(f"Congratulation You Got it! The secret number is {secret_number}.")
                print(f"You took {attempt} attempt to guess the correct secret number.")
                break

        except ValueError:
            print("Invalid Value! Please enter a number.")

def main():
    print("""\n             Welcome to number Guessing Game!              \n""")

    while True:
        number_guessing()
        play_again = input("Do you want to play again (yes/no): ").lower()

        if play_again != "yes":
            print("""            Thank you for playing!          """)
            break

if __name__ == "__main__":
    main()
        