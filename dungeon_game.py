#version alpha 1.01
import logging

from sys import exit
from random import randint

hp = 3
skill = randint(1, 6) + 6
inventory = []
stones = []
#
def start_room():
    print("\nYou are running through an open, luscious green field filled with flowers of amazing colours of all varieties. You see in the distance a beautiful cottage, just like the one you lived in back in Thule before the raiders came.  It has the same thatched roof, small wooden fence and the garden you remember playing in too! Running closer you see crouched down in the corner of the garden what appears to be a woman in a perfectly white cotton dress, long golden hair and crisp white skin, tending to the earth.. she looks like.... it cannot be! she was killed years ago..\nYou run faster, getting closer, you are fixated on the familiar figure, not daring to look away. Suddenly she rises but oddly does not turn. You are only a few dozen meters from the gate when an uneasy feeling washes over you and your skin starts to crawl.\nYou find it harder and harder to move, your running becomes laboured and its like you are trying to run underwater, a few short moments later you are paralyzed and cant act. You feel a strange burning coming from your neck and look down to see a strange symbol on a chain you dont remember ever wearing.\nLooking back up, the figure has changed, her white dress is now charcol with huge burned holes littering the fabric, her hair starts to wilt before your eyes and patches begin to drop out leaving sore red and black marks in its place, she turns, the skin is partially burned from her face and holes reveal part of her jaw and teeth, you cant look away as her eyes come into view, well if there were any eyes there, all that exist are empty deep black sockets. What remains of your mother begins lurching towards you. Trying to move is impossible and all you can do as she gets closer is try to scream but even this proves futile.....\n\nYou jolt awake into blackness, your head spinning and breathing heavy, you thrust your arms out in front of you and are met with a hard wooden surface, preventing you from rising. Half in panic, you draw on your strength, crossig your arms to form a fleshy battering ram and force yourself upwards. A splintering sound rings out as light fills your eyes. \"It was just a dream\" You tell yourself and manage to calm yourself down, you take a moment to collect your thoughts.\nThinking back, you last remember hiking through the well trodden travellers path that runs from the town of Krule, up and through the mountain pass before sloping back around to the other side and eventually to the settlement of hiarko where you had been summoned to help them with a case of multiple missing villagers. Desperate for coin, you had taken up the offer from one of the villagers who had come to the town for help and being a competent sword for hire, thought it would be easy money. Now, you are here in what appears to be a wooden casket, surrounded by cold stone and earth.\n")

    print(f"You step out of the casket, some of your provisions have been taken however not all, but your purse has been emptied and your weapon is gone too, but you are still a skilled warrior, currently having a skill of {skill}. Wondering who took them, you consider your options. You can see two tunnels leading out of the room, one that stretches to the north and another that leads east. There are no major indications that make either option the better choice, but you are sure you can hear a faint but occastional rumbling sound from the left tunnel and the right tunnel has what seems to be a stone pathway. Do you head LEFT or RIGHT?\n")

    action = input("LEFT or RIGHT > ")

    if action.upper() == "LEFT":
        goblin_tunnel()
    elif action.upper() == "RIGHT":
        stone_room()
    else:
        print("There is no such direction, please press any key to pick again.")
        input("> ")
        start_room()
#
def goblin_tunnel():
    print("""As you walk down the tunnel the rumbling becomes louder and more clear, eventually it registers that the sound is something snoring! Whatever it is, its certainly not human. Do you CONTINUE forwards and see what lies ahead? Or head BACK down the tunnel and try the other path?\n""")

    action = input("CONTINUE OR BACK? > ")
    if action.upper() == "BACK":
        print("You backtrack down the tunnel.")
        stone_room()
    elif action.upper() == "CONTINUE":
        goblin_room()
    else:
        print("There is no such action, please press any key to pick again.")
        input("> ")
        goblin_tunnel()
#
def goblin_room():
    print("The tunnel opens out into a larger chamber no bigger than where you woke. To the far left side of the room a hideous GOBLIN in leather armours with a metal helm is sat on a small stool besides a decrepid wooden table. A few torches adorn the walls, giving the chamber a suprisingly cosy feel. The mystery of where your missing supplies now went is solved as you see what remains of the food, now mere crumbs on the table. You assume your gold is in the pouch attached to his belt and see your sword, leaning in the corner but you would have to risk disturbing the goblin to get to either item. There is only one exit ahead, another plain looking tunnel that appears to slope downwards however this one is lit by more torches.\nYou pause and quickly consider your options. Attempting to knockout the goblin is off the table because of his helmet and you have no other weapons to use for an effective pre-emptive strike, an ATTACK would still be possible though but risky.\nAnother option would be to attempt to STEAL your gold and weapon back without waking the goblin.\nAlternatively, you could just LEAVE the chamber by the tunnel.")

    action = input("ATTACK, STEAL or LEAVE ")

    if action.upper() == "ATTACK":
        print("""You launch into a vicious attack on the goblin, striking him clean in the only exposed area of his head, the chin. His helmet protects his head as it thuds into the wall and he struggles to comprehend whats happening as you dive on top of him. Its still a tough fight and you take some damage before emerging victorious.\n
        *********
        LOSE 1 HP
        *********\n """)
        loseHealth(1)
        print("Dusting yourself off, you reach for your sword. It feels good to have the blade back in your hands once more. Sheathing the blade, you turn to the bloodied body of the goblin and remove the purse from his belt. You count out your 5 GOLD pieces and 2 extra, there is also a STONE MARBLE shaped like an eye and a KEY. Just as you are about to leave the room you see something tucked into the goblins belt, its a small parchment. Opening it up you see a human skull crudely drawn into the middle with strange symbols all around it, you recognise none of them but get an uneasy feeling, their image seems to burn into the depths of your mind. With nothing else of use in the chamber, you attach the purse containing the gold and stone marble and then leave by the only exit.\n")
        inventory.append("GOLD")
        inventory.append("WEAPON")
        inventory.append("STONE MARBLE")
        inventory.append("KEY")
        statue_room()

    elif action.upper() == "STEAL":
        print("""You creep up silently on the sleeping goblin and attempt to untie the pouch from his belt. Your hands reach out and you start to loosen the leather strings... PRESS ENTER TO TEST YOUR SKILL!""")
        input()

        skillsteal = randint(1, 12)

        if skill > skillsteal:
            print("""You successfully steal the pouch from the belt of the goblin and then slowly reach towards the wall where your sword rests, you carefully grip the hilt before walking softly backwards and towards the exit with both items in hand. As you reach a few meters down the tunnel, you sheathe your SWORD and investigate the pouch. You count out your 5 GOLD pieces, plus 2 extra. There is also a STONE MARBLE shaped like an eye and a KEY. You place everything back into the pouch, attaching it to your own belt and then continue down the tunnel.\n""")
            inventory.append("GOLD")
            inventory.append("WEAPON")
            inventory.append("STONE MARBLE")
            inventory.append("KEY")
            statue_room()

        else:
            print("""You seem to have the pouch detatched from the goblin and gently pull, however you didnt fully clear it from the belt and as you pull the pouch falls open on one side, just enough for a gold coin to spill out and hit the floor. TING, TING TING TING.....\n
            The goblins eyes flash open in an instant and upon seeing you, he lashes out with his near hand. You are in a compromised position and suffer a deep wound to your neck. You stagger backwards hardly having time to compose yourself before the frenzied goblin attacks again.\n
            After a brutal battle, the goblin falls dead at your feet, but you are in no great condition yourself.\n
            *********
            LOSE 2 hp
            ********* """)
            loseHealth(2)
            print("Dusting yourself off, you reach for your sword. It feels good to have the blade back in your hands once more. Sheathing the blade, you turn to the bloodied body of the goblin with eyes for the pouch but cannot see it attached to his belt. You scan the room and you spot a glimmer of a gold coin underneath the table, your eyes follow its glare and you spot more with the missing pouch burst open and contents scattered across the floor. You scrabble around and eventually count out 5 GOLD pieces but nothing else. You are about to leave the room when your eyes catch something sparkle in the far corner of the room. At first you think its another gold piece but as you reach out for it, you find its a GLASS MARBLE. There is nothing too special about it and with nothing else of use in the chamber, you reattach the pouch to your own belt and leave by the only exit.")
            input("Press any key to continue..")
            inventory.append("GOLD")
            inventory.append("WEAPON")
            inventory.append("GLASS MARBLE")
            statue_room()

    elif action.upper() == "LEAVE":
        print("You creep silently past the goblin and through the tunnel opposite, forsaking your weapon and gold..\n")
        statue_room()

    else:
        print("Sorry, there is no such action. Press Enter to pick again")
        input("< ")
        goblin_room()
#       
def stone_room():
    print("You follow the stone pathway and soon arrive at a chamber much larger than the one you entered before, the entire floor is covered with large stone tiles and there are two archways at the far side of the room. As you are walking across, you notice one of the stones has been prized loose and is sat on top of the others. Closer inspection reveals an imprint in the exposed sand like something was once buried underneath the stone.\nDo you wish to SEARCH underneath other stones or leave through LEFT or RIGHT exit?\n")

    action = input("SEARCH, LEFT OR RIGHT? >")

    if action.upper() == "SEARCH":
        print("You decide on a brick at random to begin with and find that after a little digging around the sides, come away quite easily from the loose holding of the sand beneath. Your first attempt provides you nothing and neither does your third, fourth or even your fifth. You decide to only to lift a few more.\n")
        stone_room_choice()
    elif action.upper() == "LEFT":
        trap_room()
    elif action.upper() == "RIGHT":
        deadend_room()
    else:
        print("There is no such action, press any key to try again")
        stone_room()
#
def stone_room_choice():

    print("CHOOSE A STONE FROM 1 to 3 or type LEAVE to exit >")

    number = input()

    if number == "1" and "1" not in stones:
        print("You did not find anything. You can either try another STONE, or leave by the LEFT or RIGHT exits")

        choice = input("> ")
        stones.append("1")
        print(f"You cross off stone {stones}")

        if choice.upper() == "STONE":
            stone_room_choice()
        elif choice.upper() == "LEFT":
            trap_room()
        elif choice.upper() == "RIGHT":
            deadend_room()
        else:
            stone_room_choice()
    
    elif number == "1" and "1" in stones:
        print("You have already chosen this stone. Press any key to continue. ")
        input("> ")
        stone_room_choice()
        

    elif number == "2" and "2" not in stones:
        print("You life the stone and you are surprised to see small parchment underneath one and written in what looks like dried blood 'THE ROOM WITH THE FOUNTAIN CONTAINS A HIDDEN PIT, TRIGGERED BY A STONE TILE, DONT MAKE THE MISTAKE MY COMPANION DID...' You can evade this trap by typing \"TRAP\" when you are in a room with a fountain. You can now leave by one of the exits or lift another stone.\n")

        choice = input("STONE, LEFT or RIGHT >")
        stones.append("2")
        print(f"You cross off stone {stones}")

        if choice.upper() == "STONE":
            stone_room_choice()
        elif choice.upper() == "LEFT":
            trap_room()
        elif choice.upper() == "RIGHT":
            deadend_room()
        else:
            stone_room_choice()

    elif number == "2" and "2" in stones:
        print("You have already chosen this stone. Press any key to continue. ")
        input("> ")
        stone_room_choice()

    elif number == "3" and "3" not in stones:
        
        print("You lift another of the stones and spring a small trap that fires a small needle towards your face. TEST YOUR SKILL.\n\nPRESS ANY KEY\n")

        input(" >")
        stones.append("3")

        trapskill = randint(1, 12)

        if skill >= trapskill:
            print("You skillfully evade the needle, compose yourself and look beneath the stone. You find nothing, cursing your luck, you decide what to do next.\n")
            choice = input("Another STONE, LEFT or RIGHT exit > ")

            if choice.upper() == "STONE":
                stone_room_choice()
            elif choice.upper() == "LEFT":
                trap_room()
            elif choice.upper() == "RIGHT":
                deadend_room()
            else:
                stone_room_choice()    

        elif skill < trapskill:
            print("You are too slow to react to the needle and it buries itself in your shoulder, a few seconds later a shooting pain runs through your body.\n LOSE 1 HP\n")
            loseHealth(1)
            print("You take a few moments to recover, then decide what to do next.\n")
            choice = input("Another STONE, LEFT or RIGHT exit > ")

            if choice.upper() == "STONE":
                stone_room_choice()
            elif choice.upper() == "LEFT":
                trap_room()
            elif choice.upper() == "RIGHT":
                deadend_room()
            else:
                stone_room_choice()
        
        else:
            dead("Something went wrong")

    elif number == "3" and "3" in stones:
        print("You have already chosen this stone. Press any key to continue. ")
        input("> ")
        stone_room_choice()

    else:
        print("You are through with the stones and decide to choose an exit instead.")
        choice = input("LEFT or RIGHT> ")
        if choice.upper() == "LEFT":
            trap_room()
        elif choice.upper() == "RIGHT":
            deadend_room()
        else:
            print("There is no such choice, press any key to choose again.\n")
            input("> ")
            stone_room_choice()
#
def deadend_room():  
    print("You enter the archway and walk down the tunnel, the air becomes especially damp and cold down here. Eventually the stone tiles start to become less numerous and then stop completely, leaving a wet but firm sand underfoot.")
    print("Eventually the place opens up to form a fairly small room, old crates and straw packing have been dumped here, along with many other stones tiles. You about to go back the way you came when you spot an old sword leaning against the back wall, partially covered by a crate. As you are without a weapon you decide to pick it up.")
    inventory.append("WEAPON")
    print(f"You are now carrying, {inventory}.")
    print("With nothing else here, you head back down the tunnel and through the other exit. Press any key to continue...")
    input("> ")
    trap_room()
#
def trap_room():
    print("You enter the tunnel and find yourself in a long corridor which slopes gently upwards. As you continue to walk, you start to hear what sounds like water as eventually the corridor opens out into a much larger chamber. The room is covered in huge tiles, larger than the ones from the room you just came and to the far side is an amazing fountain, with multiple jets of water arching up from the mouths of varying creatures who are entwined together within the body of the structure. A huge basin surrounds the base to catch the water you think you see a faint glow eminating from within. There is a single exit at the far side of the room. Do you head over to the FOUNTAIN for a closer look or LEAVE the room.\n")

    choice = input("> ")
    
    if choice.upper() == "TRAP":
        print("Remembering the words on the scroll, you lower yourself down at eye level with the tiles to see if anything is suspect and sure enough, right infront of the fountain one of the stone tiles is raised more than the others. You decide to trigger the trap and hit the tile with the tip of your boot, quicky backing away as the tile flips down on a hinge. You move to the edge and take a look down, large spikes adorn the bottom and you see the companion who was not as lucky, her face contorted in pain as multiple spikes have punctured her body. Littered around her are the bones of other unfortunate souls but what really catches your eye is a key hanging from the womans open hand by a leather string. You carefully lower yourself down into the pit and take the key. After climbing back up and navigating around the pit, you investigate the fountain further and see the glow is coming from hundreds of small glass stones, shaped like eyes. You decide to take one with you and then leave by the only exit.\n")
        inventory.append("KEY")
        inventory.append("GLASS MARBLE")
        print(f"You are now carrying, {inventory}.")
        statue_room()

    elif choice.upper() == "FOUNTAIN":
        print("You step towards the fountain, completely unaware of the deadly trap that lies beneath one of the tiles. You hear a click as you step further forwards and the tile gives way beneath your feet and you fall into the pit... PRESS ANY KEY TO TEST YOUR LUCK...\n")

        input("> ")
        luck = randint(1, 12)

        if luck > 9:
            print("""Through sheer fortune you manage to miss most of the spikes that are fixed to the bottom of the pit as you land on another corpse that fell victim to the trap. Luckily you only suffer a few mild cuts to our arms and legs.\n
            *********
            LOSE 1 HP
            *********\n """)
            loseHealth(1)
            print("Carefully getting to your feet you search the body which appears to be that of a young woman, she has nothing aside from a small KEY which you pocket. You heave yourself out of the pit and take a look inside the fountain, and see the glow is coming from hundreds of small glass stones, shaped like eyes. You decide to take one with you and then leave by the only exit.\n")
            inventory.append("KEY")
            inventory.append("GLASS MARBLE")
            print(f"You are now carrying, {inventory}.")
            statue_room()

        else:
            print("You have no chance to react as you fall directly onto multiple spikes fixed to the bottom of the pit, your adventure ends here.")
            dead("Fell into the Spike Trap.")

    elif choice.upper() == "LEAVE":
        print("Something strikes you as not being quite right, and you play it safe, leaving the room by the only exit.")
        statue_room()
    
    else:
        print("There is no such action, press any key to choose again.")
        input("> ")
        trap_room()
#   
def statue_room():
    print("You walk for what seems an eternity, passing multiple sealed doorways along the walls on both sides. You even come across partially dug tunnels, indicating that this place is very much a work in progress, but what... or who is it for?\n Eventually the tunnel opens out into a much larger chamber, the roof extends up so high you almost cannot see the top. Looking across the room you see two huge exits, the right one is barred with an iron portcullis that fills the doorway, the left one is already open. Right in the middle of the two, an alcove is cut into the wall and resting inside is a statue of a lions head with a coloured glass eye in the left socket and a missing eye socket in the right eye. A beam of light shines down from somewhere above and rests on the face of the lion. An inscription below reads, \"Bright eyes light the way.\" There is nothing else of interest in the chamber.\n\n Do you leave through the LEFT exit, or if you have an ITEM you wish to use?")

    choice = input("> ")

    if choice.upper() == "LEFT":
        skeleton_room()

    elif choice.upper() == "ITEM":
        statue_item_room()

    else:
        print("There is no such action, LEFT or ITEM.")
        choice = input("> ")
        if choice.upper() == "LEFT":
            skeleton_room()
        elif choice.upper() == "ITEM":
            statue_item_room()
        else:
            statue_room()
#
def statue_item_room():
    print("Which item do you wish to use?")
    item = input("> ")
    if item.upper() == "STONE MARBLE" and item.upper() in inventory:
        print(f"You attempt to fit the {item} into the eye socket")
        input("< ")
        print("There is a slight rumble as the statues eye clicks into place, the portcullis slams shut over the left exit and another hidden one slams down from your entrance. You should have paid more attention to the riddle, the dull stone is clearly not bright! Now all exits are sealed and you will eventually starve to death in the chamber, unless something more horrible happens in the meantime....")
        dead("YOU STARVED")
    elif item.upper() == "GLASS MARBLE" and item.upper() in inventory:
        print(f"You attempt to fit the {item} into the eye socket")
        input("< ")
        print("There is a slight rumble as the statues eye clicks into place, the portcullis rises up as the eye shines bright. Without hesitation you step forward through the archway")
        door_room()
    else:
        print(f"You do not have {item}, pick AGAIN or type LEFT to leave by the open exit")
        choice = input("> ")
        if choice.upper() == "AGAIN":
            statue_item_room()
        elif choice.upper() == "LEFT":
            skeleton_room()
#
def skeleton_room():
    print("You enter a chamber littered with the bones of all types of assorted creatures. Across the room on your right side, is a sturdy looking door with another portcullis in front of it. Directly opposite there is a lever cut into a hollow. You dont seem to have too many options, you can go and pull the LEVER in the alcove to the left, or you could search the piles of BONES?")
    choice = input("> ")
    
    if choice.upper() == "LEVER":
        print("You have a feeling this is too easy, as you pull the lever and the portcullis starts to slowly rise. You walk across the chamber towards the exit and as you do, begint to hear a shuffling noise coming from some of the bones, you step back in horror to see the bones forming together until the skeleton of what looks to be a dwarf has appeared in front of the doorway, he clutches a rusty axe and steps shakily towards you.\n Are you carrying a WEAPON?")
        
        weapon = input("> ")
        if weapon.upper() == "YES" and "WEAPON" in inventory:
            fight_skeleton_dwarf("Dwarf", "3")
        else:
            dead("You have no weapon to defend yourself, you fight on valiantly using old bones you grab on the floor, but they are all too brittle to be much use and you eventually fall..")

    elif choice.upper() == "BONES":
        print("You start to search through the piles of bones, there are some bones you recognise as belonging to humans, dwarfs and elves, but there are also unnervingly, many you dont. You are about to give up when you discover an old axe beneath a goblins ribcage. You decide to take this if you are without a weapon.")

        inventory.append("WEAPON")

        print("You find nothing else of use in the chamber and have no choice but to pull the lever.")
        print("You have a feeling this is too easy as you pull, seeing the portcullis starts to slowly rise. You walk across the chamber towards the exit and as you do, begint to hear a shuffling noise coming from some of the bones, you step back in horror to see the bones forming together until the skeleton of what looks to be a dwarf has appeared in front of the doorway, he clutches a rusty axe and steps shakily towards you.\n Are you carrying a WEAPON?")
        
        weapon = input("> ")
        if weapon.upper() == "YES" and "WEAPON" in inventory:
            fight_skeleton_dwarf("Dwarf", "3")
        else:
            dead("You have no weapon to defend yourself, you fight on valiantly using old bones you grab on the floor, but they are all too brittle to be much use and you eventually fall..")

    else:
        print("There is no such action, press any key to try again.")
        input()
        skeleton_room()
#
def fight_skeleton_dwarf(enemy, enemy_hp):
    print("\nYou raise you weapon and step forward to attack, the SKELETON DWARF has a SKILL of 6 and 3 HEALTH\n")

    enemy_hp = int(enemy_hp)
    enemy_skill = 7
    
    while enemy_hp > 0:
        input("PRESS ENTER TO ATTACK")
        attackroll = randint(1, 12)
        total_skill = attackroll + skill

        enemy_attackroll = randint(1, 12)
        total_enemy_skill = enemy_attackroll + enemy_skill

        if total_skill > total_enemy_skill:
            print("You land a successful hit!\n")
            enemy_hp = enemy_hp - 1

        elif total_skill < total_enemy_skill:
            print("The enemy lands a hit!\n")
            loseHealth(1)

        elif hp == 0:
            dead("Died in combat")

        else:
            print("Something went wrong...")
        
    print("You successfully defeat the Skeleton and step through the doorway into the next room...")
    door_room()


    print("placeholder")

def door_room():
    print("The doorway leads into another long corridor which slopes down and up repeatidly, you pass partially excavated tunnels and rooms cutting into the walls on either side before eventually the tunnel opens out into another huge chamber, various materials are strewn about the place and things seem to be in a process of construction. One thing however that seems finished is the finely carved oak door that faces you. Incredible designs and images, albeit disturbing ones that seemily depict some sort of supreme leader controlling many different creatues, cover the door and it could easy pass as a work of art. There is a gold plated keyhole above the large handle and you test the door, sure enough its locked. To the left and right of the door are two other doorways that are the same size, but missing the actual doors. The right one has various tools and materials around it and is only partially dug out, the left one leads into darkness. You only have two options, use a KEY if you have one to get through the door, or leave by the LEFT exit.\n")
    
    choice = input("> ")

    if choice.upper() == "LEFT":
        print("You step forward into the darkness of the tunnel, you feel like this is the wrong decison but what choice do you have? Press any key to continue...")
        input()
        barbarian_room()

    elif choice.upper() == "KEY" and choice.upper() in inventory:
        print("You try the key in the door, you hear the lock turning and it unlocks with a satisfying 'thuck'. The door swings open and another tunnel appears before you. You step forward into the unknown. Press any key to continue....")
        input()
        riddle_room()
    
    elif choice.upper() == "KEY" and choice.upper() not in inventory:
        print("You do not have a key to open the door, you have no choice but to take the left passageway. Press any key to continue....")
        input()
        barbarian_room()

    else:
        print("There is no such action, press any key to try again...")
        input()
        door_room()

def barbarian_room():
    print("The tunnel slopes downwards, the air becoming cold and unwelcoming. The squeaking of rats can be heard in the darkness beneath your feet as you kick through verious debris strewn about your path. Eventually you come to a rusty iron gate, with a lock on the inside. It is far too dark to see much futher inside, but you can make out a curved wall that opens out into a circular room with bones and assorted weaponry, littered across the sandy floor. Sliding the bolt across, it swings inwards and you step forward into the chamber. As the room opens out infront of you, the gut feeling you had that this is some kind of arena is proven true. SLAM. The gate is locked shut behind you by a hideous goblin and before you can even react, wooden boards are opened up from the ceiling above, illuminating the chamber completely.\nA tall and imposing figure appears above, though you cannot make out his features because of the shadow cast over him. Saying nothing, the figure raises a staff and mumbles a few words. A noise is suddenly heard from the wall opposite and then a gate like the one you entered can be heard opening. Into the light steps GROM! Your friend... you can barely recognise him.fight_mindcontrolled_barbarian")

    #adjust main story to include grom
    #add death as the warlocks new champion if you win.

    fight_mindcontrolled_barbarian("GROM", "6")

def fight_mindcontrolled_barbarian(enemy, enemy_hp):
    print(f"\nYou raise you weapon and anticipate a very tought fight.{enemy} has a SKILL of 18 and 8 HEALTH\n")

    enemy_hp = int(enemy_hp)
    enemy_skill = 10
    
    while enemy_hp > 0:
        input("PRESS ENTER TO ATTACK")
        attackroll = randint(1, 12)
        total_skill = attackroll + skill

        enemy_attackroll = randint(1, 12)
        total_enemy_skill = enemy_attackroll + enemy_skill

        if total_skill > total_enemy_skill:
            print("You land a successful hit!\n")
            enemy_hp = enemy_hp - 1

        elif total_skill < total_enemy_skill:
            print(f"{enemy} lands a hit!\n")
            loseHealth(1)

        elif hp == 0:
            dead("You died in combat")

        else:
            print("Something went wrong...")
        
    print(f"You successfully defeat the {enemy}")
    placehold_room()

def placehold_room():
    print("Placeholder")

def riddle_room():
    print("Placeholder")

def end_room():
    print("Placeholder")
#
def loseHealth(damage):
    global hp
    hp = hp - damage
    print(f"YOU HAVE {hp} HEALTH REMAINING\n")

    if hp <= 0:
        dead("You have lost too much health and die from your wounds")
#    
def gainHealth(life):
    global hp
    hp = hp + life
    print(f"YOU NOW HAVE {hp} HEALTH")
#
def dead(why):
    print(why, "\n\n********\nGAME OVER\n********")
    exit(0)

start_room()