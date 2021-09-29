"""
This is a comment written in 
more than just one line
"""

import pdf
import loc
import os
import time

if __name__ == "__main__":
    bash()

def ask(script):
    os.system("clear")
    print(script)
    return input()

def art(): 
    art = with open('art.txt', 'r')
    return art.read()

def bash():
    data = ask(art())
    if data == "pdf":
        pdf.execute(ask("PDF \n"))
        bash()
    elif data == "loc"
        loc.execute(ask("LOC \n"))
        bash()
    else:
        print("ERROR")
        time.sleep(5)
        bash()
 
