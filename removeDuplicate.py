
lines_seen = set() # holds lines already seen
outfile = open("musics.txt", "w")
for line in open("myPlaylists.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
