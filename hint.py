secret_word = "hello"



user_input = input("Please enter your guess: ")

correct_positions = []




for letter in secret_word:
    if letter in user_input:
        print(letter + " is in the word")

for position in range(len(secret_word)):
    if user_input[position] == secret_word[position]:
        correct_positions.append(position)
        print(correct_positions)

for index, position in enumerate(correct_positions):
    human_index = index +1
    print (human_index)