"""
Name: Nathan Orawi
Refactored assignment 1
GitHub URL: https://github.com/cp1404-students/a1-NathanOrawi
Note: push via token   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

"""
from operator import itemgetter

FILE_NAME = "songs.csv"
YEAR_OF_FIRST_RECORDED_SONG = 1860
CURRENT_YEAR = 2023
SONG_LIST_VERSION = 1
SONG_LIST_OWNER = 'Nathan Orawi'

MENU = """Menu:
D - Display songs
A - Add new song
C - Complete a song
Q - Quit"""


def main():
    """
    Makes a list of alphabetically sorted song lists.
    Capable of being manipulated according to the user via the menu,
    The user can Add new songs, can mark songs as learned, can display songs
    and can save songs
    """

    # Dumps from file
    csv_songs = readlines_csv_file()
    songs = make_list_of_sorted_lists(csv_songs)

    # Display a menu of actions for the user to choose from
    print(f"{len(songs)} songs loaded")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            display_song(songs)
        elif choice == 'A':
            title, name, year = get_song()
            add_song(songs, title, name, year)
        elif choice == 'C':
            complete_song(songs)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"{len(songs)} songs saved to {FILE_NAME} \nMake some music!")
    quit_song_list(songs)


def quit_song_list(songs):
    """Quits the program and save the update song list to 'song.csv'"""
    out_file = open(FILE_NAME, 'w')
    for song in songs:
        print(song[0], file=out_file)
    out_file.close()


def complete_song(songs):
    """Marks a song chosen by its number as learned"""
    print("Enter the number of a song to mark as learned.")
    song_number = int(input(">>> ")) - 1
    selected_song = songs.pop(song_number)[0]
    if selected_song.endswith('u'):
        learned_song = [selected_song.replace('u', 'l')]
        return songs.insert(song_number, learned_song)
    else:
        print(f"You have already learned {selected_song[0].split(',')[0]}")


def get_song():
    """Gets song from user"""
    print("Enter details for a new song.")
    new_title = input("Title: ")
    while new_title.strip() == '':
        print("Input can not be blank.")
        new_title = input("Title: ")
    new_name = input("Artist: ")
    while new_name.strip() == '':
        print("Input can not be blank.")
        new_name = input("Artist: ")
    is_valid_input = False
    while not is_valid_input:
        try:
            new_year = int(input("Year: "))
            if new_year <= 0:
                print("Number must be > 0.")
            elif new_year < YEAR_OF_FIRST_RECORDED_SONG or new_year >= CURRENT_YEAR:
                print(f"Song record do not exist in the year {new_year}")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number.")

    return new_title, new_name, new_year


def add_song(songs, new_title, new_name, new_year):
    """Adds a song to the song list"""
    entered_song = [f'{new_title},{new_name},{new_year},u']
    songs.append(entered_song)


def display_song(songs):
    """Formats and Display a list of songs"""
    for i, song in enumerate(songs):
        title = song[0].split(',')[0]
        name = song[0].split(',')[1]
        year = song[0].split(',')[2]
        learned_status = '*' if song[0].split(',')[3] == 'u' else ''
        print(f"{i + 1:>2}. {learned_status:<2} {title:<30} - {name:<25} {year:>04}")


def readlines_csv_file():
    """read lines from a csv file"""
    with open(FILE_NAME, 'r') as csv_file:
        songs = csv_file.readlines()
    return songs


def make_list_of_sorted_lists(strings):
    """Makes a list of list that is sorted alphabetically"""
    songs = [[song.rstrip('\n')] for song in strings]
    return sorted(songs)


if __name__ == '__main__':
    main()
