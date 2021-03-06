#!/usr/bin/env python

"""mapper.py"""

import sys

top10 = ["playoff", "season", "associ", "nba", "play", "coach", "final", "point", "player", "game"]

for line in sys.stdin:
    line = line.strip()
    words = line.split() 
    for i in range(len(words)):
        for j  in range(i+1, len(words)):
            if words[i] == words[j]: continue
            if words[i] in top10 or words[j] in top10:
                print "%s&%s\t%s" % (words[i],words[j], 1)