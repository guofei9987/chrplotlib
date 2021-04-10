import sys
import time


def hide_cursor():
    print('\033[?25l')


def animation(update_func, interval=range(100), pause=0.2):
    hide_cursor()
    for i in interval:
        update_func(i)
        time.sleep(pause)
