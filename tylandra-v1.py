# Text Based Adventure Game
import time
import random

class Sentinel:
    def __init__(self):
        self.name = "Sentinel"
        self.hp = 30
        self.atk = 5


class Fighter:
    def __init__(self):
        self.name = "Fighter"
        self.hp = 25
        self.atk = 8


class Rogue:
    def __init__(self):
        self.name = "Rogue"
        self.hp = 20
        self.atk = 10


player_class = None
valid_classes = {
    "sentinel": Sentinel,
    "fighter": Fighter,
    "rogue": Rogue
}


class Panther:
    def __init__(self):
        self.name = "Panther"
        self.hp = 8
        self.atk = 8


class SkeletonBull:
    def __init__(self):
        self.name = "Skeleton Bull"
        self.hp = 20
        self.atk = 10

class Necromancer:
    def __init__(self):
        self.name = "Necromancer"
        self.hp = 10
        self.atk = 5
        self.spell = 20
necro = Necromancer()

if __name__ == "__main__":
    while player_class is None:
        print("Welcome Adventurer!")
        time.sleep(1)
        selected_class = input("Choose a class: Sentinel, Fighter, Rogue\n").lower()
        if selected_class in valid_classes:
            player_class = valid_classes[selected_class]()
            break
        else:
            print("Invalid Class. Choose again.")
            time.sleep(1)


    def sentinel_intro():
        print(f"You have chosen {player_class.name}.")
        print("STATS")
        print(f"HP= {player_class.hp}")
        print(f"ATK= {player_class.atk}")


    def fighter_intro():
        print(f"You have chosen {player_class.name}.")
        print("STATS")
        print(f"HP= {player_class.hp}")
        print(f"ATK= {player_class.atk}")


    def rogue_intro():
        print(f"You have chosen {player_class.name}.")
        print("STATS")
        print(f"HP= {player_class.hp}")
        print(f"ATK= {player_class.atk}")


    if isinstance(player_class, Sentinel):
        sentinel_intro()
    elif isinstance(player_class, Fighter):
        fighter_intro()
    elif isinstance(player_class, Rogue):
        rogue_intro()
    else:
        print("Error: Exiting Program")
        quit()

    time.sleep(1)
    print(f"\n\nGood luck {player_class.name}!\n\n")
    time.sleep(2)

    def tylandra_gate():
        print("You approach the gates of Tylandra and are stopped by a guard holding up his hand, palm facing you.")
        time.sleep(2)
        print("'Oi, what business ye got in the city!?'")
        time.sleep(2)
        dialogue = input("1)Ask about the Necromancer\n2)'My business is my own!'\n")
        if dialogue == "1":
            print("'Here te slay the mad wizard are ye? Good.'")
            time.sleep(2)
            print("'He has a castle in the woods to the east, follow me.'")
            time.sleep(2)
            print("The guard leads you down a path around the outside of the city walls.")
            time.sleep(2)
            print("The path eventually diverges from the wall leading to the edge of a forest.")
            time.sleep(2)
            print("'Well here ye are, I'm not one fer goin into the Wizard's wood.")
            time.sleep(2)
            print("'Besta luck to ye Adventurer!")
            time.sleep(2)
            print("The guard turns and begins walking back the way you came.")
            time.sleep(2)
            print("You peer into the ominously quiet forest for a moment before pushing onward.")
            time.sleep(2)
            keep_scene()
        elif dialogue == "2":
            print("The guard looks at you incredulously and places two hands on his poleaxe.")
            time.sleep(2)
            print("'Git your damned arse outta here! This be a city o' order and peace!")
            time.sleep(2)
            print("Looks like you won't find any help here.")
            time.sleep(2)
            forest_scene()
        else:
            print("Invalid choice. Try again.")
            tylandra_gate()

    def forest_scene():
        print("You carefully inspect the terrain around the city...")
        time.sleep(2)
        print("You spot some unnatural stones peeking out of the canopy of a nearby forest.")
        time.sleep(2)
        print("You make your way toward the forest's edge.")
        time.sleep(2)
        print("As the approach the treeline you hear a mighty feline roar!")
        time.sleep(2)
        print("A panther leaps down on you from the trees above! What do you do?")
        time.sleep(2)
        panther = Panther()
        while panther.hp > 0 :
            action = input("1)Attack\n2)Flee\n")
            if action == "1":
                print("You attempt to spin away with your sword coming around to cut the great cat!")
                time.sleep(2)
                print("You are raked by the panther's claw!")
                time.sleep(2)
                panther.hp -= player_class.atk
                player_class.hp -= panther.atk
                print(f"You deal {player_class.atk} damage, Your HP is now {player_class.hp}")
                time.sleep(2)   
                if player_class.hp <= 0:
                    player_death()
                if panther.hp <= 0:
                    print("The great cat falls to the ground with a heavy thud.")
                    time.sleep(2)
                    break
            elif action == "2":
                print("You turn and sprint toward the city walls")
                time.sleep(2)   
                print("You hear a high-pitched growl.")
                time.sleep(2)   
                print("The panther's claws dig into your back.")
                time.sleep(2)   
                print("Then you feel the great cat clamp its jaws onto the back of your neck.")
                time.sleep(2)   
                print("You fall to the ground as the cat rips flesh from the back of your neck and rakes your back with its claws.")
                time.sleep(2)   
                player_class.hp -= (panther.atk * 3)
                print(f"Your HP is now {player_class.hp}. Foolish to think you could outrun a panther.")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()   
                print("Suddenly the cat leaps off of you and flees.")
                time.sleep(2)   
                print("You hear the voice of a man roaring, 'Git ya damned cat! Git!'")
                time.sleep(2)   
                print("As you climb to your feet you see a guardsman sporting the sigil of the city of Thylandra.")
                time.sleep(2)
                print("'Damned cats grab any folk gettin too close teh the wood.")   
                time.sleep(2)   
                print("'What business ye got in the city?'")
                time.sleep(2)
                dialogue = input("1)Ask about the Necromancer\n2)'My business is my own!'\n")
                if dialogue == "1":
                    print("'Here te slay the mad wizard are ye? Good.'")
                    time.sleep(2)
                    print("'He has a castle in the woods, follow me.'")
                    time.sleep(2)
                    print("The guard leads you to the treeline where you were just ambushed.")
                    time.sleep(2)
                    print("'Well here ye are, I'm not one fer goin into the Wizard's wood.")
                    time.sleep(2)
                    print("'Besta luck to ye Adventurer!")
                    time.sleep(2)
                    print("The guard turns and begins walking back the way he came.")
                    time.sleep(2)
                    print("You peer into the ominously quiet forest for a moment before pushing onward.")
                    time.sleep(2)
                    keep_scene()
                elif dialogue == "2":
                    print("The guard looks at you incredulously.")
                    time.sleep(2)
                    print("'Let the cats have yer damned arse then!")
                    time.sleep(2)
                    print("Looks like you won't find any help here.")
                    time.sleep(2)
                    print("You head back toward the treeline, cautiously looking to the tree tops for any threat...")
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice. Try again.")
                    time.sleep(2)
        print("You continue into the forest, walking for quite some time...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        keep_scene()
    
    def keep_scene():
        print("You spot a small stone keep in the distance. How do you approach?")
        time.sleep(2)
        choice = input("1)Walk up to the gate\n2)Do some recon\n")
        if choice == "1":
            keep_front()
        elif choice == "2":
            keep_rear()
        else:
            print("Invalid choice. Try again.")
            time.sleep(2)

    def keep_front():            
        bull = SkeletonBull()
        #The bull cannot be defeated by the player
        while bull.hp > 0:
            print("You approach the front gate sword in hand. A necromancer is rumored to lair here after all.")
            time.sleep(2)
            print("As you get closer you see the large iron gate is smashed inward.")
            time.sleep(2)
            print("You walk through the smashed gate into a small courtyard.")
            time.sleep(2)
            print("You look around the courtyard...")
            time.sleep(2)
            print("The wooden doors of the keep entrance are broken to pieces.")
            time.sleep(2)
            print("Skeletons lay all about and the walls are beginning to crumble.")
            time.sleep(2)
            print("You hear a soft thumping as you near the entrance of the keep...")
            time.sleep(2)
            print("Pounding...")
            time.sleep(2)
            print("Pounding hooves! You begin to see the form of a giant skeletal bull charging toward you!")
            time.sleep(2)
            action = input("1)Try to roll through the charge\n2)Dive out of the bull's path\n")
            if action == "1":
                print("You dive into a somersault, headed straight for the monster.")
                time.sleep(2)
                print("As you finish your roll you hear the receding sound of hoofbeats")
                time.sleep(2)
                print("Now what?")
                action2 = input("1)Run deeper into the keep\n2)Turn and fight!\n")
                if action2 == "1":
                    print("An unlit foyer before you, you sprint into the dark depths of the keep.")
                    time.sleep(2)
                    keep_interior()
                elif action2 == "2":
                    print("The monster stands between you and the iron gate you entered through.")
                    time.sleep(2)
                    print("You run at the beast, sword raised.")
                    time.sleep(2)
                    print("The skeletal bull starts to run at you.")
                    time.sleep(2)
                    print("You bring your sword down and side step attempting to dodge the monster's horns")
                    time.sleep(2)
                    print("You feel your sword connect, then it sticks in place...")
                    bull.hp -= player_class.atk
                    print(f"You deal {player_class.atk} to the monster.")
                    time.sleep(2)
                    print("The sword is wrenched from your grasp as the bull rears up.")
                    time.sleep(2)
                    print("Before you can react the bull brings its mights hooves down upon you.")
                    player_class.hp -= (bull.atk * 2)
                    print(f"Your HP is now {player_class.hp}")
                    time.sleep(2)
                    if player_class.hp <= 0:
                        player_death()
                    print("You manage to crawl out of the storm of hooves, and scramble to your feet.")
                    time.sleep(2)
                    print("You stand up and see the bull turning to face you.")
                    action3 = input("1)Attack\n2)Flee\n")
                    if action3 == "1":
                        print("You charge the monster and strike it before it can fully turn and face you!")
                        time.sleep(2)
                        bull.hp -= player_class.atk
                        print(f"You deal {player_class.atk} damage!")
                        time.sleep(2)
                        print("You feel the heavy thud of a hoof in your side.")
                        time.sleep(2)
                        player_class.hp -= bull.atk
                        print(f"Your HP is now {player_class.hp}")
                        time.sleep(2)
                        if player_class.hp <= 0:
                            player_death()
                    elif action3 == "2":
                        print("You run to the keep for cover before the beast can turn to face you fully.")
                        time.sleep(2)
                        print("You can hear the sound of pursuing hooves as you run the the keep entrance.")
                        time.sleep(2)
                        print("As you run into the darkness of the keep, the hoofbeats stop...")
                        time.sleep(2)
                        keep_interior()
                    else:
                        print("Invalid response. Try again.")
                        time.sleep(1)
            elif action == "2":
                print("You turn and leap off the steps up to the keep and land in the courtyard.")
                time.sleep(2)
                print("As you turn around you see the bull finishing its charge and turning to face you.")
                time.sleep(2)
                print("The monster stands between you and the iron gate you entered through.")
                time.sleep(2)
                action2 = input("1)Charge the monster\n2)Retreat to the keep\n")
                if action2 == "1":
                    print("You run at the beast, sword raised.")
                    time.sleep(2)
                    print("The skeletal bull starts to run at you.")
                    time.sleep(2)
                    print("You bring your sword down and side step attempting to dodge the monster's horns")
                    time.sleep(2)
                    print("You feel your sword connect, then it sticks in place...")
                    time.sleep(2)
                    bull.hp -= player_class.atk
                    print(f"You deal {player_class.atk} to the monster.")
                    time.sleep(2)
                    print("The sword is wrenched from your grasp as the bull rears up.")
                    time.sleep(2)
                    print("Before you can react the bull brings its mights hooves down upon you.")
                    time.sleep(2)
                    player_class.hp -= (bull.atk * 2)
                    if player_class.hp <= 0:
                            player_death()
                    print(f"Your HP is now {player_class.hp}")
                    time.sleep(2)
                    print("You manage to crawl out of the storm of hooves, and out the iron gate.")
                    time.sleep(2)
                    print("You stand on the other side and look face to face with the skeletal bull.")
                    time.sleep(2)
                    action3 = input("1)Attack\n2)Flee\n")
                    if action3 == "1":
                        print("You charge the monster and strike it before it can fully turn and face you!")
                        time.sleep(2)
                        bull.hp -= player_class.atk
                        print(f"You deal {player_class.atk} damage!")
                        time.sleep(2)
                        print("You feel the heavy thud of a hoof in your side.")
                        time.sleep(2)
                        player_class.hp -= bull.atk
                        print(f"Your HP is now {player_class.hp}")
                        time.sleep(2)
                        if player_class.hp <= 0:
                            player_death()
                    elif action3 == "2":
                        print("You run to the keep for cover before the beast can turn to face you fully.")
                        time.sleep(2)
                        print("You can hear the sound of pursuing hooves as you run the the keep entrance.")
                        time.sleep(2)
                        print("As you run into the darkness of the keep, the hoofbeats stop...")
                        time.sleep(2)
                        keep_interior()
                    else:
                        print("Invalid response. Try again.")
                        time.sleep(1)
                elif action2 == "2":
                    print("You run to the keep for cover.")
                    time.sleep(2)
                    print("You can hear the sound of pursuing hooves as you run the the keep entrance.")
                    time.sleep(2)
                    print("As you run into the darkness of the keep, the hoofbeats stop...")
                    time.sleep(2)
                    keep_interior()
                else:
                    print("Invalid response. Try again.")
                    time.sleep(1)
            else:
                print("Invalid response. Try again.")
                time.sleep(1)

    def keep_rear():
        print("You cautiously patrol the area around the keep looking for any weakness in its defense.")
        time.sleep(2)
        print("From the rear you can see there is a large hole into the interior of the keep.")
        time.sleep(2)
        while True:
            choice = input("Enter through the front or the rear?(F/R)")
            if choice.upper() == "R":
                print("You approach the large hole in the back wall of the keep.")
                time.sleep(2)
                print("As you reach the hole you notice that ominous darkness shrouds the interior")
                time.sleep(2)
                print("You walk into the darkness of the keep.")
                time.sleep(2)
                keep_interior()
            elif choice.upper() == "F":
                keep_front()
            else:
                print("Invalid response. Try again.")
                time.sleep(1)

    def keep_interior():
        print("As you walk into the darkness, it turns from normal shadows to an ominous abscense of light.")
        time.sleep(2)
        print("You feel your way around the keep, navigating corridor after corridor...")
        time.sleep(2)
        print("Finally you stumble onto a spiral staircase.")
        time.sleep(2)
        print("Still unable to see, you crawl up the steps.")
        time.sleep(2)
        print("As you reach the top of the staircase the darkness ends abruptly.")
        time.sleep(2)
        print("Your eyes nearly clamp shut as they adjust to the brightly lit room before you.")
        time.sleep(2)
        print("You find yourself in what looks to have been some sort of chapel or monastary.")
        time.sleep(2)
        print("The large room is cleared of any furniture, save for a few desks containing morbid and macabre baubles.")
        time.sleep(2)
        print("A large tapestry depicting a skeletal demon slaying an angel hangs behind an altar.")
        time.sleep(2)
        print("Before the altar, dried blood is smeared on the ground in the shape of a pentagram.")
        time.sleep(2)
        print("You yank your sword from its sheath as you hear a mad cackle fill the atrium.")
        time.sleep(2)
        print("YOU ARE A FOOL TO HAVE COME HERE! BAHAHAHA!")
        time.sleep(2)
        print("You cannot pinpoint where the voice is coming from and you do not see anyone.")
        time.sleep(2)
        choice = input("1)Search for the Necromancer\n2)Brace yourself and wait\n")
        if choice == "1":
            print("You slowly walk a circle around the atrium, checking behind and under each desk.")
            time.sleep(2)
            print("As you approach the altar the tapestry flies toward you!")
            time.sleep(2)
            print("You see the tapestry float harmlessly to the ground as a bolt of light smashes into your torso.")
            time.sleep(2)
            print("A sudden overwhelming cold takes you to your knees.")
            time.sleep(2)
            player_class.hp -= necro.spell
            print(f"Your HP is now {player_class.hp}")
            time.sleep(2)
            if player_class.hp <= 0:
                player_death()
            print("'BAHAHAHAHA!'")
            time.sleep(2)
            print("You see a frail, wrinkled man lunging at you with a dagger as the light disappates!")
            time.sleep(2)
            action = input("1)Attack\n2)Dodge\n")
            if action == "1":
                print("You swing your sword at the old man's face.")
                time.sleep(2)
                print("He ducks with surprising speed and plunges his blade into your side!")
                time.sleep(2)
                player_class.hp -= necro.atk
                print(f"Your HP is now {player_class.hp}")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()
                boss_battle()
            elif action == "2":
                print("You bring your sword down and out, deflecting the old man's blade.")
                time.sleep(2)
                print("Too far into his lunge now, the old man stumbles to the floor.")
                time.sleep(2)
                boss_battle()
            else:
                print("Invalid Response. Try again.")
                time.sleep(1)
        elif choice == "2":
            print("You scan the room carefully, sword at the ready.")
            time.sleep(2)
            print("You leap to the side as you see a flash of blue-white light flying out from behind the tapestry!")
            time.sleep(2)
            print("As you come to your feet you see a frail, wrinkled man lunging at you with a dagger!")
            time.sleep(2)
            action = input("1)Attack\n2)Dodge\n")
            if action == "1":
                print("You swing your sword at the old man's face.")
                time.sleep(2)
                print("He ducks with surprising speed and plunges his blade into your side!")
                time.sleep(2)
                player_class.hp -= necro.atk
                print(f"Your HP is now {player_class.hp}")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()
            elif action == "2":
                print("You bring your sword down and out, deflecting the old man's blade.")
                time.sleep(2)
                print("Too far into his lunge now, the old man stumbles to the floor.")
                time.sleep(2)
                boss_battle()
            else:
                print("Invalid Response. Try again.")
                time.sleep(1)
        else:
            print("Invalid Response. Try again.")
            time.sleep(1)

    def boss_battle():
        while necro.hp > 0:
            necro_roll = random.randint(0,1)
            if necro_roll == 0:
                necro_action = necro.atk
            elif necro_roll == 1:
                necro_action = necro.spell
            else:
                print("Error: Exiting Program")
                quit()
            print("The Necromancer is before you...")
            time.sleep(2)
            action = input("1)Attack\n2)Dodge\n")
            if action == "1" and necro_roll == 0:
                print("The Necromancer stabs at you while you bring your sword down on him!")
                time.sleep(2)
                player_class.hp -= necro_action
                necro.hp -= player_class.atk
                print(f"You deal {player_class.atk} damage. Your HP is now {player_class.hp}")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()
            elif action == "2" and necro_roll == 0:
                print("You step to the side and shove the old man as he come in to stab you.")
                time.sleep(2)
                player_class.hp -= necro_action
                necro.hp -= player_class.atk
                print(f"You deal {player_class.atk} damage. Your HP is now {player_class.hp}")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()
            elif action =="1" and necro_roll == 1:
                print("The Necromancer begins moving his arms and waggling his fingers...")
                time.sleep(2)
                print("You jump at him, stabbing him with your sword before he can finish his incantation!")
                time.sleep(2)
                necro.hp -= player_class.atk
                print(f"You deal {player_class.atk} damage.")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()
            elif action == "2" and necro_roll == 1:
                print("You prepare yourself for the old man's next attack...")
                time.sleep(2)
                print("Before you notice him casting, the necromancer sends a spell at you!")
                time.sleep(2)
                print("A bolt of light crushes your chest and knocks you backward.")
                time.sleep(2)
                player_class.hp -= necro_action
                print(f"Your HP is now {player_class.hp}")
                time.sleep(2)
                if player_class.hp <= 0:
                    player_death()
            else:
                print("Invalid Response. Try again.")
                time.sleep(1)
        print("The old man collapses to the ground.")
        time.sleep(2)
        print("Blood starts to pool around the corpse of the pathetic looking old man.")
        time.sleep(2)
        print("With another evil snuffed out, you return to a nearby outpost of the Order of the Flaming Fist.")
        time.sleep(2)
        print("Congratulations! You have beaten my game! Thanks for playing and stay tuned for additions and updates!")
        time.sleep(2)
        quit()

    def player_death():
        print("Your vision goes black as you feel the cold embrace of death.")
        time.sleep(1)
        print("GAME OVER")
        time.sleep(1)
        quit()
  
    while True:
        print("You are tasked by the Order of the Flaming Fist to stop a necromancer's plot near the city of Tylandra")
        time.sleep(2)
        print("You can see the gates of Tylandra in the distance, but how will you find the necromancer's tower?")
        time.sleep(2)
        setting = input("1)Ask around the city\n2)Explore the nearby area\n")
        if setting == "1":
            tylandra_gate()
        elif setting == "2":
            forest_scene()
        else:
            print("Invalid Response. Try again.")
            time.sleep(1)

