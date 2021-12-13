import warnings
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

with open("input_day_4") as input_data:
    numbers = list(map(int, input_data.readline().split(",")))
    data = input_data.read().split("\n\n")
    boards = [np.array(list(map(int, board.replace("\n", " ").replace("  ", " ").strip().split(" ")))).reshape(5, 5) for board in data]


def removearray(lst, arr):
    ind = 0
    size = len(lst)
    while ind != size and not np.array_equal(lst[ind], arr):
        ind += 1
    if ind != size:
        lst.pop(ind)
    else:
        raise ValueError('array not found in list.')


def find_last_winning_board(num_lst, boards_array):
    winning_boards = {}
    max_num = 0
    for board in boards_array:
        if np.amax(board) > max_num:
            max_num = np.amax(board)

    replace_zero = max_num + 1

    for index in range(0, len(num_lst)):
        if num_lst[index] == 0:
            num_lst[index] = replace_zero
        else:
            continue

    for board in boards_array:
        board[board == 0] = replace_zero

    winner = "no winner"

    for num in num_lst:
        if winner == "no winner":
            for board in boards_array:
                if num in board:
                    board[board == num] = 0
                else:
                    continue
            for board in boards_array:
                for index in range(0, len(board[0])):

                    if not np.any(board[:, index]):
                        winner = board
                        winner[winner == replace_zero] = 0
                        last_num = num
                        final_score = np.sum(winner) * last_num
                        winning_boards[len(winning_boards) + 1] = [final_score, last_num]
                        removearray(boards_array, board)
                        winner = "no winner"
                        break

                    elif not np.any(board[index, :]):
                        winner = board
                        winner[winner == replace_zero] = 0
                        last_num = num
                        final_score = np.sum(winner) * last_num
                        winning_boards[len(winning_boards) + 1] = [final_score, last_num]
                        removearray(boards_array, board)
                        winner = "no winner"
                        break

                    else:
                        continue
        else:
            break

    return "Score of the first winning board - {}\nScore of the last winning board - {}".format(winning_boards[1][0], winning_boards[len(winning_boards)][0])


print(find_last_winning_board(numbers, boards))
