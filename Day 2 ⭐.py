with open("input_day_2") as input_data:
    data_lst = input_data.read().split("\n")

data_lst_2d = [command.split() for command in data_lst]


def calculation_submarine_position(lst):
    horizontal_position = 0
    depth = 0

    for command in lst:
        if command[0] == "forward":
            horizontal_position += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        else:
            depth -= int(command[1])
    return horizontal_position * depth


print(calculation_submarine_position(data_lst_2d))


def calculation_planned_course(lst):
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in lst:
        if command[0] == "forward":
            horizontal_position += int(command[1])
            depth += int(command[1]) * aim
        elif command[0] == "down":
            aim += int(command[1])
        else:
            aim -= int(command[1])

    return horizontal_position * depth


print(calculation_planned_course(data_lst_2d))
