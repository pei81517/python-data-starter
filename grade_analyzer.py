import csv

print("--- IGCSE MOCK EXAM ANALYZER ---")

top_student = ""
top_average = 0

with open("scores.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Student"]
        math = int(row["Math"])
        physics = int(row["Physics"])
        cs = int(row["ComputerScience"])

        avg = round((math + physics + cs) / 3, 1)
        print(f"{name}: Average = {avg}%")

        if avg > top_average:
            top_average = avg
            top_student = name

print(f"\nTop Performer: {top_student} ({top_average}%)")