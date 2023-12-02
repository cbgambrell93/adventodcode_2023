inputs = open("d2in.txt", "r")

red = 12
green = 13
blue = 14
games = {}
total_score = 0
current_game_valid = True

for line in inputs.readlines():
    red_min = 0
    blue_min = 0
    green_min = 0
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
        int_cube = int(cube)
        match color_match:
            case 'red':
                if int_cube > red_min:
                    red_min = int_cube
            case 'blue':
                if int_cube > blue_min:
                    blue_min = int_cube
            case 'green':
                if int_cube > green_min:
                    green_min = int_cube
    round_total = red_min*blue_min*green_min
    total_score += round_total

print(total_score)