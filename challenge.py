# Modify the program so that exits are dictionaries
# with keys being the numbers of the locations and the values being dictionaries
# holding the exits (as they do at present). No change should be needed for the actual code

# Once that is done, create another dictionary that contains words that
# players may use. These words wil be the keys, and their values will be
# a single letter that the program can use to determine which way to go.



locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"
               }

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0} }

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exists are " + availableExits).upper()
    print()
    # parse the user input, using vocabulary dictionary if necessary
    if len(direction) > 1:  # more than one letter, so check vocab
        words = directions.split()
        for word in words:  # does it contain a word we know?
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
