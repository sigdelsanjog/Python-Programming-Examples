from dataclasses import dataclass
from config import UniversitySettings


@dataclass
class AdmissionService:
    settings: UniversitySettings

    def show_info(self) -> str:
        return f"Admissions at {self.settings.university_name}"
