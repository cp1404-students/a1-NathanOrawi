"""
Name: Nathan Orawi
Date started: 25/10/2023
GitHub URL: https://github.com/cp1404-students/a1-NathanOrawi.git
"""
FILE_NAME = "songs.csv"
SONGS = []

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
            data = get_data()
            format_data(data)
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
    """reads from a file and display string line by line"""
    in_file = open(file)
    songs = in_file.read()
    print(songs)
    in_file.close()
    return songs


def create_nested_list_from_file(file):
    in_file = open(file)
    songs = []
    for line in in_file:
        song = (line.strip().split('  '))
        # print(song)
        songs.append(song)
    # print(songs)
    in_file.close()
    return songs


def format_data(data):
    """Format and Display subject details with supporting data """
    for parts in data:
        for part in parts:
            pass
        print(f"{parts[3]:3} {parts[0]:30} - {parts[1]:20} ({parts[2]})")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILE_NAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        data.append(parts)
        # print("----------")
    input_file.close()
    return data


if __name__ == '__main__':
    main()
