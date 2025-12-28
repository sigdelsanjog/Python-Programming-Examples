from services.grading_policy import GradingPolicy

class ExamService:
    def evaluate(self, marks):
        policy = GradingPolicy()
        return {
            "percentage": policy.calculate_percentage(marks),
            "pass": policy.is_pass(marks)
        }
