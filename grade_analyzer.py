import csv

print("--- IGCSE MOCK EXAM ANALYZER ---")

top_student = ""
top_average = 0

math_scores = []
physics_scores = []
cs_scores = []

with open("scores.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Student"]
        math = int(row["Math"])
        physics = int(row["Physics"])
        cs = int(row["ComputerScience"])

        math_scores.append(math)
        physics_scores.append(physics)
        cs_scores.append(cs)

        avg = round((math + physics + cs) / 3, 1)
        print(f"{name}: Average = {avg}%")

        if avg > top_average:
            top_average = avg
            top_student = name

print(f"\nTop Performer: {top_student} ({top_average}%)")

print("\n--- SUBJECT CLASS AVERAGES ---")
subjects = {
    "Math": round(sum(math_scores) / len(math_scores), 1),
    "Physics": round(sum(physics_scores) / len(physics_scores), 1),
    "CompSci": round(sum(cs_scores) / len(cs_scores), 1)
}

for subject, avg in subjects.items():
    bar = "█" * int(avg // 2)
    print(f"{subject:8} | {bar} {avg}%")