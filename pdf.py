import os
result = []

def execute(filename):
    for root, dir, files in os.walk(search_path):
        if sys.argv in files:
            result.append(os.path.join(root, filename))
    print result



