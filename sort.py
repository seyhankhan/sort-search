######## Seyhan Van Khan
######## Sorting module
######## Bubble, merge sort
######## January 2018

from analysis import *

################################## BUBBLE SORT #################################


def BubbleSort(numbers, order):
    steps = 0
    start = StartClock()
    item = 0
    limit = len(numbers) - 1
    while limit > 0:
        if item == limit:
            limit -= 1
            item = 0
        if (   (numbers[item] >= numbers[item + 1] and order == "ASC")
            or (numbers[item] <= numbers[item + 1] and order == "DESC")
            ):
            numbers[item], numbers[item + 1] = numbers[item + 1], numbers[item]
        item += 1
        steps += 1
    return numbers, steps, TimeTaken(start)


################################## MERGE SORT ##################################


def MergeSort(list_, order):

    def Merge(list1, list2, order, steps):
        new = []
        index_1 = index_2 = 0

        while len(new) < len(list1) + len(list2):
            steps += 1

            if (   list1[index_1] < list2[index_2] and order == "ASC"
                or list1[index_1] > list2[index_2] and order == "DESC"
                ):
                new.append(list1[index_1])
                index_1 += 1
                if index_1 == len(list1):
                    steps += len(list2[index_2:])
                    new += list2[index_2:]
                    break
            else:
                new.append(list2[index_2])
                index_2 += 1
                if index_2 == len(list2):
                    steps += len(list1[index_1:])
                    new += list1[index_1:]
                    break

        return new, steps

    def SplitMerge(list_, order, steps):
        if len(list_) > 2:
            mid = len(list_) // 2
            firstHalf, steps = SplitMerge(list_[:mid], order, steps)
            secondHalf, steps = SplitMerge(list_[mid:], order, steps)
            return Merge(firstHalf, secondHalf, order, steps)

        elif len(list_) == 2:
            return Merge([list_[0]], [list_[1]], order, steps)

        else:
            return list_, steps


    start = StartClock()
    list_, steps = SplitMerge(list_, order, 0)
    return list_, steps, TimeTaken(start)



################################ SORT FUNCTIONS ################################


sortMethods = {"Bubble" : BubbleSort,
                "Merge" : MergeSort
                }
