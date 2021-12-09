import numpy as np

with open("input_day_5") as input_data:
    input_xy = input_data.read().split("\n")
coordinates = [list(map(int, input_xy[index].replace(" -> ", ",").split(","))) for index in range(len(input_xy))]


def find_grid_size(lst):
    x = 0
    y = 0
    for coord in lst:
        for i in range(0, len(coord), 2):
            if coord[i] > x:
                x = coord[i]
        for i in range(1, len(coord), 2):
            if coord[i] > y:
                y = coord[i]
    zeros_grid = np.zeros((x + 1, y + 1), dtype=int)
    return zeros_grid


grid = find_grid_size(coordinates)


def create_diagram(coord_grid, coord_lst):
    for num in coord_lst:
        if num[1] == num[3]:
            if num[0] > num[2]:
                coord_grid[num[1]][num[2]: num[0] + 1] += 1
            else:
                coord_grid[num[1]][num[0]: num[2] + 1] += 1
        elif num[0] == num[2]:
            if num[1] > num[3]:
                coord_grid[num[3]: num[1] + 1, num[0]] += 1
            else:
                coord_grid[num[1]: num[3] + 1, num[0]] += 1
        else:
            if num[0] < num[2] and num[1] < num[3]:
                while num[0] <= num[2]:
                    coord_grid[num[1]][num[0]] += 1
                    num[0] += 1
                    num[1] += 1
            elif num[0] < num[2] and num[1] > num[3]:
                while num[0] <= num[2]:
                    coord_grid[num[1]][num[0]] += 1
                    num[0] += 1
                    num[1] -= 1
            elif num[0] > num[2] and num[1] < num[3]:
                while num[2] <= num[0]:
                    coord_grid[num[1]][num[0]] += 1
                    num[0] -= 1
                    num[1] += 1
            else:
                while num[2] <= num[0]:
                    coord_grid[num[1]][num[0]] += 1
                    num[0] -= 1
                    num[1] -= 1
    return coord_grid

diagram = create_diagram(grid, coordinates)


def counting_dangerous_areas(diagram):
    counter = 0
    for y in diagram:
        for x in y:
            if x > 1:
                counter += 1
    return counter


dangerous_areas = counting_dangerous_areas(diagram)
print(dangerous_areas)
