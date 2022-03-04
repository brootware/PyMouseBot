#!/usr/bin/env python
"""
Utility to move Mouse
"""

import time
import argparse
import time
from random import randint
import tkinter as tk
import platform
import sys


def runMouse(time_to_stop):
    print(
        """\
 ______          ______                            ______             
(_____ \        |  ___ \                          (____  \       _    
 _____) )   _   | | _ | | ___  _   _  ___  ____    ____)  ) ___ | |_  
|  ____/ | | |  | || || |/ _ \| | | |/___)/ _  )  |  __  ( / _ \|  _) 
| |    | |_| |  | || || | |_| | |_| |___ ( (/ /   | |__)  ) |_| | |__ 
|_|     \__  |  |_||_||_|\___/ \____(___/ \____)  |______/ \___/ \___)
       (____/                                                         
                                          
                +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
                |P|o|w|e|r|e|d| |b|y| |B|r|o|o|t|w|a|r|e|
                +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
    """
    print("If you want to stop the bot, press CTRL+C in the terminal")
    )
    condition_to_run = True
    while condition_to_run:
        # get current time
        current_time = time.localtime()
        # get screen size
        root = tk.Tk()
        # TODO work on limiting the screen clicks to bottom right
        screen_width = root.winfo_screenwidth() - 1000
        screen_height = root.winfo_screenheight() - 500

        # pass random value to axis
        posx = randint(screen_height, screen_width)
        posy = randint(screen_height, screen_width)

        if platform.system() == "Darwin":
            from src.macMouse import macMoveClick

            macMoveClick(posx, posy)
        elif platform.system() == "Windows":
            from src.winMouse import winMoveClick

            winMoveClick(posx, posy)
        else:
            print(
                f"[ - ] Seems like you are running on unsupported platform {platform.system()}. Currently the bot is only supported on Windows and Mac(Darwin)."
            )

        if current_time > time_to_stop:
            iso_time = time.strftime("%H:%M:%S", time_to_stop)
            print(f"[ + ] It's after {iso_time} now, stopping this script.")
            condition_to_run = False

        # Interval in seconds
        time.sleep(15)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("time", help="Please enter the time in HH:MM:SS format")
    args = parser.parse_args()

    try:
        current_date = time.strftime("%Y %m %d")
        args.time = time.strptime(f"{current_date} {args.time}", "%Y %m %d  %H:%M:%S")
    except ValueError:
        print(f"[ - ] The time you entered is incorrect. Try again in HH:MM:SS format")

    runMouse(args.time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"[ + ] The bot is stopped by the user. Good bye!")
        sys.exit()
