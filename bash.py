import os

bash();

def ask(script):
  os.system('clear')
  print(script)
  return data = input()

def bash():
  data = ask("Bash \n")

  if data == 'pdf':
    data = ask("PDF \n")
