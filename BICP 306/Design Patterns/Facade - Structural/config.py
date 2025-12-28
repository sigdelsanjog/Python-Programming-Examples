from dataclasses import dataclass


@dataclass(frozen=True)
class UniversitySettings:
    university_name: str = "Kathmandu University"
    fiscal_year: str = "2025/26"


@dataclass(frozen=True)
class GradingPolicy:
    pass_mark: int = 40
    max_mark: int = 100

    def calculate_percentage(self, marks: float) -> float:
        return (marks / self.max_mark) * 100

    def is_pass(self, marks: float) -> bool:
        return marks >= self.pass_mark
