secret_word = "hello"
secret_word_list = list(secret_word)


user_input = input("Please enter your guess: ")
user_input_list = list(user_input)



for i in secret_word:
    if i in user_input.lower() or user_input.upper():
        print(i + " is correct")

