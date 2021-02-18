from nested_data import albums

while True:
    # print("Please choose your album (invalid choice exits): ")
    # for index, (title, artist, year, songs) in enumerate(albums):
    #    print("{}: {}, {}, {}, {}".format(index + 1, title, artist, year, songs))

    # for index, value in enumerate(albums):
    #    title, artist, year, songs = value
    #    print(index, title, artist, year, songs)

    SONGS_LIST_INDEX = 3
    SONG_TITLE_INDEX = 1

    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break

    # print(albums[choice - 1])
    # print(songs_list)
    # print()

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice -1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    # else:
    #    break

    print("=" * 40)