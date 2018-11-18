import random


def prints_instructions():
    """Prints to the player the instuctions"""

    print """Hello and welcome to Hang-Person. I'll think of a word and
    you have 6 lives to guess the letters of the word I am thinking about."""


def random_word_generator():
    """Returns a random word"""
    words = ["banana", "apple", "cherry"]

    return random.choice(words)


def prints_loss(random_word, player_name):
    """Prints to player that they lost"""

    print "Oh no, {}! You lost! The correct word is {}".format(player_name, random_word)


def prints_win(player_name):
    """Prints to player that they Won"""

    print "Congratulations {}! You won!".format(player_name)


def plays_game(random_word, player_name):
    """Runs the Game"""

    lives = 6
    letters_used = []
    current_word = list(len(random_word)*"_")

    while True:
        print "\nWord: "

        for char in current_word:
            print char

        print "\nAttempts left: {}, Letters used: {}".format(str(lives), str(letters_used))

        letter = raw_input("\nType a letter: ")

        if len(letter) > 1:
            if letter == random_word:
                prints_win(player_name)
            else:
                prints_loss(random_word, player_name)
            break

        letters_used.append(letter)

        found_letter = False
        for i, ch in enumerate(random_word):
            if ch == letter:
                found_letter = True
                current_word[i] = letter

        if not found_letter:
            lives -= 1
            print"\nThis letter is not in the word.\n"

        if lives == 0:
            prints_loss(random_word, player_name)
            break

        if "_" not in current_word:
            print "\nWord: "
            for char in current_word:
                print char
            prints_win(player_name)
            break


def ask_if_continue():
    """Ask user if they want to get another horoscope returns Boolean"""

    playing = raw_input("Do you want play again?(type exit to exit) ")

    if playing == 'exit' or playing[0] == 'n':
        return False

    return True


def start():

    prints_instructions()
    player_name = raw_input("What is your name? ")

    playing = True

    while playing:
        random_word = random_word_generator()
        plays_game(random_word, player_name)
        playing = ask_if_continue()

    print "thanks for playing!"

start()
