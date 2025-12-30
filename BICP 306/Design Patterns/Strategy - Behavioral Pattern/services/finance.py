from dataclasses import dataclass
from config import UniversitySettings


@dataclass
class FinanceService:
    settings: UniversitySettings

    def show_info(self) -> str:
        return f"Finance Dept - Fiscal Year {self.settings.fiscal_year}"
