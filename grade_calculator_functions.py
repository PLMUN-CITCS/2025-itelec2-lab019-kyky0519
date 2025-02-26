def get_student_score() -> int:
    while True:
        try:
            score = int(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

student_score = get_student_score()
grade = calculate_grade(student_score)
print(f"Your Grade is: {grade}")
