# Dependency Inversion Principle (violation)
# High-level module depends on concrete low-level modules.

class StudentDatabase:
    def fetch_students(self) -> list[dict[str, str | int]]:
        print("Connecting directly to SQL...")
        return [
            {"name": "Bidhan", "marks": 85},
            {"name": "Luniva", "marks": 92},
            {"name": "Sajina", "marks": 78},
        ]


class UniversityReportGenerator:
    def __init__(self):
        self.db = StudentDatabase()  # hard dependency on concrete class

    def build_report(self) -> list[str]:
        students = self.db.fetch_students()
        return [f"Student: {s['name']}, Marks: {s['marks']}" for s in students]


def run_violation() -> None:
    print("DIP violation example:")
    report = UniversityReportGenerator().build_report()
    for line in report:
        print("  ", line)


if __name__ == "__main__":
    run_violation()
