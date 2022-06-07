# ToDo:
#  Start from a shape / icon

import random

adjectives = ["cyberpunk", "steampunk", "goth",
              "emo", "lilac", "purple", "red",
              "orange", "yellow", "pink", "green",
              "blue", "salmon", "brown", "grey",
              "white", "indigo", "artstationHQ",
              "trending on /r/art", "Junji Ito",
              "Vincent Van Gogh", "disney", "pixar",
              "evil", "rendered in unreal engine high quality",
              "Mordor", "at night", "during the day",
              "wizard", "cherry"]

nouns = ["forest", "robot", "Microsoft Excel",
         "city", "duel", "Mark Zuckerberg",
         "Elon Musk", "space", "hamburger",
         "eye", "robotic"]


def get_phrase():
    '''
    Ideas:
     1- Noun
     2- Adjective + Noun
     3- Adjective + Adjective + Noun
     4- Adjective + Adjective
     5- Noun | Adjective
     6- Noun | Adjective with weights
     7- Noun | Adjective | Adjective
     8- Noun | Adjective | Adjective with weights
     9- !Noun | Adjective
     10- Noun | !Adjective
     11- Noun | !Adjective | !Adjective
     Can weight stuff with XYZ:3 -> will weight XYZ 3 times more
     Use XYZ:-1 to remove it from image
    '''
    choice = (random.randint(1, 17) % 12) + 1

    if choice == 1:
        return nouns[random.randint(0, len(nouns) - 1)]

    if choice == 2:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " " \
               + nouns[random.randint(0, len(nouns) - 1)]

    if choice == 3:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " " \
               + adjectives[random.randint(0, len(adjectives) - 1)] \
               + " " \
               + nouns[random.randint(0, len(nouns) - 1)]

    if choice == 4:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " " \
               + adjectives[random.randint(0, len(adjectives) - 1)]

    if choice == 5:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)]

    if choice == 6:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":" \
               + str(random.randint(1, 3)) \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)] \
               + ":" \
               + str(random.randint(1, 3))

    if choice == 7:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " | " \
               + adjectives[random.randint(0, len(adjectives) - 1)] \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)]

    if choice == 8:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":" \
               + str(random.randint(1, 3)) \
               + " | " \
               + adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":" \
               + str(random.randint(1, 3)) \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)] \
               + ":" \
               + str(random.randint(1, 3))

    if choice == 9:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":-1" \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)]

    if choice == 10:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)] \
               + ":-1"

    if choice == 11:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + " | " \
               + adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":-1" \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)]

    if choice == 12:
        return adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":-1" \
               + " | " \
               + adjectives[random.randint(0, len(adjectives) - 1)] \
               + ":-1" \
               + " | " \
               + nouns[random.randint(0, len(nouns) - 1)]


if __name__ == '__main__':
    for i in range(0, 1000):
        print(get_phrase())
