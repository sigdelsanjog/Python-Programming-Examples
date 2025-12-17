from config.university_config import UniversityConfig

class GradingPolicy:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = UniversityConfig()
        return cls._instance

    def calculate_percentage(self, marks):
        return (marks / self.config.max_mark) * 100

    def is_pass(self, marks):
        return marks >= self.config.pass_mark
