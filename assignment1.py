"""
Name: Nathan Orawi
Date started: 25/10/2023
Date submitted: 28/10/2023
GitHub URL: https://github.com/cp1404-students/a1-NathanOrawi
Note: push via token   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

"""
from operator import itemgetter

FILE_NAME = "songs.csv"
SONGS = []  # List of dictionaries
YEAR_OF_FIRST_RECORDED_SONG = 1860
CURRENT_YEAR = 2023

MENU = """Menu:
D - Display songs
A - Add new song
C - Complete a song
Q - Quit"""


def main():
    """main adds the fields to 'song.csv' then makes
    a list of dictionaries of field value pairs and
    is manipulated according to the user in the menu """

    # Prepares csv file for processing
    add_fields_to_csv()
    make_dictionary()

    # Display of program structure is set here
    read_csv_file()
    print("Song List 1.0 - by Nathan Orawi")
    menu()  # Where 'song.csv' is manipulated


def menu():
    """display a menu of actions for the user to choose from"""
    print(f"{len(SONGS)} songs loaded")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            display_song()
        elif choice == 'A':
            add_song()
        elif choice == 'C':
            complete_song()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"{len(SONGS)} songs saved to {FILE_NAME} \nMake some music!")
    quit_song_list()


def display_song():
    """Takes the song dictionary then formats and Displays it """
    song_number = 1
    number_of_learned_song = 0
    sorted_songs = sorted(SONGS, key=itemgetter('year'))  # list of song dictionaries
    for sorted_song_field_to_song_value in sorted_songs:
        title, artist, year, learned_status = sorted_song_field_to_song_value.values()
        if learned_status == 'u':
            learned_status = '*'
            number_of_learned_song += 1
        else:
            learned_status = ''
        print(f"{song_number:>2}. {learned_status:2} {title:35} - {artist:25} ({year:>04})")
        song_number += 1
    print(
        f"{(len(sorted_songs) - number_of_learned_song)} songs learned, {number_of_learned_song} songs still to learn.")


def add_song():
    print("Enter details for a new song.")
    new_title = input("Title: ")
    while new_title.strip() == '':
        print("Input can not be blank.")
        new_title = input("Title: ")
    new_artist = input("Artist: ")
    while new_artist.strip() == '':
        print("Input can not be blank.")
        new_artist = input("Artist: ")
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

    SONGS.append({'title': new_title, 'artist': new_artist, 'year': str(new_year), 'learned status': 'u'})
    print(f"{new_title} by {new_artist} ({new_year}) added to song list.")


def complete_song():
    """marks a song chosen by its number as learned"""
    learned_index = 0
    print("Enter the number of a song to mark as learned.")
    sorted_song_fields_to_song_values = sorted(SONGS, key=itemgetter('year'))
    is_valid_input = False
    while not is_valid_input:
        mark = int(input(">>> "))
        if mark <= 0:
            print("Number must be > 0.")
        elif mark > len(sorted_song_fields_to_song_values):
            print("Invalid song number")
        else:
            for index, item in enumerate(sorted_song_fields_to_song_values):
                if index == (mark - 1):
                    title, artist, year, learned_status = item.values()
                    if learned_status == 'l':
                        print(f"You have already learned {title}")
                    else:
                        print(f"{title} by {artist} learned")
                        learned_index = index
                    break
            sorted_song_fields_to_song_values[learned_index]['learned status'] = 'l'
            is_valid_input = True


def quit_song_list():
    """quits the program and save the update song list to 'song.csv'"""
    out_file = open("songs.csv", 'w')
    for song in SONGS:
        # My favourite method is pop(). I had to find a way to incorporate it into the code :)
        title = (list(song.values())).pop(0)
        artist = (list(song.values())).pop(1)
        year = (list(song.values())).pop(2)
        learned_status = (list(song.values())).pop(3)
        songs_csv = ("{},{},{},{}".format(title, artist, year, learned_status))

        print(songs_csv, file=out_file)
    out_file.close()


def add_fields_to_csv():
    """adds field to the first line of the csv file"""
    with open("songs.csv") as file:
        first_line = file.readline()
        if first_line != 'title,artist,year,learned status\n':
            csv_field = 'title,artist,year,learned status\n'
            in_file = open("songs.csv")
            line = in_file.read()
            fielded_file = csv_field + line
            in_file.close()

            out_file = open("songs.csv", 'w')
            print(fielded_file.rstrip('\n'), file=out_file)
            out_file.close()


def read_csv_file():
    """reads from a file and display csv song line by line"""
    in_file = open(FILE_NAME)
    songs_csv = in_file.read()
    in_file.close()
    print(songs_csv)


def make_dictionary():
    """makes a song dictionary from csv file"""
    with open(FILE_NAME, 'r') as csv_file:
        songs_csv = csv_file.readlines()
        song_fields = [fields.strip() for fields in songs_csv[0].split(',')]
        for song_csv in songs_csv[1:]:
            song_values = [value.strip() for value in song_csv.split(',')]
            song_field_to_song_value = {field: value for field, value in zip(song_fields, song_values)}
            SONGS.append(song_field_to_song_value)


if __name__ == '__main__':
    main()
