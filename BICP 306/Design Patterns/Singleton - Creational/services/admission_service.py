from config.university_config import UniversityConfig

class AdmissionService:
    def show_info(self):
        config = UniversityConfig()
        return f"Admissions at {config.university_name}"
