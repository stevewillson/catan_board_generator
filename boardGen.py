# %%
import random
from random import shuffle
boardSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9,
               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
adjacent = {
    1:  [2, 4, 5],
    2:  [1, 3, 5, 6],
    3:  [2, 6, 7],
    4:  [1, 5, 8, 9],
    5:  [1, 2, 4, 6, 9, 10],
    6:  [2, 3, 5, 7, 10, 11],
    7:  [3, 6, 11, 12],
    8:  [4, 9, 13],
    9:  [4, 5, 8, 10, 13, 14],
    10: [5, 6, 9, 11, 14, 15],
    11: [6, 7, 10, 12, 15, 16],
    12: [7, 11, 16],
    13: [8, 9, 14, 17],
    14: [9, 10, 13, 15, 17, 18],
    15: [10, 11, 14, 16, 18, 19],
    16: [11, 12, 15, 19],
    17: [13, 14, 18],
    18: [14, 15, 17, 19],
    19: [15, 16, 18]
}

# %%
# for each hex in the square, put a number
assignedHexBoard = {}

hexes = ["sheep", "sheep", "sheep", "sheep",
         "stone", "stone", "stone",
         "brick", "brick", "brick",
         "wheat", "wheat", "wheat", "wheat",
         "wood", "wood", "wood", "wood",
         "desert"
         ]

shuffle(hexes)
for space in boardSpaces:
    strSpace = str(space)
    assignedHexBoard[strSpace] = hexes.pop(0)

# %%
assignedBoard = {}


def assignBoard():
    numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    for space in boardSpaces:
        strSpace = str(space)
        if assignedHexBoard[strSpace] != 'desert':
            assignedBoard[strSpace] = 0
        else:
            assignedBoard[strSpace] = 'D'

    shuffle(numbers)
    for space in boardSpaces:
        strSpace = str(space)
        if assignedBoard[strSpace] == 0:
            numToAssign = numbers.pop(0)
            assignedBoard[strSpace] = numToAssign
    return assignedBoard

# %%


def checkBoard(assignedBoard):
    for space in boardSpaces:
        # get the assigned number and check against the other assigned numbers
        curNum = assignedBoard[str(space)]
        for adjNum in adjacent[space]:
            if curNum == 6 and assignedBoard[str(adjNum)] == 6:
                return False
            if curNum == 6 and assignedBoard[str(adjNum)] == 8:
                return False
            if curNum == 8 and assignedBoard[str(adjNum)] == 6:
                return False
            if curNum == 8 and assignedBoard[str(adjNum)] == 8:
                return False
            # do not allow adjacent numbers
            # if curNum == assignedBoard[str(adjNum)]:
                # return False
    return True


# %%
newBoard = assignBoard()
while not checkBoard(newBoard):
    newBoard = assignBoard()

for space in newBoard.keys():
    if space == str(1):
        print(f"    ", end='')
    elif space == str(4):
        print()
        print(f"  ", end='')
    elif space == str(8):
        print()
    elif space == str(13):
        print()
        print(f"  ", end='')
    elif space == str(17):
        print()
        print(f"    ", end='')

    print(f'{newBoard[space]:>2}', end='')
    print('  ', end='')

print()
print()

for space in newBoard.keys():
    if space == str(1):
        print(f"            ", end='')
    elif space == str(4):
        print()
        print(f"      ", end='')
    elif space == str(8):
        print()
    elif space == str(13):
        print()
        print(f"      ", end='')
    elif space == str(17):
        print()
        print(f"            ", end='')

    print(f'{assignedHexBoard[space]:>6}', end='')
    print('      ', end='')


def board_layout():
    res_01 =f"{hexes[2].resource:^8}"
    num_01 = f"{hexes[2].number:^8}"
    board = (
        f"\n"
        f"                       ______\n"
        f"                      /      \\\n"
        f"               ______/{res_01}\\______\n"
        f"              /      \\{num_01}/      \\\n"
        f"       ______/        \\______/        \\\n"
        f"      /      \\        /      \\        /\n"
        f"     /        \\______/        \\______/\n"
        f"     \\        /      \\        /\n"
        f"      \\______/        \\______/\n"
    )