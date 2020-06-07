def resolve_boat_collision_at(curr_map, y, x):
    if len(curr_map) > y and len(curr_map[y]) > x:
        if curr_map[y][x] == " ":
            return 0
        if curr_map[y][x] == "B":
            return 1
        if curr_map[y][x] == "P":
            return 2



def move_boat(curr_map, y, x):
    collision_res = resolve_boat_collision_at(curr_map, y + 1, x)
    if collision_res == 0:
        curr_map[y][x] = " "
        curr_map[y + 1][x] = "B"
    elif collision_res == 1:
        if resolve_boat_collision_at(curr_map, y + 1, x - 1) == 0:
            curr_map[y][x] = " "
            curr_map[y + 1][x - 1] = "B"
        elif resolve_boat_collision_at(curr_map, y + 1, x + 1) == 0:
            curr_map[y][x] = " "
            curr_map[y + 1][x + 1] = "B"


def get_next_state_map(curr_map, next_map):
    for index_row in range(len(curr_map) - 1, -1, -1):
        for index_tile, tile in enumerate(curr_map[index_row]):
            if tile == "B":
                move_boat(curr_map, index_row, index_tile)
