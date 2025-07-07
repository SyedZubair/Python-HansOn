import os
def exercise6():
    try:
        os.remove("greetings.txt")
        print("Exercise 6: File 'greeting.txt' deleted.")
    except FileNotFoundError:
        print("Exercise 6: File 'greeting.txt' not found.")

exercise6()