
import sys
import os
import shutil
import glob
from pathlib import Path
from pyfiglet import figlet_format
from colorama import init
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected


def get_full_tt(path):
    user = path[path.index("@") + 1: path.index(")")]

    cmd = "lynx -dump " + path + " | grep -oP 'https://www.tiktok.com/@" + user + \
        "/video/[0-9]+' | uniq -u > url_list && youtube-dl -a url_list"

    os.system(cmd)

    src = "./"
    dst = os.path.join(src, user + "-tt/")

    print("dst: ", dst)

    if not os.path.isdir(dst):
        Path(dst).mkdir(parents=True, exist_ok=True)

    for file in glob.glob(os.path.join(src, "*.unknown_video")):
        Path(file).with_suffix("")
        Path(file).with_suffix(".mp4")
        shutil.move(file, dst)


def get_video(url):
    cmd = "youtube-dl " + url
    os.system(cmd)


def get_usr_req():
    cool = False
    option = 0
    while (not cool):
        try:
            option = int(input("Please choose an option: "))
            cool = True
        except ValueError:
            print("Please choose a correct option...")

    return option


def main():
    exit_program = False
    usr_req = 0

    print(figlet_format('Tik Tok\nDownloader\nBy: N3sh', font='slant'))

    while not exit_program:

        print("Welcome!")
        print("Here's what you can do:")
        print("1. Download all videos from user")
        print("2. Download an specific video")
        print("3. Exit")

        usr_req = get_usr_req()

        if usr_req == 1:
            path = input("Enter HTML path: ")
            get_full_tt(path)
        elif usr_req == 2:
            link = input("Enter the video URL:")
            get_video(link)
        elif usr_req == 3:
            exit_program = True
        else:
            print("Please choose a correct option...")

    print("Goodbye!")


if __name__ == "__main__":
    main()
