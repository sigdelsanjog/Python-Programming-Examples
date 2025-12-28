class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.university_name = "Kathmandu University"
            cls._instance.fiscal_year = "2025/26"
            cls._instance.pass_mark = 40
            cls._instance.max_mark = 100
        return cls._instance
