from dataclasses import dataclass
from config import GradingPolicy


@dataclass
class ResultService:
    policy: GradingPolicy

    def generate(self, marks: float) -> dict:
        percentage = self.policy.calculate_percentage(marks)
        is_pass = self.policy.is_pass(marks)
        
        return {
            "marks": marks,
            "percentage": percentage,
            "status": "PASS" if is_pass else "FAIL",
            "grade": self._calculate_grade(percentage)
        }

    def _calculate_grade(self, percentage: float) -> str:
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C+"
        elif percentage >= 40:
            return "C"
        else:
            return "F"
