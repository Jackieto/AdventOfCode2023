
"""
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
"""


input = open("./inputs/day2")

separators = ":"
cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
for line in input:

    game = line.split(separators,1)
    idx = int( game[0].strip("Game") )
    grabs = game[1].strip("\n").split(";")
    """
    print(game)
    print(idx)
    print(attemps)
    """
    viableGrab = True
    it = 0
    while viableGrab and it < len(grabs):
        for g in grabs:
            attemp = g.split(",")
            for att in attemp:
                att_strip = att.strip()
            # print(att_strip)
                att_split= att_strip.split(" ")
            # print(att_split)
                n = int(att_split[0])
                colour = att_split[1]

                if cubes.get(colour) < n:
                    viableGrab = False

        it += 1           
           
    if viableGrab is True:
        total += idx

        #multiple cubes

print(total)



