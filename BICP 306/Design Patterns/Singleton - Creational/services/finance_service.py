from config.university_config import UniversityConfig

class FinanceService:
    def show_info(self):
        config = UniversityConfig()
        return f"Finance Dept - Fiscal Year {config.fiscal_year}"
