import random
# Block 1: TCM Clinical Case Database & Text Normalizer

tcm_cases = [
    {
        "category": "Dizziness",
        "formula": "Bu Zhong Yi Qi Tang",
        "pattern": "Spleen Qi Sinking",
        "symptoms": "Dizziness worse with exertion, severe fatigue, tiredness after stool, organ/rectal prolapse",
        "tongue_pulse": "Pale tongue; Deficient/Soft pulse",
        "why_better": "Tastes dull; dizziness directly worsens after physical exertion or bowel movements."
    },
    {
        "category": "Headache",
        "formula": "Wu Zhu Yu Tang",
        "pattern": "Jueyin Vertex Headache",
        "symptoms": "Vertex (top of head) headache, severe cold stomach, spitting clear watery saliva, acid vomiting, icy limbs",
        "tongue_pulse": "Pale tongue, white coat; Deep Wiry Slow pulse",
        "why_better": "Pain specifically at top of head with cold stomach acid/water vomiting."
    },
    {
        "category": "Fever",
        "formula": "Baihu Tang",
        "pattern": "Yangming Qi-Level Heat",
        "symptoms": "4 Bigs: Big Fever, Big Thirst, Big Sweat, Big Surging Pulse. High heat with no aversion to cold",
        "tongue_pulse": "Dry yellow coat; Surging Large pulse",
        "why_better": "Extreme interior heat; uses Gypsum to generate fluids."
    }
]

def clean_text(text):
    # Makes text lowercase and removes extra spaces at the start/end
    return text.strip().lower()

def run_quiz(cases):
    remaining_cases = list(cases)
    round_num = 1
    first_round_correct = 0

    print("=== TCM CLINICAL CASE EXAM TRAINER ===")
    while remaining_cases:
        random.shuffle(remaining_cases)  # Randomize order so she learns symptoms, not sequence
        print(f"\n========== ROUND {round_num} ({len(remaining_cases)} cases) ==========")
        missed_cases = []

        for i, case in enumerate(remaining_cases, 1):
            print(f"\n--- Case {i}: {case['category']} ---")
            print(f"Symptoms: {case['symptoms']}")
            print(f"Tongue & Pulse: {case['tongue_pulse']}")

            pattern_guess = clean_text(input("Step 1 - Enter Pattern: "))
            formula_guess = clean_text(input("Step 2 - Enter Formula: "))

            # Flexible check for pattern (keyword match) + exact check for formula
            pattern_ok = len(pattern_guess) >= 4 and pattern_guess in clean_text(case["pattern"])
            formula_ok = formula_guess == clean_text(case["formula"])

            if pattern_ok and formula_ok:
                print("Full Marks! Both Pattern & Formula correct.")
                if round_num == 1:
                    first_round_correct += 1
            else:
                print(f"Review Needed -> Pattern: {case['pattern']} | Formula: {case['formula']}")
                missed_cases.append(case)

            print(f"Why Better?: {case['why_better']}")

        # Next round only quizzes the cases she missed!
        remaining_cases = missed_cases
        round_num += 1

    accuracy = (first_round_correct / len(cases)) * 100
    print(f"\n100% MASTERY ACHIEVED in {round_num - 1} round(s)!")
    print(f"First-Attempt Exam Accuracy: {first_round_correct}/{len(cases)} ({accuracy:.0f}%)")

run_quiz(tcm_cases)