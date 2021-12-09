with open("input_day_8") as input_data:
    data_lst_1 = input_data.read().split("\n")
    data_lst_2 = [element.split(" | ") for element in data_lst_1]
    signal_patterns = [element[0].split(" ") for element in data_lst_2]
    four_digits = [element[1].split(" ") for element in data_lst_2]


def decode_ten_digits(pattern_lst):
    pattern_lst.sort(key=lambda item: (len(item), item))
    decoded_value = {1: "", 2: "", 3: "", 4: "", 5: [], 6: "", 7: "", 8: "", 9: "", 0: ""}

    for signal in pattern_lst:
        if len(signal) == 2:
            decoded_value[1] = signal
        elif len(signal) == 3:
            decoded_value[7] = signal
        elif len(signal) == 4:
            decoded_value[4] = signal
        elif len(signal) == 5:
            if decoded_value[1][0] in signal and decoded_value[1][1] in signal:
                decoded_value[3] = signal
            else:
                if len(decoded_value[5]) < 1:
                    decoded_value[5].append(signal)
                else:
                    decoded_value[5].append(signal)
                    var = ""
                    for letter in decoded_value[5][0]:
                        if letter in decoded_value[5][1]:
                            continue
                        else:
                            var += letter
                    if var[0] in decoded_value[4] and var[1] in decoded_value[4]:
                        decoded_value[2] = decoded_value[5][1]
                        decoded_value[5] = decoded_value[5][0]
                    else:
                        decoded_value[2] = decoded_value[5][0]
                        decoded_value[5] = decoded_value[5][1]
        elif len(signal) == 6:
            if decoded_value[1][0] not in signal or decoded_value[1][1] not in signal:
                decoded_value[6] = signal
            elif decoded_value[4][0] in signal and decoded_value[4][1] in signal and decoded_value[4][2] in signal and decoded_value[4][3] in signal:
                decoded_value[9] = signal
            else:
                decoded_value[0] = signal
        else:
            decoded_value[8] = signal

    return decoded_value


def decode_four_digits(four_digits_lst, decoded_ten_digits_dict):
    sum_values = ""

    for digit in four_digits_lst:
        if len(digit) == 2:
            sum_values += "1"
        elif len(digit) == 3:
            sum_values += "7"
        elif len(digit) == 4:
            sum_values += "4"
        elif len(digit) == 7:
            sum_values += "8"
        elif len(digit) == 5:
            var = ""
            for letter in digit:
                if letter in decoded_ten_digits_dict[2]:
                    var += letter
                else:
                    continue
            if len(var) == 5:
                sum_values += "2"
            else:
                var = ""
                for letter in digit:
                    if letter in decoded_ten_digits_dict[3]:
                        var += letter
                    else:
                        continue
                if len(var) == 5:
                    sum_values += "3"
                else:
                    sum_values += "5"
        elif len(digit) == 6:
            var = ""
            for letter in digit:
                if letter in decoded_ten_digits_dict[0]:
                    var += letter
                else:
                    continue
            if len(var) == 6:
                sum_values += "0"
            else:
                var = ""
                for letter in digit:
                    if letter in decoded_ten_digits_dict[6]:
                        var += letter
                    else:
                        continue
                if len(var) == 6:
                    sum_values += "6"
                else:
                    sum_values += "9"

    return int(sum_values)


def adding_all_output_values(patterns_lst, digits_lst):
    output_values_sum = 0

    for index in range(0, len(patterns_lst)):
        output_values_sum += decode_four_digits(digits_lst[index], decode_ten_digits(patterns_lst[index]))

    return output_values_sum


print(adding_all_output_values(signal_patterns, four_digits))
