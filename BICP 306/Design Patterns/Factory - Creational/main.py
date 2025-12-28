from factories.service_factory import ServiceFactory
from config import UniversitySettings, GradingPolicy


def demo():
    # Use defaults from config.py; override via args/env if needed
    settings = UniversitySettings()
    policy = GradingPolicy()

    factory = ServiceFactory(settings=settings, policy=policy)

    # Create services via Factory
    admission = factory.create("admission")
    finance = factory.create("finance")
    exam = factory.create("exam")
    result = factory.create("result")

    print(f"{settings.university_name} - {settings.fiscal_year} \n")
    print("=== Services ===")
    print(admission.show_info())
    print(finance.show_info())

    print("\n=== Exam & Result ===")
    marks = 50
    print("Evaluation:", exam.evaluate(marks))
    print("Final:", result.generate(marks))


if __name__ == "__main__":
    demo()
