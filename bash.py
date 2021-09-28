import pdf
import os

bash()

def ask(script):
    os.system("clear")
    print(script)
    return input()

def bash():
    data = ask("BASH \n")
    if data == "pdf":
        pdf.execute(ask("PDF \n"))

