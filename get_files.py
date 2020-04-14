import shutil
import os
import sys

directory = sys.argv[1]

for root, dirs, files in os.walk(directory):
    for dr in dirs:
        dr = root+"/"+dr
        # find folders without subfolders (= lowest level)
        if len(next(os.walk(dr))[1]) == 0:
            # direct superior directory
            up = dr[:dr.rfind("/")]
            # move files from lowest level one level up
            for f in os.listdir(dr):
                shutil.move(dr+"/"+f, up+"/"+f)
