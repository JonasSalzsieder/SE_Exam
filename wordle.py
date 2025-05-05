print("Welcome to your daily 'Wordle'")
print("Your task is to guess a secret 5 letter word within 6 tries. Good Luck, you will need it!")
print("-----------------")

secret_word = "hello".upper()
secret_word_list = list(secret_word)
print (secret_word_list)

game_counter = 0
guess_counter = 6


while game_counter <= 5:
    
    user_input = input("Please enter your guess: ").upper()
    if user_input == secret_word:
        print("Congrats, you got it!")
        break
    elif len(user_input)<= 4:
        print("The word has not enough letters.")
    elif len(user_input) >=6:
        print("The word has to many letters.")
    elif len(user_input) == 5:
        print("Nice try.")
        guess_counter -= 1
            

        if guess_counter == 0:
                print("Out of tries")
                print(f"The word would have been {secret_word}")
            
        else:
                
                for letter in secret_word:
                    if letter in user_input:
                        print(letter + " is in the word")
                    else:
                        no_correct_letter = letter
                    
                for position in range(len(secret_word)):
                    correct_positions = []
                    correct_pos = correct_positions
                    if user_input[position] == secret_word[position]:
                        correct_positions.append(position+1)
                        print(f"You have a correct letter at position: {correct_pos}")
                
                print(f"You have {guess_counter} tries left")
        game_counter += 1
    else:
        print("Better luck next time.")



