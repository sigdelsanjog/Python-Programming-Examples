from university_grading_system import UniversityGradingSystem
from grading_strategies import PercentageGradingStrategy, GPAGradingStrategy


def main():    
    try:
        marks = float(input("Enter your marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Invalid marks! Please enter a value between 0 and 100.")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return
    
    grading_system = UniversityGradingSystem(PercentageGradingStrategy())
    
    print("\n--- Percentage-Based Grading ---")
    result_pct = grading_system.grade_student(marks)
    print(f"Marks: {result_pct['marks']}/{result_pct['max_marks']}")
    print(f"Percentage: {result_pct['percentage']:.2f}%")
    print(f"Division: {result_pct['division']}")
    
    # GPA-Based Grading
    print("\n--- GPA-Based Grading ---")
    grading_system.set_strategy(GPAGradingStrategy())
    result_gpa = grading_system.grade_student(marks)
    print(f"Marks: {result_gpa['marks']}/{result_gpa['max_marks']}")
    print(f"GPA: {result_gpa['gpa']:.1f}/4.0")
    print(f"Grade: {result_gpa['grade']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
