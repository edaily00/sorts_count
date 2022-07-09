def bubble_count(list):

    comparisons = 0
    exchanges = 0
    length = len(list) - 1

    for pass_num in range(length):
        for index in range(length - pass_num):
            comparisons += 1
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
                exchanges += 1
    both = (comparisons, exchanges)
    return both


def insertion_count(list):

    comparisons = 0
    exchanges = 0

    for i in range(1, len(list)):
        j = i
        while list[j - 1] > list[j] and j > 0:
            temp = list[j-1]
            list[j - 1] = list[j]
            list[j] = temp
            j -= 1
            comparisons += 1
        exchanges += 1

    both = (comparisons, exchanges)
    return both

