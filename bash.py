"""
This is a comment written in
more than just one line
"""

import os
import time
import loc

def ask(script):
    os.system("cls")
    print(script)
    return input()

def bash():
    data = ask("BASH")
    if data == "pdf":
        ask("PDF \n")
        bash()
    elif data == "loc":
        loc.execute(ask("LOC \n"))
        bash()
    else:
        print("ERROR")
        time.sleep(2)
        bash()

if __name__ == "__main__":
    bash()
