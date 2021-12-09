with open("input_day_7") as input_data:
    data = list(map(int, input_data.readline().split(",")))


def find_cheapest_outcome_part_one(lst):
    num_dict = {key: lst.count(key) for key in sorted(lst)}
    uniq_num_lst = [num for num in num_dict.keys()]
    new_lst = [num for num in range(0, uniq_num_lst[-1] + 1)]

    num_ind1 = new_lst.copy()[int(len(new_lst) / 2 - 1)]
    num_ind2 = new_lst.copy()[int(len(new_lst) / 2)]

    min_fuel = 0
    fuel_1 = 0

    fuel_2 = 0

    while len(new_lst.copy()) > 1:
        for key in num_dict.keys():
            fuel_1 += abs(num_ind1 - key) * num_dict[key]
            fuel_2 += abs(num_ind2 - key) * num_dict[key]
        if fuel_1 < fuel_2:
            min_fuel = fuel_1
            new_lst = new_lst[:int(len(new_lst) / 2)]
        else:
            min_fuel = fuel_2
            if int(len(new_lst) / 2 - 1) > 0:
                new_lst = new_lst[int(len(new_lst) / 2 - 1):]
            else:
                new_lst = new_lst[int(len(new_lst) / 2):]

        fuel_1 = 0
        fuel_2 = 0
        num_ind1 = new_lst.copy()[int(len(new_lst) / 2 - 1)]
        num_ind2 = new_lst.copy()[int(len(new_lst) / 2)]

    return min_fuel


print(find_cheapest_outcome_part_one(data))


def find_cheapest_outcome_part_two(lst):
    num_dict = {key: lst.count(key) for key in sorted(lst)}
    uniq_num_lst = [num for num in num_dict.keys()]
    new_lst = [num for num in range(0, uniq_num_lst[-1] + 1)]
    num_ind1 = new_lst.copy()[int(len(new_lst) / 2 - 1)]
    num_ind2 = new_lst.copy()[int(len(new_lst) / 2)]

    min_fuel = 0
    fuel_1 = 0
    fuel_2 = 0
    while len(new_lst.copy()) > 1:
        for key in num_dict.keys():
            fuel_1 += int((1 + abs(num_ind1 - key)) / 2 * abs(num_ind1 - key) * num_dict[key])
            fuel_2 += int((1 + abs(num_ind2 - key)) / 2 * abs(num_ind2 - key) * num_dict[key])
        if fuel_1 < fuel_2:
            min_fuel = fuel_1
            new_lst = new_lst[:int(len(new_lst) / 2)]
        else:
            min_fuel = fuel_2
            if int(len(new_lst) / 2 - 1) > 0:
                new_lst = new_lst[int(len(new_lst) / 2 - 1):]
            else:
                new_lst = new_lst[int(len(new_lst) / 2):]
        fuel_1 = 0
        fuel_2 = 0
        num_ind1 = new_lst.copy()[int(len(new_lst) / 2 - 1)]
        num_ind2 = new_lst.copy()[int(len(new_lst) / 2)]

    return min_fuel


print(find_cheapest_outcome_part_two(data))
