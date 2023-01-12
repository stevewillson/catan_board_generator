# %%
import random
from random import shuffle

random.seed()

hexNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
              '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
hexTypes = ["wool", "wool", "wool", "wool",
            "ore", "ore", "ore",
            "brick", "brick", "brick",
            "grain", "grain", "grain", "grain",
            "lumber", "lumber", "lumber", "lumber",
            "desert"
            ]
adjacentHexNumbers = {
    '1':  ['2', '4', '5'],
    '2':  ['1', '3', '5', '6'],
    '3':  ['2', '6', '7'],
    '4':  ['1', '5', '8', '9'],
    '5':  ['1', '2', '4', '6', '9', '10'],
    '6':  ['2', '3', '5', '7', '10', '11'],
    '7':  ['3', '6', '11', '12'],
    '8':  ['4', '9', '13'],
    '9':  ['4', '5', '8', '10', '13', '14'],
    '10': ['5', '6', '9', '11', '14', '15'],
    '11': ['6', '7', '10', '12', '15', '16'],
    '12': ['7', '11', '16'],
    '13': ['8', '9', '14', '17'],
    '14': ['9', '10', '13', '15', '17', '18'],
    '15': ['10', '11', '14', '16', '18', '19'],
    '16': ['11', '12', '15', '19'],
    '17': ['13', '14', '18'],
    '18': ['14', '15', '17', '19'],
    '19': ['15', '16', '18']
}

# %%
# for each hex on the game board, assign a type


def assignHexTypes():
    hexTypeBoard = {}
    shuffle(hexTypes)
    for space in hexNumbers:
        hexTypeBoard[space] = hexTypes.pop(0)
    return hexTypeBoard

# %%


def assignHexNumbers(hexTypeBoard):
    numberedBoard = {}
    for space in hexNumbers:
        if hexTypeBoard[space] != 'desert':
            numberedBoard[space] = 0
        else:
            numberedBoard[space] = 'D'

    gameNumbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    shuffle(gameNumbers)
    for space in hexNumbers:
        if numberedBoard[space] == 0:
            numberedBoard[space] = gameNumbers.pop(0)
    return numberedBoard

# %%


def checkBoard(assignedBoard):
    for space in hexNumbers:
        # get the assigned number and check against the other assigned numbers
        curNum = assignedBoard[space]
        for adjNum in adjacentHexNumbers[space]:
            if curNum == 6 and assignedBoard[adjNum] == 6:
                return False
            if curNum == 6 and assignedBoard[adjNum] == 8:
                return False
            if curNum == 8 and assignedBoard[adjNum] == 6:
                return False
            if curNum == 8 and assignedBoard[adjNum] == 8:
                return False
            # do not allow adjacent numbers
            if curNum == assignedBoard[str(adjNum)]:
                return False
    return True


# %%
hexTypeBoard = assignHexTypes()
numberedBoard = assignHexNumbers(hexTypeBoard)
while not checkBoard(numberedBoard):
    numberedBoard = assignHexNumbers(hexTypeBoard)

for space in numberedBoard.keys():
    if space == '1':
        print(f"    ", end='')
    elif space == '4':
        print()
        print(f"  ", end='')
    elif space == '8':
        print()
    elif space == '13':
        print()
        print(f"  ", end='')
    elif space == '17':
        print()
        print(f"    ", end='')

    print(f'{numberedBoard[space]:>2}', end='')
    print('  ', end='')

print()
print()

for space in hexTypeBoard.keys():
    if space == '1':
        print(f"            ", end='')
    elif space == '4':
        print()
        print(f"      ", end='')
    elif space == '8':
        print()
    elif space == '13':
        print()
        print(f"      ", end='')
    elif space == '17':
        print()
        print(f"            ", end='')

    print(f'{hexTypeBoard[space]:>6}', end='')
    print('      ', end='')

# %%


def board_layout(hexTypeBoard, numberedBoard):
    res_01 = f"{hexTypeBoard['1']:^8}"
    num_01 = f"{numberedBoard['1']:^8}"
    res_02 = f"{hexTypeBoard['2']:^8}"
    num_02 = f"{numberedBoard['2']:^8}"
    res_03 = f"{hexTypeBoard['3']:^8}"
    num_03 = f"{numberedBoard['3']:^8}"
    res_04 = f"{hexTypeBoard['4']:^8}"
    num_04 = f"{numberedBoard['4']:^8}"
    res_05 = f"{hexTypeBoard['5']:^8}"
    num_05 = f"{numberedBoard['5']:^8}"
    res_06 = f"{hexTypeBoard['6']:^8}"
    num_06 = f"{numberedBoard['6']:^8}"

    res_07 = f"{hexTypeBoard['7']:^8}"
    num_07 = f"{numberedBoard['7']:^8}"
    res_08 = f"{hexTypeBoard['8']:^8}"
    num_08 = f"{numberedBoard['8']:^8}"
    res_09 = f"{hexTypeBoard['9']:^8}"
    num_09 = f"{numberedBoard['9']:^8}"
    res_10 = f"{hexTypeBoard['10']:^8}"
    num_10 = f"{numberedBoard['10']:^8}"
    res_11 = f"{hexTypeBoard['11']:^8}"
    num_11 = f"{numberedBoard['11']:^8}"
    res_12 = f"{hexTypeBoard['12']:^8}"
    num_12 = f"{numberedBoard['12']:^8}"

    res_13 = f"{hexTypeBoard['13']:^8}"
    num_13 = f"{numberedBoard['13']:^8}"
    res_14 = f"{hexTypeBoard['14']:^8}"
    num_14 = f"{numberedBoard['14']:^8}"
    res_15 = f"{hexTypeBoard['15']:^8}"
    num_15 = f"{numberedBoard['15']:^8}"
    res_16 = f"{hexTypeBoard['16']:^8}"
    num_16 = f"{numberedBoard['16']:^8}"
    res_17 = f"{hexTypeBoard['17']:^8}"
    num_17 = f"{numberedBoard['17']:^8}"
    res_18 = f"{hexTypeBoard['18']:^8}"
    num_18 = f"{numberedBoard['18']:^8}"

    res_19 = f"{hexTypeBoard['19']:^8}"
    num_19 = f"{numberedBoard['19']:^8}"

    board = (
        f"\n"
        f"                       ______\n"
        f"                      /      \\\n"
        f"               ______/{res_01}\\______\n"
        f"              /      \\{num_01}/      \\\n"
        f"       ______/{res_04}\\______/{res_02}\\______\n"
        f"      /      \\{num_04}/      \\{num_02}/      \\\n"
        f"     /{res_08}\\______/{res_05}\\______/{res_03}\\\n"
        f"     \\{num_08}/      \\{num_05}/      \\{num_03}/\n"
        f"      \\______/{res_09}\\______/{res_06}\\______/\n"
        f"      /      \\{num_09}/      \\{num_06}/      \\\n"
        f"     /{res_13}\\______/{res_10}\\______/{res_07}\\\n"
        f"     \\{num_13}/      \\{num_10}/      \\{num_07}/\n"
        f"      \\______/{res_14}\\______/{res_11}\\______/\n"
        f"      /      \\{num_14}/      \\{num_11}/      \\\n"
        f"     /{res_17}\\______/{res_15}\\______/{res_12}\\\n"
        f"     \\{num_17}/      \\{num_15}/      \\{num_12}/\n"
        f"      \\______/{res_18}\\______/{res_16}\\______/\n"
        f"             \\{num_18}/      \\{num_16}/\n"
        f"              \\______/{res_19}\\______/\n"
        f"                     \\{num_19}/\n"
        f"                      \\______/\n"

    )
    print(board)


board_layout(hexTypeBoard, numberedBoard)
