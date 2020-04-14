import os
import sys
folder = sys.argv[1]
for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.webp', '')
    output = os.rename(infilename, newname)
