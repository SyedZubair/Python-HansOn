


'''with open("Students.csv", "w") as file:
    file.write("Name,Score\nBharah, 85\nUsha, 89\nSupreeth, 85\n")
'''

def exercise7():
    # Create and write to CSV
    with open("Students.csv", "w") as file:
        #file.write("Name,Score\nAlice,85\nBob,90\nCharlie,78\n")
        file.write("Name, Score\nBharah, 85\nUsha, 89\nSupreeth, 85\n")
    
    # Read and calculate average
    try:
        with open("students.csv", "r") as file:
            lines = file.readlines()[1:]  # Skip header
            scores = [int(line.split(",")[1]) for line in lines]
            print(scores)
            average = sum(scores) / len(scores) if scores else 0
            print(f"Exercise 7: Average score from 'students.csv': {average}")
    except FileNotFoundError:
        print("Exercise 7: File 'students.csv' not found.")
    except ValueError:
        print("Exercise 7: Invalid data in 'students.csv'.")

exercise7()