inputs = open("d2in.txt", "r")

red = 12
green = 13
blue = 14
games = {}
total_score = 0
current_game_valid = True

for line in inputs.readlines():
    line = line.rstrip('\n')
    a, b = line.split(":")
    b = b.split(" ")
    for i, cube in enumerate(b):
        try:
           num_cub = int(cube) 
        except:
            continue
        color_match = b[i+1].rstrip(',')
        color_match = color_match.rstrip(';')
        match color_match:
            case 'red':
                if num_cub > red:
                    current_game_valid = False
            case 'blue':
                if num_cub > blue:
                    current_game_valid = False
            case 'green':
                if num_cub > green:
                    current_game_valid = False                 
    if current_game_valid == True:
        a = a.split(" ")
        total_score += int(a[1])
    current_game_valid = True

print(total_score)
