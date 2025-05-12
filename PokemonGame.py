import random
import time

## Intro scene Function to get User to input name less than 10 characters, and to choose if they are a boy or a girl
## in the While True lines, programs makesuser pick a town based off three choices. User must type either 1,2 or 3 and press enter to continue.
def intro():
    print("\nWelcome to the Pokémon World!")
    time.sleep(1.0)
    user_name = input("\nWhat's your name? (Cannot be more than 10 letters): ")
    while len(user_name) > 10:
        print("Sorry, the name cannot be more than 10 letters.")
        user_name = input("Please enter a valid name: ")

    time.sleep(1.0)
    gender = input("\nAre you a boy or a girl? (Type 'boy' or 'girl'): ")
    while gender.lower() not in ['boy', 'girl']:
        print("Invalid choice. Please enter 'boy' or 'girl'.")
        gender = input("Are you a boy or a girl? (Type 'boy' or 'girl'): ")

    time.sleep(1.5)
    print(f"\nHello, {user_name}! Welcome to the world of Pokémon!")

    # Ask the user which town they want to start in using Enuemrate
    town_choices = ['Kanto', 'Johto', 'Hoenn']

    while True:
        try:
            time.sleep(1.5)
            print("\nHere are the Pokemon World Town Choices:")
            for (i, town) in enumerate(town_choices, start=1):
                print(f"{i}. {town}")

            choice_number = int(input("\nPlease enter 1, 2 or 3 to choose a town: "))
            
            if choice_number in [1, 2, 3]:
                break
            else:
                print("\nInvalid choice. Please enter a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    town_choice = town_choices[choice_number - 1]
    time.sleep(1.5)
    print(f'\n\nPress Enter To Start Your Pokémon Aventure in {town_choice}')
    input()
    time.sleep(2.0)
    print("\n(You arrive at your new home)")
    time.sleep(1.5)
    print(f'\nMom: I love this new town {town_choice}! It is so beautiful!!')
    time.sleep(1.5)
    print(f'Mom: Awwww.... My little {gender} all grown up.')
    time.sleep(1.5)
    print('Mom: You are finally old enough become a Pokémon trainer.')
    time.sleep(1.5)
    print('Mom: What are you still doing standing there??')
    time.sleep(1.5)
    print('Mom: Go and see the Professor of this town to start your adventure!')
    time.sleep(1.5)
    print(f'Mom: Goodluck {user_name}. just make sure to call back home!! ')
    time.sleep(1.5)
    cut_scene()
    return user_name, gender, town_choice


## used to ask user to press enter to continue. Similar to pressing A to continue in a video game
def cut_scene():
    input("Press enter to continue...")

## contains information about the each Pokemon Starter. If the User picks the choice of starter, it will print the information accordingly
def pokedex_descriptions(starters):
    if starters == 'Bulbasaur':
        time.sleep(1.5)
        print("\nBulbasaur: The Grass Type Pokémon")
        time.sleep(1.5)
        print("A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.")
    
    if starters == 'Charmander':
        time.sleep(1.5)
        print("\nCharmander: The Fire Type Pokémon")
        time.sleep(1.5)
        print("The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is enjoying itself. If the Pokémon becomes enraged, the flame burns fiercely.")
    
    if starters == 'Squirtle':
        time.sleep(1.5)
        print("\nSquirtle: The Water Type Pokémon")
        time.sleep(1.5)
        print("Its shell is not just for protection. Its rounded shape and the grooves on its surface minimize resistance in water, enabling Squirtle to swim at high speeds.")
    
    if starters == 'Chikorita':
        time.sleep(1.5)
        print("\nChikorita: The Grass Type Pokémon")
        time.sleep(1.5)
        print("It loves to bask in the sunlight. It uses the leaf on its head to seek out warm places.")
    
    if starters == 'Cyndaquil':
        time.sleep(1.5)
        print("\nCyndaquil: The Fire Type Pokémon")
        time.sleep(1.5)
        print("It flares flames from its back to protect itself. The fire burns vigorously if the Pokémon is angry. When it is tired, it sputters with incomplete combustion.")
    
    if starters == 'Totodile':
        time.sleep(1.5)
        print("\nTotodile: The Water Type Pokémon")
        time.sleep(1.5)
        print("Despite its small body, Totodile's jaws are very powerful. While it may think it is just playfully nipping, its bite has enough strength to cause serious injury.")
    
    if starters == 'Treecko':
        time.sleep(1.5)
        print("\nTreecko: The Grass Type Pokémon")
        time.sleep(1.5)
        print("Treecko has small hooks on the bottom of its feet that enable it to scale vertical walls. This Pokémon attacks by slamming foes with its thick tail.")
    
    if starters == 'Torchic':
        time.sleep(1.5)
        print("\nTorchic: The Fire Type Pokémon")
        time.sleep(1.5)
        print("Torchic has a place inside its body where it keeps its flame. Give it a hug - it will be glowing with warmth. This Pokémon is covered all over by a fluffy coat of down.")
    
    if starters == 'Mudkip':
        time.sleep(1.5)
        print("\nMudkip: The Water Type Pokémon")
        time.sleep(1.5)
        print("In water, Mudkip breathes using the gills on its cheeks. If it is faced with a tight situation in battle, this Pokémon will unleash its amazing power - it can crush rocks bigger than itself.")
    print()
    cut_scene()


## Choosing a starter scene with a character named Professor Oak.
## using if elif else statements to give choices of starters based on which town they picked in Intro(). 
def choose_starter(town, user_name):
    time.sleep(1.5)
    print(f"\n\n(You arrive at the Pokémon Professor's Lab in {town} Town)")
    time.sleep(1.5)
    print("\nProfessor Oak: Welcome, young Trainer!")
    time.sleep(1.5)
    print("Professor Oak: What is your name??")
    cut_scene()
    time.sleep(1.5)
    print(f"\nProfessor Oak: {user_name}? What a nice name!")
    time.sleep(1.5)
    print(f"Professor Oak: Okay {user_name}.. Are you ready to be a Pokémon Trainer?")
    time.sleep(1.5)
    print("Professor Oak: First, I need to give you this. Here is a Pokedex.")
    time.sleep(1.5)
    print("\n(You put the Pokedex in your pocket)")
    time.sleep(1.5)
    print('\nProfessor Oak: The Pokedex is used to scan a Pokémon and take notes in there... catch them all and fill this Pokédex out.')
    time.sleep(1.5)
    print(f"\nProfessor Oak: Okay, good. Now, I need you to make a choice of which starter you're going to start off with in {town} Town.")
    cut_scene()
    while True:
        try:
            time.sleep(1.5)
            print(f"\nHere are the starter Pokémon available:")
            time.sleep(1.5)
            
            if town.lower() == 'kanto':
                starters = ('Bulbasaur', 'Charmander', 'Squirtle')
            elif town.lower() == 'johto':
                starters = ('Chikorita', 'Cyndaquil', 'Totodile')
            else:
                starters = ('Treecko', 'Torchic', 'Mudkip')

            for i, starter in enumerate(starters, start=1):
                print(f"{i}. {starter}")

            starter_choice = int(input("Choose your starter (enter the corresponding number): "))

            if starter_choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please choose a number between 1 and 3.")

            chosen_starter = starters[starter_choice - 1]
            time.sleep(1.5)
            print(f"\nYou chose {chosen_starter}!")
            print(f'\n(You start to scan your starter with your Pokédex)')
            cut_scene()
            pokedex_descriptions(chosen_starter)
            return chosen_starter
        except ValueError as e:
            print('Wrong input. Enter a different number')
## Loading Rival information such as their starter and the name. Returns values to make varibles. 
def rival_information():
    rival_name = 'Gary'
    rival_starter = 'Eveee'
    return rival_name,rival_starter

## First scene with rival dialoge. References Varibles names from Intro() and rival_information().
def first_scene_with_rival(chosen_starter, user_name):
    rival_name,rival_starter = rival_information()

    time.sleep(1.5)
    print('\n\n\n(A young boy walks into the professors Lab...)')
    time.sleep(1.5)
    print(f'\n{rival_name}: Hey Grandpa. Who is this???')
    time.sleep(1.5)
    print(f'Professor Oak: Hello grandson. This is {user_name}. He is a new trainer just like you')
    time.sleep(1.5)
    print(f'Professor Oak: He just chose {chosen_starter} as his first Pokemon.')
    time.sleep(1.5)
    print(f'{rival_name}: oh yeah? Lets see if your {chosen_starter} can beat my {rival_starter}. Lets battle..')
    time.sleep(1.5)
    cut_scene()

## Battle scene with ribal, using a While True: to be able to make a loop where the battle goes on until its proven true that the User won.     
def first_battle_with_rival(chosen_starter):
    rival_name, rival_starter = rival_information()

    while True:
        
        print(f'\n----{rival_name} started a Pokémon battle with you----')
        print(f'{rival_name} throws out {rival_starter}.')
        print(f'You throw out {chosen_starter}.')

        # Initial HP values
        rival_starter_hp = random.randint(10, 15)
        user_starter_hp = random.randint(15, 25)

        print(f'\nWhat will {chosen_starter} do?')

        while user_starter_hp > 0 and rival_starter_hp > 0:
            # Player's turn
            input("\nPress Enter to attack...")
            print('______________________________________________________________________________')
            player_attack = random.randint(5, 7)
            rival_starter_hp -= player_attack
            time.sleep(1.5)
            print(f"{chosen_starter} attacks! Gary's {rival_starter} loses {player_attack} HP.")

            if rival_starter_hp <= 0:
                print(f"\nCongratulations! You defeated Gary's {rival_starter}.")
                print('______________________________________________________________________________')

                user_won = True
                break

            # Rival's turn
            rival_attack = random.randint(2, 4)
            user_starter_hp -= rival_attack
            time.sleep(1.5)
            print(f"{rival_name}'s {rival_starter} attacks with Tackle. {chosen_starter} loses {rival_attack} HP.")

            if user_starter_hp <= 0:
                print(f"\nOh no! {chosen_starter} fainted. You lost the battle.")
                input('Press Enter to try again...')
                user_won = False
                break

        if user_won:
            break

# The end scene of the program, only can get here after the user wins battle from first_battle_with_rival().
def ending_scene(chosen_starter,user_name,town_choice):
    rival_name,rival_starter = rival_information()
    time.sleep(1.5)
    print(f'\n\n{rival_name}: Wow... I cant beleive {rival_starter} lost to your {chosen_starter}.')
    time.sleep(1.5)
    print(f'{rival_name}: This wont be the last time you see me {user_name}.')
    time.sleep(1.5)
    print(f'\n({rival_name} leaves the Pokémon Lab)')
    time.sleep(1.5)
    print(f'\nProfessor Oak: Congrats {user_name}!! You just your first battle. You did amazing!')
    time.sleep(1.5)
    print(f'Professor Oak: The time has now come to go explore {town_choice}')
    time.sleep(1.5)
    print('Professor Oak: Go become the very best. Like no one ever was')
    time.sleep(2.0)
    print(f"\n\nEnd of the adventure. Good luck on your journey, {user_name}!")
    time.sleep(2.0)
    cut_scene()

# Main program Execution
user_name, gender, town_choice = intro()
chosen_starter = choose_starter(town_choice,user_name)
first_scene_with_rival(chosen_starter, user_name)
first_battle_with_rival(chosen_starter)
ending_scene(chosen_starter,user_name,town_choice)
