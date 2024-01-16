# Spotify Analyzer
# Author: Kyle Wang
# 16 January 2024

import csv

# Open the file
with open("./spotify.csv") as f:
    # ----- Search for all Drake songs
    # ----- Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Make a list to store all Drake songs
    drake_songs = []

    # Create a counter to store the current line #
    line_num = 0
    
    # For every line in the file
    for line in csv_reader:
        # If it's the first line, print out all the headings
        if line_num == 0:
            print("The column are: ")

           # print(", ".join(line))
            for item in line:
                print(item)

                line_num += 1
        else:
            # If the artist for this song is Drake
            # Store the song info in the list
            # ---- artist, song title, danceability
            if "drake" in line['artist'].lower():
                drake_songs.append((
                    line["artist"],
                    line["song_title"],
                    line["danceability"]
                ))
                line_num += 1

# Print only the drake songs
# that have the danceability of 0.5 or higher                
