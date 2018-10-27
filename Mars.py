

print("Get ready for blast off, you're going to Mars!")
print(5)
print(4)
print(3)
print(2)
print(1)
print("BLAST OFF!!")
print()

#Welcome
name =  input("Whats your name, explorer?")
name = name.title()

print()
print("Hi, " + name + " Welcome aboard!")
print("Yesterday you recieved a call from your good friend at NASA")
print("They need someone to go to Mars this weekend, and you've been chosen!")

#Mission excitement 
print()
print("Are you excited? Type Y or N.")
excited = input("> ")
excited = excited.upper()

if excited == "Y":
    print("W00t! Let the games begin!")
elif excited == "N":
    print("Welp, too bad buddy. You're goin' to Mars anyway!")

#Spaceship packing
print()
print("It's time to pack for your trip to Mars")

print("How many bags do you plan to bring?")
num_suitcases = input("> ")
num_suitcases = int(num_suitcases)

if num_suitcases > 2:
    print("WHAT! that'll never fit on our ship!")
    print("Try to consolidate down to two, mate.")

else:
    print("Load 'em up! Let's get moving!")

#Companion animal 
print()
print("You may bring one companion animal with you.")
print("What kind of companion animal would you like to bring?")
comp_animal = input("> ")
print("What is the name of your companion animal?")
name_comp_animal = input("> ")
name_comp_animal = name_comp_animal.title()

print("Cool, so you're bringing {name} the {animal}".format(name = name_comp_animal, animal = comp_animal))

#Spaceship Decor
print()
print("Nasa has a decor team with options to decorate your spaceship")
print("You have a couple options for the interior of your ship")
print()
print("Your options are:")
print()
print("A: TikiBar style")
print("B: 1970's brutualist")
print("C: San Francisco coffeehouse")
print()
decor_choice = input("Choose A,B, or C:")
print()

if decor_choice.upper() == "A":
    decor = "TikiBar style"
elif decor_choice.upper() == "B":
    decor = "1970's brutalist" 
elif decor_choice.upper() == "C":
    decor = "San Francisco coffeehouse"
else:
    print ("Not a valid choice. You get IKEA furniture!")
    decor = "IKEA furniture"

#Space narrative 
print()
print("I can see it now")
print(name , "the astronaut", "and his trusty", comp_animal , name_comp_animal)
print("surfing the celestial abyss in a" , decor , "spaceship")

import time
timer = 5
while timer > 0:
    print (timer, "...")
    time.sleep(2)
    timer -= 1

print ("***LIFTOFF BAYBAY***")