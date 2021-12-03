with open("input_day_3.txt") as input_data:
    binary_data_lst = input_data.read().split("\n")


def calculate_power_consumption(lst):
    gamma_rate = ""
    epsilon_rate = ""
    count_lst = [[] for _ in lst[0]]

    for index in range(len(count_lst)):
        for num in lst:
            count_lst[index] += num[index]
    for sub_lst in count_lst:
        if sub_lst.count("0") > sub_lst.count("1"):
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    for num in gamma_rate:
        if num == "0":
            epsilon_rate += "1"
        else:
            epsilon_rate += "0"
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

    return power_consumption


print(calculate_power_consumption(binary_data_lst))


def oxygen_generator_rating(lst):
    index = 0
    new_lst = lst
    while len(new_lst) >= 1:
        if len(new_lst) == 1:
            break
        else:
            count_lst = [element[index] for element in new_lst]
            if count_lst.count("1") >= count_lst.count("0"):
                new_lst = [element for element in new_lst if element[index] == "1"]
            else:
                new_lst = [element for element in new_lst if element[index] == "0"]
            index += 1

    return int(new_lst[0], 2)


def co2_scrubber_rating(lst):
    index = 0
    new_lst = lst
    while len(new_lst) >= 1:
        if len(new_lst) == 1:
            break
        else:
            count_lst = [element[index] for element in new_lst]
            if count_lst.count("0") <= count_lst.count("1"):
                new_lst = [element for element in new_lst if element[index] == "0"]
            else:
                new_lst = [element for element in new_lst if element[index] == "1"]
            index += 1

    return int(new_lst[0], 2)


def life_support_rating(lst):
    return oxygen_generator_rating(lst) * co2_scrubber_rating(lst)


print(life_support_rating(binary_data_lst))
