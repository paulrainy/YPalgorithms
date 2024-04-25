def d_remove_num(days, wins):
    wins = wins.split()
    output_wins = ''
    if len(wins) == days:
        for win in wins:
            if win != '0':
                output_wins += str(win)
                output_wins += ' '
        return output_wins
    else:
        return ValueError('Number of wins cannot be less than or equal to zero.')


def f_data_base(num, array):
    if len(array) == num:
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] == array[j]:
                    return array[i]
                else:
                    continue

        return ValueError('Equal key didnt find')
    else:
        return ValueError('Array must be the same size as num.')
