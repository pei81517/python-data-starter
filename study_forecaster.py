# Multi-Subject Exam Score & Study Hour Optimizer

subjects = {
    "Mathematics": {"current": 74.0, "target": 85.0, "gain_per_hr": 2.8, "hours": 0},
    "Physics":     {"current": 68.0, "target": 80.0, "gain_per_hr": 3.2, "hours": 0},
    "Chemistry":   {"current": 79.0, "target": 85.0, "gain_per_hr": 2.2, "hours": 0},
    "English":     {"current": 86.0, "target": 90.0, "gain_per_hr": 1.5, "hours": 0},
}

def calc_average(data, key):
    total = sum(info[key] for info in data.values())
    return total / len(data)

def optimize_study_plan(data, total_hours):
    # Initialize predicted score equal to current score
    for info in data.values():
        info["predicted"] = info["current"]

    for _ in range(total_hours):
        best_subject = None
        best_priority_score = -1

        for name, info in data.items():
            if info["predicted"] >= 100.0:
                continue

            # Diminishing returns: each hour already spent reduces marginal gain by 10%
            effective_gain = info["gain_per_hr"] * (0.9 ** info["hours"])
            # Cap gain so score never exceeds 100%
            actual_gain = min(effective_gain, 100.0 - info["predicted"])

            # Boost priority if subject is still below target grade
            priority = actual_gain * (1.5 if info["predicted"] < info["target"] else 1.0)

            if priority > best_priority_score:
                best_priority_score = priority
                best_subject = name

        if best_subject is None:
            break

        # Allocate 1 hour to the winning subject
        chosen = data[best_subject]
        gain = min(chosen["gain_per_hr"] * (0.9 ** chosen["hours"]), 100.0 - chosen["predicted"])
        chosen["predicted"] += gain
        chosen["hours"] += 1
        
def print_forecast_report(data, total_hours):
    print("\n=== SMART EXAM SCORE & STUDY ALLOCATOR ===")
    print(f"Total Study Budget: {total_hours} hour(s)\n")
    print(f"{'Subject':<14} {'Current':>8} {'Hours':>7} {'Predicted':>10} {'Target':>8} {'Status':>10}")
    print("-" * 62)

    for name, info in data.items():
        status = "TARGET MET" if info["predicted"] >= info["target"] else "IN PROGRESS"
        print(f"{name:<14} {info['current']:>7.1f}% {info['hours']:>6}h {info['predicted']:>9.1f}% {info['target']:>7.1f}% {status:>11}")

    before_avg = calc_average(data, "current")
    after_avg = calc_average(data, "predicted")
    print("-" * 62)
    print(f"Overall Average: {before_avg:.1f}%  ->  {after_avg:.1f}% (+{after_avg - before_avg:.1f}%)")

hours_input = int(input("How many total study hours do you have before exams? "))
optimize_study_plan(subjects, hours_input)
print_forecast_report(subjects, hours_input)