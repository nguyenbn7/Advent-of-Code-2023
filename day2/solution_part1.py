game_ids = []
threshold = {"red": 12, "green": 13, "blue": 14}
with open("./input.txt") as file:
    while line := file.readline():
        game, string_cubes = line.split(":")
        game_id = int(game.split()[1])
        cube_sets = string_cubes.strip().split(";")
        cubes = []
        impossible = False
        for set in cube_sets:
            tmp = list(map(lambda a: a.strip().split(), set.split(",")))
            for s in tmp:
                k = int(s[0])
                if k > threshold[s[1]]:
                    impossible = True
                    break
            if impossible:
                break

        if not impossible:
            game_ids.append(game_id)

print(sum(game_ids))
