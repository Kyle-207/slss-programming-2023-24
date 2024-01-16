# Spotify Analyzer
# Author: Kyle Wang
# 16 January 2024

import csv

# Create a function that searches through data
# Finds all songs from a given artist

def find_all_songs(artist: str) -> list:
    """Searches through a set of data and
    returns all songs """
    # Open the file
    with open("./spotify.csv") as f:
        # ----- Search for all artist's songs
        # ----- Use linear search
        # Create a csv reader object
        csv_reader = csv.DictReader(f)

        # Make a list to store all songs
        songs = []

        # Create a counter to store the current line #
        line_num = 0
        
        # For every line in the file
        for line in csv_reader:
            # If it's the first line, print out all the headings
            if line_num == 0:
                # print("The column are: ")

                # print(", ".join(line))
                    
                # for item in line:
                #     print(item)

                    line_num += 1
            else:
                # If the artist for this song is given artist
                # Store the song info in the list
                # ---- artist, song title, danceability
                if artist.lower() in line['artist'].lower():
                    songs.append((
                        line["artist"],
                        line["song_title"],
                        line["danceability"]
                    ))
                    line_num += 1
        return songs
drake_songs = find_all_songs("drake")
ed_sheeran_songs = find_all_songs("ed sheeran")
kendrick_songs = find_all_songs("kendrick")

print(find_all_songs("drake"))

# Print only the drake songs
# that have the danceability of 0.5 or higher

for song in kendrick_songs:
    if float(song[-1]) >= 0.5:
        print(song)
 
