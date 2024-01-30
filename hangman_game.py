from os import system  # Importing system from os for clearing the terminal
from time import sleep  # Importing sleep to add delays in the output
import random  # Importing random module for selecting random words

# Importing custom modules
from hangman_artwork import logo, stages  # Importing game artwork and stages
from words import dictionary  # Importing word dictionary for single player mode

# Class for the hangman game
class hangman_game:

    # Function for single player game mode
    def single_player():
        # Selecting a random word from the dictionary
        selected_word = random.choice(dictionary)

        # Storing the word as dashes
        computer_choice = ["_" for _ in selected_word]

        # Initializing lives and game state
        lives = 6
        end_of_game = False

        # Main game loop
        while not end_of_game:
            print(f"{stages[lives]}\n{computer_choice}\nYou have {lives} in this game mode")
            player_letter = input("Guess a letter ").lower()

            # Checking if the guessed letter is correct
            if player_letter in selected_word:
                print("*******************************************************************************")
                print(f"Congratulations you have guessed the correct letter which is {player_letter}")

                # Replacing dashes with correct letters
                for index, letter in enumerate(selected_word):
                    if letter == player_letter:
                        computer_choice[index] = letter

            elif player_letter not in computer_choice:
                lives -= 1
                print("*******************************************************************************")
                print(f"Letter is not in the computer word\nYou lost a life\nCurrent lives left {lives}")

            # Checking if the player has won
            if "_" not in computer_choice:
                print("*******************************************************************************")
                print(f"Congratulations you have won the game\nThe word you needed to guess was {selected_word}\n{stages[lives]}\nGAME OVER")
                end_of_game = True

            # Checking if the player has lost
            if lives == 0:
                end_of_game = True
                print(f"Game Over\n{stages[lives]}")

    # Function for multiplayer game mode
    def multiplayer():
        # Getting player names and words to be guessed
        player1_name = input("Player 1, enter your name =>")
        player2_name = input("Player 2, enter your name =>")
        five_words = [input(f"Word {i + 1}. =>").lower() for i in range(5)]

        # Selecting a word to be guessed
        selected_word = random.choice(five_words)
        words_to_be_guessed = ["_" for _ in selected_word]
        lives = 6
        end_of_game = False

        # Main game loop
        while not end_of_game:
            print(f"{stages[lives]}\n{words_to_be_guessed}\nYou have {lives} in this game mode")
            player2_letter = input("Guess a letter =>").lower()

            # Checking if the guessed letter is correct
            if player2_letter in selected_word:
                print("*******************************************************************************")
                print(f"Congratulations you have guessed the correct letter which is {player2_letter}")

                # Replacing dashes with correct letters
                for index, letter in enumerate(selected_word):
                    if letter == player2_letter:
                        words_to_be_guessed[index] = letter

            elif player2_letter not in selected_word:
                lives -= 1
                print("*******************************************************************************")
                print(f"{stages[lives]}\nLetter is not in the computer word\n{stages[lives]}")

            # Checking if the player has won
            if "_" not in words_to_be_guessed:
                print("******************************************************************************************")
                print(f"Congratulations {player1_name} you have won the game\n{player2_name} lost the game\nThe word you needed to guess was {selected_word}\nCurrent lives are {lives}\n{stages[lives]}")
                end_of_game = True
                
            # Checking if the player has lost
            if lives == 0:
                end_of_game = True
                print(f"Game Over\nYou have {lives} lives left")

    # Function to display hangman game rules
    def hangman_game_rules():
        print(f"Fill in the letter everywhere it appears on the appropriate dash (or dashes) each time the person guesses correctly. Circle the letter on the alphabet if is guessed correctly.\nAdd one body part to the drawing each time the letter chosen is not in the word. Begin by drawing a head attached to the short vertical line (the noose).\nAdd eyes, ears, nose, hair, body, legs, and arms. Put an X through the letter that was guessed and not correct. You may also wish to make your drawings very elaborate - one ear at a time, a neck, and a belly button\n- so that children will have a lot of guesses before losing. If the drawing of the person is completed before the word or words are guessed,\nthe guessing player loses. If the player figures out the word or words first, he or she wins.\nYou only have 6 lives to guess the word")
        sleep(5)

        clear = input("Type 'NEXT' to exit the rules page =>").lower()
        
        if clear == "next":
            system('cls')
        else:
            print("Invalid option")

# Displaying the game logo and prompting user for game choice
print(logo)
game_choice = input(f"Welcome to hangman. Would you like to play the game\n==================================================================\nType 'YES' to play and 'NO' to exit =>").lower()

if game_choice == "yes":
    game_mode_choice = input("Would you like to player single player mode or against a friend\nType 'SINGLE PLAYER' to play against the computer or 'MULTIPLAYER' to play against your friend =>").lower()
    
    if game_mode_choice == "single player":
        hangman_game.hangman_game_rules()
        hangman_game.single_player()
    elif game_mode_choice == "multiplayer":
        hangman_game.hangman_game_rules()
        hangman_game.multiplayer()
    else:
        print(f"You have entered an invalid option\nThanks for coming")

elif game_choice == "no":
    print(f"Thanks for coming")
else:
    print(f"You have entered an invalid option\nThanks for coming")
