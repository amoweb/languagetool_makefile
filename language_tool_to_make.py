#!/usr/bin/python

import re, sys

regex = re.compile(r"^.*Line ([0-9]+), column ([0-9]+), (Rule ID:.*)$", re.IGNORECASE)
filename = sys.argv[1]

for line in sys.stdin:
    if ".) Line" in line:
        linemodif = regex.sub(filename+":\\1:\\2: \\3", line)
        linemodif = linemodif.replace("\n", "")
        linemodif = linemodif.replace("\r", "")
        sys.stdout.write(linemodif)
    elif "Message: " in line:
        line = line.replace("Possible typo: ", "")
        sys.stdout.write(line.replace("Message: ", "  "))


