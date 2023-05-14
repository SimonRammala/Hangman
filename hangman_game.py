# import only system from os
from os import system
 
# import sleep to show output for some time period
from time import sleep

import random
from hangman_artwork import logo,stages

class hangman_game:
    #function for a single player game mode, player against the computer
    def single_player():
        #used import the words file to my project
        from words import dictionary
        #used to select a random word from the words file
        selected_word = random.choice(dictionary)

        #used to store the word in the from dashes
        computer_choice=[]

        #used to add or append the letter of the computer word
        for t in selected_word:
            computer_choice.append("_")

        lives = 6

        end_of_game = False

        #used to loop the game till a result has been given
        while (not end_of_game):
            
            print(f"{stages[lives]}\n{computer_choice}\nYou have {lives} in this game mode")
            player_letter = input("Guess a letter ").lower()

            if player_letter in selected_word:
                print("*******************************************************************************")
                print(f"Congratulations you have guessed the correct letter which is {player_letter}")
                
            
                for postin in range(len(selected_word)):
                    letter = selected_word[postin]

                    if(letter == player_letter):
                        computer_choice[postin] = letter
                        
            elif (player_letter not in computer_choice):
                lives-=1
                print("*******************************************************************************")
                print(f"Letter is not in the computer word\nYou lost a life\nCurrent lives left {lives}")

            if "_" not in computer_choice:
                print("*******************************************************************************")
                print("Game over")
                end_of_game = True

            if lives == 0:
                end_of_game = True
                print(f"Game Over\nYou have {lives} lives left")

            
    def multiplayer():
        amount_of_words = 1
        five_word = []
        words_to_be_guess = []
    
        end_of_game = False
        lives = 6

        playe1_name = input(f"Player 1,enter your name =>")
        player2_name = input("Player 2, enter your name =>")

        while (amount_of_words <= 5 ):
            player_1 = input(f"Enter a word that the player needs to guess {amount_of_words} =>").lower()

            five_word.append(player_1)
            amount_of_words+=1
        #used to clear the terminal window
        system('cls')
        selected_word = random.choice(five_word)


        for x in selected_word:
            words_to_be_guess.append("_")

        while(not end_of_game):
            
            player_2_letter=input("Guess a letter =>").lower()

            if(player_2_letter in selected_word):
                print(f"Congratulations you have guessed the correct letter which is {player_2_letter}")

                for index in range(len(selected_word)):
                    letter = selected_word[index]

                    if(letter == player_2_letter):
                        words_to_be_guess[index] = letter
                print(words_to_be_guess)        

            elif(player_2_letter not in selected_word):
                lives -=1
                print("*******************************************************************************")
                print(f"{stages[lives]}\nLetter is not in the computer word\n{stages[lives]}")
            
            if "_" not in words_to_be_guess:
                print(f"{stages[lives]}\nCongratulations {playe1_name} you have won the game\n{player2_name} lost the game\nCurrent lives are {lives}")
                end_of_game= True
                
            
            if lives == 0:
                end_of_game = True
                print(f"Game Over\nYou have {lives} lives left")




    #used to print the game rules for the player
    def hangman_game_rules():
        print(f"Fill in the letter everywhere it appears on the appropriate dash (or dashes) each time the person guesses correctly. Circle the letter on the alphabet if is guessed correctly.\nAdd one body part to the drawing each time the letter chosen is not in the word. Begin by drawing a head attached to the short vertical line (the noose).\nAdd eyes, ears, nose, hair, body, legs, and arms. Put an X through the letter that was guessed and not correct. You may also wish to make your drawings very elaborate - one ear at a time, a neck, and a belly button\n- so that children will have a lot of guesses before losing. If the drawing of the person is completed before the word or words are guessed,\nthe guessing player loses. If the player figures out the word or words first, he or she wins.\nYou only have 6 lives to guess the word")
        sleep(5)

        clear = input("Type 'NEXT' to exit the rules page").lower()
        
        if(clear == "next"):
            #used to clear the terminal window
            system('cls')
        else:
            print("Invalide option")



print(logo)
game_choice = input(f"Welcome to hangman. Would you like to play the game\n==================================================================\nType 'YES' to play and 'NO' to exit =>").lower()

if(game_choice == "yes"):
    game_mode_choice = input("Would you like to player single player mode or agaist a friend\nType 'SINGLE PLAYER' to play against the computer or 'MULTIPLAYER' to play aganist you friend =>").lower()
    
    if(game_mode_choice == "single player"):
        hangman_game.hangman_game_rules()
        
        hangman_game.single_player()
    elif(game_mode_choice == "multiplayer"):
        hangman_game.hangman_game_rules()
        
        hangman_game.multiplayer()
    else:
        print(f"You have enterd an invalide option\nThanks for coming")

elif(game_choice == "no"):
    print(f"Thanks for coming")

else:
    print(f"You have enterd an invalide option\nThanks for coming")


