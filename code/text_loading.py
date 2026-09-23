from pathlib import Path

def get_content(lines):
    file = open(Path("books/5"))
    text = ""
    for i in range(lines):
        text += file.readline()
    return text