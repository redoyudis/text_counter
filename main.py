from pathlib import Path


def line_counter(path):
    file_path = Path(path)
    with open(file_path, 'r') as file:
        line_count = sum(1 for x in file)
    return line_count


lines = line_counter('email_text.txt')
print(f'this files has {lines} lines')
