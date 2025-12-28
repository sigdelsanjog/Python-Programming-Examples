from dataclasses import dataclass
from config import GradingPolicy


@dataclass
class ExamService:
    policy: GradingPolicy

    def evaluate(self, marks: float) -> dict:
        return {
            "percentage": self.policy.calculate_percentage(marks),
            "pass": self.policy.is_pass(marks),
        }
