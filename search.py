######## Seyhan Van Khan
######## Searching module
######## Linear, binary, binary tree search
######## January 2018

from analysis import *

################################# LINEAR SEARCH ################################


def LinearSearch(_list, number):
    start = StartClock()
    steps = 0
    for num in _list:
        steps += 1
        if num == number:
            return True, steps, TimeTaken(start)
    return False, steps, TimeTaken(start)


################################# BINARY SEARCH ################################


def BinarySearch(_list, number):
    start = StartClock()
    steps = 0
    gap = item = len(_list) / 2
    while _list[int(item)] != number and gap >= 1:
        steps += 1
        gap /= 2
        if _list[int(item)] < number:
            item += gap
        elif _list[int(item)] > number:
            item -= gap
    return (True if _list[int(item)] == number else False), steps, TimeTaken(start)


############################## BINARY SEARCH TREE ##############################


class Node:
    def __init__(self, newValue):
        self.nodeValue = newValue
        self.leftNode = self.rightNode = None


    def Insert(self, newValue):
        if newValue == self.nodeValue:
            return
        if newValue < self.nodeValue:
            if self.leftNode:
                self.leftNode.Insert(newValue)
            else:
                self.leftNode = Node(newValue)
        else:
            if self.rightNode:
                self.rightNode.Insert(newValue)
            else:
                self.rightNode = Node(newValue)


    def RecursiveSearch(self, newValue, steps):
        if newValue == self.nodeValue:
            steps += 1
            return True, steps
        if newValue < self.nodeValue:
            steps += 1
            return self.leftNode.RecursiveSearch(newValue, steps) if self.leftNode else (False, steps)
        else:
            steps += 1
            return self.rightNode.RecursiveSearch(newValue, steps) if self.rightNode else (False, steps)


def BinaryTreeSearch(_list, number):
    start = StartClock()

    tree = Node(_list[0])
    for element in _list[1:]:
        tree.Insert(element)

    found, steps = tree.RecursiveSearch(number, 0)

    return found, steps, TimeTaken(start)


############################### SEARCH FUNCTIONS ###############################


searchMethods = {   "Linear":LinearSearch,
                    "Binary":BinarySearch,
                    "Binary Search Tree":BinaryTreeSearch
                    }
