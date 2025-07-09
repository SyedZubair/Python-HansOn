#file handling operations

from datetime import datetime

def fileReading():
    print("File Reading \n")

    #reading the content from the file file.txt
    try:
        with open("file.txt", "r") as file:
            lines = file.readlines()
            print(lines)
            if lines:
                content = file.read()
                print(content)
            else:
                print("file is empty")
    except FileNotFoundError:
        print("file doesn't exists in the given path")

def fileWriting():
    try:
        with open("file.txt", 'w') as file:
            ts = datetime.now()
            file.write(f"\n Last Accessed: {ts}")
    except FileNotFoundError:
        print("file doesn't exists in the given path")

fileReading()

fileWriting()

fileReading()
