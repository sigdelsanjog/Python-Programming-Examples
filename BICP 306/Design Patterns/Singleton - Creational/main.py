from services.admission_service import AdmissionService
from services.finance_service import FinanceService
from config.university_config import UniversityConfig

from services.exam_service import ExamService
from services.result_service import ResultService


def main():
    admission = AdmissionService()
    finance = FinanceService()

    print(admission.show_info())
    print(finance.show_info())

    # Proof of Singleton
    c1 = UniversityConfig()
    c2 = UniversityConfig()

    print("Same instance:", c1 is c2)

    exam = ExamService()
    result = ResultService()

    print(exam.evaluate(50))
    print(result.generate(50))


if __name__ == "__main__":
    main()
