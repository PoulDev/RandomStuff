import string
import random
import time
import sys
import os
from ctypes import c_int, c_byte, Structure, byref, windll
os.system('')

class _CursorInfo(Structure):
    _fields_ = [("size", c_int),
                ("visible", c_byte)]

# https://github.com/billythegoat356/pystyle
def set_cursor_visible(visible):
    ci = _CursorInfo()
    handle = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
    ci.visible = visible
    windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))

def hacker_print(text, enter=True):
    set_cursor_visible(False)
    for corrupted_start_from in range(0, len(text)+1):
        print(text[:corrupted_start_from] + ''.join(
            random.choices(string.ascii_letters, k=len(text[corrupted_start_from:]
        ))), end='\r')
        time.sleep(0.05)
    if enter: print()
    set_cursor_visible(True)

def typing_print(*texts):
    set_cursor_visible(False)
    num_of_texts = len(texts)
    for index, text in enumerate(texts):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print(' ' * len(text))
        time.sleep(0.6)
        if index < num_of_texts-1:
            sys.stdout.write("\033[F")
            for index in range(0, len(text)):
                sys.stdout.write('\r' + text[:len(text)-1-index] + ' ' * (len(text[index:])-1))
                sys.stdout.flush()
                time.sleep(0.05)
    set_cursor_visible(True)

hacker_print('Hacker Style Typing', False)
time.sleep(0.5)
hacker_print('Pretty cool, right?')
time.sleep(1)
typing_print('https://github.com/PoulDev', 'https://poulandlorix.gq/')
