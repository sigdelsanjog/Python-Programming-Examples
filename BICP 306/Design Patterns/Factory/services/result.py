from dataclasses import dataclass
from config import GradingPolicy


@dataclass
class ResultService:
    policy: GradingPolicy

    def generate(self, marks: float) -> str:
        return "Result: PASS" if self.policy.is_pass(marks) else "Result: FAIL"
