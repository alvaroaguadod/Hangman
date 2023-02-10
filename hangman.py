import random

def play_hangman():
    print("\n\nWelcome to\n")
    print("H A N G M A N")
    
    #Create the elements
    words = ["python", "java", "kotlin", "javascript", "ruby", "rust", "flutter", "php", "bash", "cobol", "pascal", "dart"] 
    
    #Function to chose randomly an element
    word = random.choice(words)
    
    #Function to display in screen the guides for the player
    hidden_word = list("-" * len(word))
    #Amount of attempts to guess the word 
    tries = 8
    #List of letters that the player has already tried
    used_letters = set()

    #While Loop with our functions to create the game
    while tries > 0:
        print(f"\nYou still have {tries} tries. \n")
        print("\n" + "".join(hidden_word))
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not letter.islower():
            print("It is not an ASCII lowercase letter")
            continue
        if letter in used_letters:
            print("You already typed this letter")
            continue
        used_letters.add(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            if "".join(hidden_word) == word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                break
        else:
            print("No such letter in the word")
            tries -= 1

    if tries == 0:
        print("You are hanged!")

while True:
    play_hangman()
    again = input('Do you want to play again? (yes/no) ')
    if again == 'no':
        break
    elif again == 'yes':
        print("\nFirst time? :)")