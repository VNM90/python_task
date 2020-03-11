import datetime

YEAR = 2
MONTH = 1
DAY = 0

try:
    def import_file(file='input.txt'):
        date_table = []
        with open(file, 'r') as f:
            for item in f.readlines():
                date_table.append(item.strip().split('/'))
            return date_table
except FileNotFoundError:
    print('File not found')


def convert_to_int():
    try:
        date_table = import_file()
        results = [int(item) for item in date_table[0]]
        return sorted(results)
    except ValueError:
        list_to_str = '/'.join([str(item) for item in date_table[0]])
        print(list_to_str + ' is illigal')


def date_finder():
    result = convert_to_int()
    try:
        for item in result:
            if item == 2000 or item == 0:
                item = 0
            elif (item < 2000 or item > 2999) and item > 31:
                smallest_date = 'Wrong date'
            elif result[YEAR] < 31 and result[MONTH] > 12 and result[DAY] < 31:
                smallest_date = datetime.date(result[1] + 2000, result[0], result[2])
            elif result[YEAR] < 31 and result[MONTH] <= 12 and result[DAY] < 31:
                smallest_date = datetime.date(result[0] + 2000, result[1], result[2])
            else:
                smallest_date = datetime.date(result[YEAR], result[DAY], result[MONTH])
        return smallest_date
    except ValueError:
        print("Wrong date")

print(date_finder())
