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
    # Step 2: We have created a University facade. 
    # Apply above created configurations which the services listed inside the University facade can use it

    Before implementing the Facade pattern, client needed to interact with multiple services directly like below:
         admission_service = AdmissionService(settings)
         finance_service = FinanceService(settings)
         exam_service = ExamService(policy)
         result_service = ResultService(policy)
      Now, with the Facade pattern, client only needs to interact with the Facade itself:
      university = UniversityFacade(settings=settings, policy=policy)

     Question: How is Facade pattern actually implemented?
      # Answer: The Facade class (UniversityFacade) encapsulates the complexity of initializing and coordinating
      multiple services (AdmissionService, FinanceService, ExamService, ResultService).
      Clients interact with a single Facade object instead of directly managing multiple services.

      Switch to the file university_facade.py to see the implementation of the Facade pattern. 
      Comment on university_facade.py will help you understand the implementation.
    """
    university = UniversityFacade(settings=settings, policy=policy)

    print(f"\n{settings.university_name} - {settings.fiscal_year}")
    print("-" * 60)
    """
    Step 3 in the main.py file but actually needs to be implemented only after creating your University Facade.
    After we have created custom methods inside Facade class which invokes individual services, 
    we can actually use those methods here in main.py
    """
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

   #  print("\n=== Admission and Finance Report (via Facade convenience method) ===")
   #  report = university.get_admission_finance_report()
   #  print(f"University: {report['university']}")
   #  print(f"Admission: {report['admission_info']}")
   #  print(f"Finance: {report['finance_info']}")

if __name__ == "__main__":
    main()
