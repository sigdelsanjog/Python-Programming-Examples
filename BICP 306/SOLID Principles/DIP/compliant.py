from abc import ABC, abstractmethod

# Dependency Inversion Principle (compliant)
# High-level module depends on abstraction, and implementations are injected.

class StudentDataSource(ABC):
    @abstractmethod
    def fetch_students(self) -> list[dict[str, str | int]]:
        ...


class SQLStudentDataSource(StudentDataSource):
    def fetch_students(self) -> list[dict[str, str | int]]:
        print("Fetching students from SQL")
        return [
            {"name": "Alice", "marks": 88},
            {"name": "Bob", "marks": 91},
            {"name": "Charlie", "marks": 79},
        ]


class APIStudentDataSource(StudentDataSource):
    def fetch_students(self) -> list[dict[str, str | int]]:
        print("Fetching students from API")
        return [
            {"name": "Daisy", "marks": 95},
            {"name": "Ethan", "marks": 82},
        ]


class UniversityReportGenerator:
    def __init__(self, data_source: StudentDataSource):
        self.data_source = data_source

    def build_report(self) -> list[str]:
        students = self.data_source.fetch_students()
        return [f"Student: {s['name']}, Marks: {s['marks']}" for s in students]


def run_compliant() -> None:
    print("DIP compliant example:")
    print("\n--- SQL Data Source ---")
    sql_report = UniversityReportGenerator(SQLStudentDataSource()).build_report()
    for line in sql_report:
        print("  ", line)
        
    print("\n--- API Data Source ---")
    api_report = UniversityReportGenerator(APIStudentDataSource()).build_report()
    for line in api_report:
        print("  ", line)


if __name__ == "__main__":
    run_compliant()
