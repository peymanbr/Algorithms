from operator import itemgetter
from itertools import groupby

data = [1, 1, 4, 5, 4, 5, 4, 5, 4, 5, 2, 2, 2, 2, 3, 4, 4, 2, 1, 5, 12, 4, 2, 7, 11,
        10, 8, 7, 6, 5, 2, 2, 3, 8, 7, 8, 3 ,3, 3, 3, 3, 3, 5, 4, 4, 4, 4, 6, 6, 2,
        2, 4, 5, 2, -1, -2, 3, -1, 4, 5, 6, 7, 3, 10, 15, 11, 10, 10, 8, 9, 11, 13,
        12, 10, 15, 17, 22]

def find_largest_consecutive_numbers_sequence():
    diff = [i for i, (a, b) in enumerate(zip(data, data[1:])) if abs(a - b) <=5]
    ls = []
    for k, g in groupby(enumerate(diff), lambda x: x[0] - x[1]):
        ls.append(list(map(itemgetter(1), g)))
    result = max(ls, key=len)
    return (result[0], result[-1]+1)

def main():
    print(find_largest_consecutive_numbers_sequence())

if __name__ == '__main__':
    main()
