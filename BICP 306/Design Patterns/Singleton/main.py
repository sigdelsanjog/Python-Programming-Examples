from services.admission_service import AdmissionService
from services.finance_service import FinanceService
from config.university_config import UniversityConfig

def main():
    admission = AdmissionService()
    finance = FinanceService()

    print(admission.show_info())
    print(finance.show_info())

    # Proof of Singleton
    c1 = UniversityConfig()
    c2 = UniversityConfig()

    print("Same instance:", c1 is c2)


if __name__ == "__main__":
    main()
