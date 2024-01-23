from pathlib import Path
import sys

def line_counter(path):
    file_path = Path(path)
    with open(file_path, 'r') as file:
        line_count = sum(1 for x in file)
    return line_count

argument = sys.argv
path = argument[1]

lines = line_counter(path)
print(f'this files has {lines} lines')
