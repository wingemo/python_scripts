import pdf
import os
import time

if __name__ == "__main__":
    bash()

def ask(script):
    os.system("clear")
    print(script)
    return input()

def bash():
    data = ask("BASH \n")
    if data == "pdf":
        pdf.execute(ask("PDF \n"))
        bash()
    else:
        print("ERROR")
        time.sleep(5)
        bash()
 
