#!/usr/bin/env python
from random import randint, seed

# max artists
maxA = 3
# load file
aFile = open("/home/rjanardhana/git/spotify-random/artists.txt", "r")
artists = aFile.read().split("\n")
# strip white spaces
artists = [a.strip() for a in artists if a.strip()]
aLen = len(artists)
count = 1
seed()
for i in xrange(maxA):
    # print artist
    j = randint(0, aLen-1)
    print "%d. %s" % (count, artists[j])
    # remove artist from list
    del artists[j]
    # update count and len
    aLen -= 1
    count += 1
