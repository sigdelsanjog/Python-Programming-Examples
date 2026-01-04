from abc import ABC, abstractmethod


class GradingStrategy(ABC):
    @abstractmethod
    def calculate_grade(self, marks: float, max_marks: int = 100) -> dict:
        """Calculate the grade based on marks and return a dictionary of results"""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the grading strategy"""
        pass

class PercentageGradingStrategy(GradingStrategy):
    def calculate_grade(self, marks: float, max_marks: int = 100) -> dict:
        percentage = (marks / max_marks) * 100
        
        # Determine division based on percentage
        if percentage >= 75:
            division = "Distinction"
        elif percentage >= 60:
            division = "First Division"
        elif percentage >= 45:
            division = "Second Division"
        elif percentage >= 35:
            division = "Third Division"
        else:
            division = "Fail"
        
        return {
            "marks": marks,
            "max_marks": max_marks,
            "percentage": round(percentage, 2),
            "division": division,
            "strategy": self.get_strategy_name()
        }

    def get_strategy_name(self) -> str:
        return "Percentage-Based Grading"


class GPAGradingStrategy(GradingStrategy):
    def calculate_grade(self, marks: float, max_marks: int = 100) -> dict:
        if marks >= 90:
            gpa = 4.0
            grade = "A"
        elif marks >= 85:
            gpa = 3.7
            grade = "A-"
        elif marks >= 80:
            gpa = 3.3
            grade = "B+"
        elif marks >= 75:
            gpa = 3.0
            grade = "B"
        elif marks >= 70:
            gpa = 2.7
            grade = "B-"
        elif marks >= 65:
            gpa = 2.3
            grade = "C+"
        elif marks >= 60:
            gpa = 2.0
            grade = "C"
        elif marks >= 55:
            gpa = 1.7
            grade = "C-"
        elif marks >= 50:
            gpa = 1.0
            grade = "D"
        else:
            gpa = 0.0
            grade = "F"
        
        return {
            "marks": marks,
            "max_marks": max_marks,
            "gpa": gpa,
            "grade": grade,
            "strategy": self.get_strategy_name()
        }

    def get_strategy_name(self) -> str:
        return "GPA-Based Grading"
