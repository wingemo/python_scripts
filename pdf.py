"""
This is a comment written in 
more than just one line
"""

import os

result = []

def execute(filename):
    for root, dir, files in os.walk("C:/"):
        if sys.argv in files:
            os.startfile(filename)
            result.append(os.path.join(root, filename))
    print result



