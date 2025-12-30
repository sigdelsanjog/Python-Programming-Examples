from grading_strategies import GradingStrategy


class UniversityGradingSystem:
    def __init__(self, strategy: GradingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: GradingStrategy):
        self._strategy = strategy
        print(f"Strategy changed to: {self._strategy.get_strategy_name()}")

    def grade_student(self, marks: float, max_marks: int = 100) -> dict:
        return self._strategy.calculate_grade(marks, max_marks)

    def get_current_strategy(self) -> str:
        """Return the name of the current strategy"""
        return self._strategy.get_strategy_name()

    def batch_grade_students(self, student_marks: list) -> list:
        results = []
        for student_name, marks in student_marks:
            grade_result = self.grade_student(marks)
            grade_result["student"] = student_name
            results.append(grade_result)
        return results
