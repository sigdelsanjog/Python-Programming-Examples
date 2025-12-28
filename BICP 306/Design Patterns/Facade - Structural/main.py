from config import UniversitySettings, GradingPolicy
from university_facade import UniversityFacade


def main():
    print("FACADE - Structural Design Pattern")
    """
    Step 1 Import necessary configuration from config.py via the import done in line 1
    from config import UniversitySettings, GradingPolicy

    We have used this configuration in previous Creational design patterns Singleton and Factory Method.
    Here, we will use these configurations to initialize the Facade and its services.
    """
    settings = UniversitySettings()
    policy = GradingPolicy()

    """
    # Create the Facade with the configuration
    """
    university = UniversityFacade(settings=settings, policy=policy)

    print(f"\n{settings.university_name} - {settings.fiscal_year}")
    print("-" * 60)

    # Now client only needs to interact with the Facade, not individual services
    print("\n=== Department Information ===")
    print(university.show_admission_info())
    print(university.show_finance_info())

    print("\n=== Exam & Result Processing ===")
    marks = 50
    print(f"Marks: {marks}")
    evaluation = university.evaluate_exam(marks)
    print(f"Evaluation: {evaluation['percentage']:.2f}% - Pass: {evaluation['pass']}")
    print(university.generate_result(marks))

    print("\n=== Complete Student Report (via Facade convenience method) ===")
    report = university.get_complete_student_report(marks)
    print(f"University: {report['university']}")
    print(f"Admission: {report['admission_info']}")
    print(f"Finance: {report['finance_info']}")
    print(f"Exam Evaluation: {report['exam_evaluation']}")
    print(f"Final Result: {report['result']}")

if __name__ == "__main__":
    main()
