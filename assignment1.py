"""
Name: Nathan Orawi
Date started: 25/10/2023
GitHub URL: https://github.com/cp1404-students/a1-NathanOrawi.git
"""
FILE_NAME = "songs.csv"
songs = []
once = 1

MENU = """Menu:
D - Display songs
A - Add new song
C - Complete a song
Q - Quit"""


def main():
    """..."""
    is_only_once = True
    if is_only_once:
        make_dictionary()
        is_only_once = False

    read_from_file()
    print("Song List 1.0 - by Nathan Orawi")
    menu()


def menu():
    """display a menu for the user to choose from"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'D':
            format_data()
        elif choice == 'A':
            add_song()
        elif choice == 'C':
            print("Song complete")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("X songs saved to songs.csv")


def read_from_file():
    """reads from a file and display string line by line"""
    in_file = open(FILE_NAME)
    songs_csv = in_file.read()
    in_file.close()
    print(songs_csv)


def make_dictionary():
    """makes a song dictionary from csv file"""
    with open(FILE_NAME, 'r') as csvfile:
        songs_csv = csvfile.readlines()
        fields = [fields.strip() for fields in songs_csv[0].split(',')]
        for line in songs_csv[1:]:
            values = [value.strip() for value in line.split(',')]
            song = {field: value for field, value in zip(fields, values)}
            songs.append(song)


def format_data():
    """Takes the song dictionary then formats and Displays it """
    i = 1
    learned = 0
    sorted_songs = sorted(songs, key=lambda x: x['year'])

    # Print the sorted list
    for song in sorted_songs:
        # print(song)

        # for data in data_list:
        title, artist, year, learned_status = song.values()
        if learned_status == 'u':
            learned_status = '*'
            learned += 1
        else:
            learned_status = ''
        print(f"{i:>2}. {learned_status:2} {title:30} - {artist:25} ({year})")
        i += 1
    print(f"{len(sorted_songs) - learned} songs learned, {learned} songs still to learn")


def add_song():
    print("Enter details for a new song")
    new_title = input("Title: ")
    while new_title.strip() == '':
        print("Input can not be blank")
        new_title = input("Title: ")
    new_artist = input("Artist: ")
    while new_artist.strip() == '':
        print("Input can not be blank")
        new_artist = input("Artist: ")
    is_valid_input = False
    while not is_valid_input:
        try:
            new_year = int(input("Year: "))
            if new_year < 0:
                print("Number must be > 0.")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")

    songs.append({'title': new_title, 'artist': new_artist, 'year': str(new_year), 'learned status': 'u'})
    print(f"{new_title} by {new_artist} ({new_year}) added to song list.")


if __name__ == '__main__':
    main()
