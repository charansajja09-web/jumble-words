import random

def choose():
     dictionary = [
    # 4 Letters
    "blue", "cake", "desk", "frog", "glow", "jump", "lion", "nest", "pink", "quiz",
    "rain", "star", "tree", "wind", "zero",
    
    # 5 Letters
    "apple", "beach", "clock", "dance", "earth", "flute", "grape", "house", "juice", "lemon",
    "magic", "night", "ocean", "paper", "queen", "robot", "smile", "tiger", "water", "zebra",
    
    # 6 Letters
    "banana", "camera", "dragon", "energy", "forest", "guitar", "helmet", "island", "jungle", "kitten",
    "lizard", "monkey", "nature", "orange", "planet", "puzzle", "rocket", "shadow", "tunnel", "wizard",
    
    # 7 Letters
    "balloon", "blanket", "chicken", "diamond", "dolphin", "feather", "harvest", "journey", "kingdom", "lantern",
    "monster", "octopus", "penguin", "pyramid", "rainbow", "scooter", "sunfire", "tornado", "unicorn", "volcano",
    
    # 8 Letters
    "alphabet", "astronaut", "backpack", "butterfly", "dinosaur", "elephant", "flamingo", "fountain", "hedgehog", "hospital",
    "kangaroo", "mountain", "notebook", "painting", "sandcastle", "scorpion", "squirrel", "starfish", "treasure", "umbrella",
    
    # Extra Game Words (mix of fun 5-7 letters)
    "biscuit", "castle", "circus", "cobweb", "cookie", "cowboy", "crystal", "digger", "donkey", "dragonfly",
    "feather", "firefly", "goldfish", "hamster", "jacket", "magnet", "mermaid", "pirate", "pumpkin", "wizard"
]
     return random.choice(dictionary)

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def play():
    p1 = input("Enter Player 1's name: ")
    p2 = input("Enter Player 2's name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    
    while True:
        # Pick and jumble a new word at the start of every round
        picked_word = choose()
        jumbled_word = jumble(picked_word)
        
        if turn % 2 == 0:
            # Player 1's turn
            print(p1," your turn.")
            print("The jumbled word is:", jumbled_word)
            a = input("What do you think the word is? ")
            
            if a == picked_word:
                pp1 += 1
                print("Correct answer! You get a point.")
                print(f"Current Score -> {p1}: {pp1} | {p2}: {pp2}")
            else:
                print("Wrong answer! Better luck next time.")
                print("the correct word is",picked_word)
                
        else:
            # Player 2's turn
            print(p2," your turn.")
            print("The jumbled word is:", jumbled_word)
            a = input("What do you think the word is? ")
            
            if a == picked_word:
                pp2 += 1
                print("Correct answer! You get a point.")
                print(f"Current Score -> {p1}: {pp1} | {p2}: {pp2}")
            else:
                print("Wrong answer! Better luck next time.")
                print("the correct word is",picked_word)

        
        # Ask to continue after the turn is complete
        c = input("\nIf you want to continue press 1, or press 0 to quit: ")
        if c == '0':
            print("\n--- Game Over ---")
            print(f"Final Score -> {p1}: {pp1} | {p2}: {pp2}")
            break
            
        turn += 1

# Start the game
play()