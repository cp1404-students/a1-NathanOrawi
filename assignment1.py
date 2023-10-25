"""
Name: Nathan Orawi
Date started: 25/10/2023
GitHub URL: https://github.com/cp1404-students/a1-NathanOrawi.git
"""
FILE_NAME = "songs.csv"

MENU = """Menu:
D - Display songs
A - Add new song
C - Complete a song
Q - Quit"""


def main():
    """..."""
    read_from_file(FILE_NAME)
    print("Song List 1.0 - by Nathan Orawi")
    menu()


def menu():
    """display a menu for the user to choose from"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            print("Songs 1")
            print("Songs 2")
            print("Songs 3")
        elif choice == 'A':
            print("Song added")
        elif choice == 'C':
            print("Song complete")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("X songs saved to songs.csv")


def read_from_file(file):
    """reads from a file"""
    in_file = open(file)
    song = in_file.read()
    print(song)
    in_file.close()


if __name__ == '__main__':
    main()
