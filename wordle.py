print("Welcome to your daily 'Wordle'")
print("Your task is to guess a secret 5 letter word within 6 tries. Good Luck, you will need it!")
print("-----------------")

secret_word = "Hello"

game_counter = 0

while game_counter <= 6:
    user_input = input("Please enter your guess: ")
    if len(user_input)<= 4:
        print("The word has not enough letters.")
    elif len(user_input) >=6:
        print("The word has to many letters.")
    elif len(user_input) == 5:
        print("nice try.")
        print(f"You have  tries left")
        game_counter =+ 1
    else:
        print("This is not a correct input")