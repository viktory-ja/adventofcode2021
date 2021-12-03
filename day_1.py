with open("input_day_1") as input_data:
    depths = input_data.read().split("\n")
depths_lst = list(map(int, depths))


def increased_measurements(lst):
    counter = 0
    for index in range(len(lst)):
        if index == 0:
            continue
        if lst[index] > lst[index - 1]:
            counter += 1
        else:
            continue
    return counter


print(increased_measurements(depths_lst))


def sum_of_three_measurement(lst):
    sum_lst = []
    for index in range(len(lst) - 2):
        sum_lst.append(lst[index] + lst[index + 1] + lst[index + 2])
    return sum_lst


print(increased_measurements(sum_of_three_measurement(depths_lst)))
