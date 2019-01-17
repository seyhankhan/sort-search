######## Seyhan Van Khan
######## Analysis module
######## Calculating complexity & time taken
######## January 2018

################################### LIBRARIES ##################################


from math import log10, log
from time import time


################################### CONSTANTS ##################################


# If time taken lower, outputs "< 0.001 secs"
TIME_MINIMUM = 0.001
# Time taken measurement precision
TIME_DECIMAL_PLACES = int(abs(log10(TIME_MINIMUM)))


################################# COMPLEXITIES #################################


# Formats long numbers with commas
def FormatNum(n, decimalPlaces):
    if decimalPlaces == int:
        n = list(str(int(n)))
    else:
        n = list(str(round(n, decimalPlaces)))

    intlength = n.index(".") if "." in n else len(n)
    for i in range (3, intlength, 3):
        n.insert((intlength - i), ",")

    return ''.join(n)

# Complexity functions
def O1(n):
    return '1'
def On(n):
    return FormatNum(n, int)
def Ologn(n):
    return FormatNum(log(n, 2), int)
def Onlogn(n):
    return FormatNum(n * log(n, 2), int)
def On2(n):
    return FormatNum(n ** 2, int)

# A dict is created from these values whereby
## For each list of 3 values, add to dict:
#### first value : {"text": second value, "function": third value}
#### "Merge" : {"text": 'n log n', "function": Onlogn}

bigOmega_list = [   ["Linear",              '1',        O1],
                    ['Binary',              '1',        O1],
                    ["Binary Search Tree",  '1',        O1],
                    ["Bubble",              'n',        On],
                    ["Merge",               'n log n',  Onlogn]
                    ]

bigO_list = [   ["Linear",              'n',        On],
                ["Binary",              'log n',    Ologn],
                ["Binary Search Tree",  'n log n',  Onlogn],
                ["Bubble",              'n^2',      On2],
                ["Merge",               'n log n',  Onlogn]
                ]

bigOmega = {}
bigO = {}

for complexity in ((bigOmega, bigOmega_list), (bigO, bigO_list)):
    for method in complexity[1]:
        complexity[0][method[0]] = {"text": method[1], "function": method[2]}


################################ TIME FUNCTIONS ################################


def StartClock():
    return time()

def TimeTaken(start):
    timeTaken = time() - start
    # If time taken lower, just outputs "< 0.001 secs"
    if timeTaken < TIME_MINIMUM:
        return "< " + FormatNum(TIME_MINIMUM, TIME_DECIMAL_PLACES)
    else:
        return FormatNum(timeTaken, TIME_DECIMAL_PLACES)
