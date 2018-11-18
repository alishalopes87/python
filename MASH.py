import random

print("Let's play MASH! The game that reveals your future!")
print()
category_len = 4
partners = []
children = []
careers = []

wildcard_partners = ["Pee-Wee Herman", "Barbara Streinsan", "Homer Simpson", "Barrack Obama"]
wildcard_careers = ["Figure skater", "Tarot card reader", "Gypsy", "Unemployed"]
MASH = ["Mansion 👑", "🛏 Apartment", "🏚 Shack", "House 🏡"]

def wild_card(wild_lst):
    wild = random.choice(wild_lst)
    wild_lst.remove(wild)

    return wild


def play_mash():
    """Main game loop"""

    add_partners()
    add_career()
    add_children()
    reveal_future()


def ask_question(str):
    """Returns users answer""" 
    return input(str)


def add_partners():
    """Add's partners to list"""
    print()
    print("First let's choose your life partner! Enter four names to reveal who you will spend your life with")
    print()
    while len(partners) < category_len:
        partner = ask_question("Do you wanna pick a partner? Or go for a wild card?")
        if partner == "wild card":
            partner = wild_card(wildcard_partners)
            add_partner = partner.title()
    
        if partner not in partners:
            print("Great add {} more!".format(category_len - len(partners)-1))
            add_partner = partner.title()
            add_partner = partners.append(partner)
        else:
            print("You've already said that, no cheating!")
    
    return partners


def add_career():
    """Adds careers to list"""
    print()
    print("Next let's pick a profession! How will you spend your working years?")
    print()
    while len(careers) < category_len:
        career = ask_question("Would you like to choose a career? Or do you wanna pick a wild card?")
        if career == "wild card":
            career = wild_card(wildcard_careers)
            add_career = career.title()
            
        if career not in careers:
            print("Great add {} more!".format(category_len - len(careers)-1))
            add_career = career.title()
            careers.append(add_career)
        else:
             print("You've already said that, no cheating!")
    return careers
    

def add_children():
    """Adds number of children to list"""
    print()
    print("Will you have children? Enter how many you wish to have!")
    print()
    """Adds users choice of how many children they will have"""
    while len(children) < 4:
        child = ask_question("How many children will you have?")
        if child.isdigit():
            children.append(child)
            
        else:
            print("Enter a number")
    return children

def reveal_future():
    """Printers out result future"""
    print()
    rando = random.randint(0,3)
    child = children[rando]
    career = careers[rando]
    partner = partners[rando]
    home = MASH[rando]
    
    print("You will become a(n) {}, marry {}, have {} children, and live in a {}!".format(career, partner, child, home))
   
    again = ask_question("Do you want to play again?")
    again = again.lower()
    if again == "yes":
        partners.clear()
        careers.clear()
        children.clear()
        play_mash()
    
    else:
        print("Ok thanks for playing!")

play_mash()

