

import random
import copy


def default_values():

    """This function randomly selects 2 or 4 .
     Then puts this values into randomly selected cells
     of the list at the beginning of the game.
      And returns the list with default values."""
    start_lists = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    start = 0
    while start < 2:
        inde1 = random.randint(0, 3)
        inde2 = random.randint(0, 3)
        choice = random.randint(0, 7)
        if choice == 0:
            if start_lists[inde1][inde2] == 0:
                start_lists[inde1][inde2] = 4
        else:
            if start_lists[inde1][inde2] == 0:
                start_lists[inde1][inde2] = 2
        start = start + 1
    return start_lists


def select_val(lst):
    """This function operates AFTER the game started.
    It randomly selects values and  indices and places the values
     in the selected indices and returns the list"""
    while True:
        control = random.randint(0, 7)
        inde1 = random.randint(0, 3)
        inde2 = random.randint(0, 3)
        if control == 1:
            num = 4
        else:
            num = 2
        if lst[inde1][inde2] == 0:
            lst[inde1][inde2] = num

        return lst


def shift(row):
    """This function takes a single row and shifts
    all non_zero values of the row to the the left and
    the returns the shifted row."""
    new_lst = []
    for i in range(4):
        if row[i] != 0:
            new_lst.append(row[i])
    if len(new_lst) < len(row):
        new_lst.extend([0] * (len(row) - len(new_lst)))
    row = new_lst

    return row


def add_tiles(array):
    """This function takes a single row and
     merges identical tiles together to the left and,
     then it returns the merged row."""
    lst = shift(array)
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i + 1] and lst[i + 1] != 0:
            lst[i] *= 2
            lst[i + 1] = 0

    return shift(lst)


def reverse(row):
    """A function takes a single row and reverses
    the order of the elements and returns the reversed row."""
    new_row = []
    for i in range(len(row) - 1, -1, -1):
        new_row.append(row[i])
    row = new_row

    return row


def transpose(lsts):
    """A function takes a list of lists and
    transpose the elements and,
    then returns the transposed list of lists. """

    new_lsts = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            new_lsts[i][j] = lsts[j][i]
    lsts = new_lsts

    return lsts


def merge_right(row):
    """This function takes a single row and
     merges identical tile to the right and
     returns the merged row."""
    row1 = reverse(row)
    row2 = add_tiles(row1)
    row3 = reverse(row2)
    row = row3

    return row


def merge_AllLeft(lsts):
    """This function takes a list of lists and
     merges all rows to the left and
      returns the list of lists"""
    new_lsts = []
    for row in lsts:
        array1 = add_tiles(row)
        new_lsts.append(array1)
    lsts = new_lsts

    return lsts


def merge_AllRight(lsts):
    """Takes a list of lists and merges all
    values to the right and returns the merged list of lists."""
    new_lsts = []
    for row in lsts:
        array1 = merge_right(row)
        new_lsts.append(array1)
    lsts = new_lsts

    return lsts


def merge_up(lsts):
    """Takes list of lists and merges all identical
     tiles up and returns the list of lists."""
    lsts1 = transpose(lsts)
    lsts2 = merge_AllLeft(lsts1)
    lsts3 = shift(lsts2)
    lsts4 = transpose(lsts3)
    lsts = lsts4

    return lsts


def merge_down(lists):
    """The function for merging identical tiles
    down and returns the merged list of lists."""
    lst1 = transpose(lists)
    lst2 = merge_AllRight(lst1)
    lst3 = transpose(lst2)

    lists = lst3

    return lists


def legalShifts(lists):
    """This function checks if there is any
     possible shift in ALL Directions."""

    # making two identical copies of the input lists
    cop_lists1 = copy.deepcopy(lists)
    cop_lists2 = copy.deepcopy(lists)

    if cop_lists2 == merge_AllLeft(cop_lists1):
        if cop_lists2 == merge_AllRight(cop_lists1):
            if cop_lists2 == merge_up(cop_lists1):
                if cop_lists2 == merge_down(cop_lists1):
                    return False
    return True


def checkWin(lists):
    """This function searches if any row
     contains the specified value(s).It tells
      that the player has won if there is(are)
      any specified  value(s) in any row."""
    for lst in lists:
        for value in lst:
            if value == 2048 or value == 4096 or value == 8192 or value == 16384:
                return True
    return False


def displayAsMatrix(lists):
    """This function shows the lists
    to have vertical view."""
    for lst in lists:
        print(lst)


def start_game(lists):
    """A function to start the game(in the first while loop),
    and then to play the game(in the second while loop)."""
    while True:
        choice1 = input("Enter FIRST S OR s :TO START GAME:\n")
        if choice1 == 's':
            print("GAME STARTED!")
            displayAsMatrix(lists)
            break
        else:
            print("Invalid input! Please enter S or s FIRST TO START THE GAME")
            continue

    while True:
        if checkWin(lists):
            print("Congratulations! You Won the game!")

        if not legalShifts(lists):  # the player has no any possible moves
            print("You lost. The game is over!")
            break

            # asks the player to make choice
        choice = input("THEN U or u :to move u,"
                       "D or d :to move dow, "
                       "R or r : to move right,"
                       "L or l : to left, "
                       "Q or q to move le\n").lower()  # changing to lower case

        if choice == 'u':
            lists = merge_up(lists)
            select_val(lists)
            displayAsMatrix(lists)

        elif choice == 'd':
            lists = merge_down(lists)
            select_val(lists)
            displayAsMatrix(lists)

        elif choice == 'r':
            lists = merge_AllRight(lists)
            select_val(lists)
            displayAsMatrix(lists)

        elif choice == 'l':
            lists = merge_AllLeft(lists)
            select_val(lists)
            displayAsMatrix(lists)

        elif choice == 'q':
            print("You are quiting the game!")
            break
        elif choice == 's':
            print("You have already started the game.")
        else:
            print("Incorrect choice. Please enter the correct choice.")


start_game(default_values())
