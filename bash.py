"""
This is a comment written in
more than just one line
"""

import os
import time

def ask(script):
    os.system("cls")
    print(script)
    return input()

def art():
    art = open('art.txt', 'r')
    return art.read()


def bash():
    data = ask(art())
    if data == "pdf":
        ask("PDF \n")
        bash()
    elif data == "loc":
        ask("LOC \n")
        bash()
    else:
        print("ERROR")
        time.sleep(5)
        bash()

if __name__ == "__main__":
    bash()
