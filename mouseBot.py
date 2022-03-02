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


def runMouse(time_to_stop):
    condition_to_run = True
    while condition_to_run:
        # get current time
        current_time = time.localtime()
        # get screen size
        root = tk.Tk()
        # TODO work on limiting the screen clicks to bottom right
        screen_width = root.winfo_screenwidth() - 500
        screen_height = root.winfo_screenheight() - 1000

        # pass random value to axis
        posx = randint(screen_height, screen_width)
        posy = randint(screen_height, screen_width)

        if platform.system() == "Darwin":
            from src.macMouse import macMoveClick

            macMoveClick(posx, posy)
        elif platform.system() == "Windows":
            from src.winMouse import winMoveClick

            winMoveClick(posx, posy)

        if current_time > time_to_stop:
            iso_time = time.strftime("%Y-%m-%dT%H:%M:%SZ", time_to_stop)
            print(f"[ + ] It's after {iso_time} now, stopping this script.")
            condition_to_run = False

        # Interval in seconds
        time.sleep(10)


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
    main()
