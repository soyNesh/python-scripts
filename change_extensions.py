import os
import sys

folder = sys.argv[1]
original_extension = sys.argv[2]
replacement = sys.argv[3] if sys.argv[3] != "" else ""

for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(original_extension, replacement)
    output = os.rename(infilename, newname)
