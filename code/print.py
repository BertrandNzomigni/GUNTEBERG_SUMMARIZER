from pathlib import Path

file = open(Path("books/1"))

for i in range(10):
    print(file.readline())