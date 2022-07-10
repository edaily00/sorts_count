#Author: Eric Daily
#Github username: edaily00
#Date: 7/9/2022
#This program counts comparisons and exchanges from different sorting methods
def bubble_count(list):
#Created accumlators to store the numbers
    comparisons = 0
    exchanges = 0
    length = len(list) - 1

    for pass_num in range(length):
        for index in range(length - pass_num):
            #here a comparison is made
            comparisons += 1
            if list[index] > list[index + 1]:
                #inside this statement an exchange occurs
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
                exchanges += 1
    both = (comparisons, exchanges)
    return both


def insertion_count(list):
#Holding numbers
    comparisons = 0
    exchanges = 0

    for i in range(1, len(list)):
        j = i

        while j > 0:
            #Everytime the if state finishes we add to the compare
            comparisons += 1
            if list[j - 1] > list[j]:
                #This is where it exchanges
                temp = list[j-1]
                list[j - 1] = list[j]
                list[j] = temp
                j -= 1
                exchanges += 1
            else: break

    both = (comparisons, exchanges)
    return both

