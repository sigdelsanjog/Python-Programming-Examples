from services.grading_policy import GradingPolicy

class ResultService:
    def generate(self, marks):
        policy = GradingPolicy()
        if policy.is_pass(marks):
            return "Result: PASS"
        return "Result: FAIL"
