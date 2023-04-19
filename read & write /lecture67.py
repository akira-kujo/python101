contents = ["A Song of Ice and Fire",
            "Elder Scrolls: Skyrim",
            "Laputa: The Castle in the Sky"]

filenames = ["book.txt", "game.txt", "movie.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"./{filename}", "w")
    file.write(content)

