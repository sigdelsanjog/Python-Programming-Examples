"""
Facade Design Pattern: University Services Facade

The Facade provides a unified, simplified interface to a complex subsystem
of University services (Admission, Finance, Exam, Result). Clients interact
with a single Facade object instead of directly managing multiple services.
"""

from config import UniversitySettings, GradingPolicy
from services.admission import AdmissionService
from services.finance import FinanceService
from services.exam import ExamService
from services.result import ResultService


class UniversityFacade:
    """
    Facade that provides a simplified interface to all University services.
    
    This class encapsulates the complexity of initializing and coordinating
    multiple services, allowing clients to work with a single entry point.
    """

    def __init__(
        self,
        settings: UniversitySettings | None = None,
        policy: GradingPolicy | None = None,
    ) -> None:
        """Initialize the Facade with configuration and create all services."""
        self.settings = settings or UniversitySettings()
        self.policy = policy or GradingPolicy()

        # Initialize all subsystem services
        self._admission_service = AdmissionService(self.settings)
        self._finance_service = FinanceService(self.settings)
        self._exam_service = ExamService(self.policy)
        self._result_service = ResultService(self.policy)

    def show_admission_info(self) -> str:
        """Get admission department information."""
        return self._admission_service.show_info()

    def show_finance_info(self) -> str:
        """Get finance department information."""
        return self._finance_service.show_info()

    def evaluate_exam(self, marks: float) -> dict:
        """Evaluate exam marks and return percentage and pass status."""
        return self._exam_service.evaluate(marks)

    def generate_result(self, marks: float) -> str:
        """Generate final result based on marks."""
        return self._result_service.generate(marks)

    def get_complete_student_report(self, marks: float) -> dict:
        """
        Convenience method: Get a complete student report with all information.
        This demonstrates the Facade's ability to provide high-level operations.
        """
        return {
            "university": self.settings.university_name,
            "admission_info": self.show_admission_info(),
            "finance_info": self.show_finance_info(),
            "exam_evaluation": self.evaluate_exam(marks),
            "result": self.generate_result(marks),
        }
