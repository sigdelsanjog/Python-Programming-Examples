"""
Facade Design Pattern: University Services Facade
You switched from main.py to university_facade.py to see the implementation of the Facade pattern.
This Facade class encapsulates the complexity of initializing and coordinating
multiple services, allowing clients to work with a single entry point.

How? The Facade class (UniversityFacade) initializes and manages multiple services:
- AdmissionService
- FinanceService
- ExamService
- ResultService

Clients interact with the UniversityFacade instead of dealing with each service individually.
Meaning, clients can call high-level methods on the Facade to perform complex operations
that involve multiple services, without needing to understand the details of those services.

Navigate to UniversityFacade class below to see the implementation.
Implementation is expalined in comments inside the class in step-by-step manner.
"""

"""
   Step 1: Import necessary configurations from config.py
   These configurations will be used to initialize the Facade and its services.

   Step 2: Import necessary services that the Facade will encapsulate.
   These services represent different subsystems of the university.
"""

from config import UniversitySettings, GradingPolicy
from services.admission import AdmissionService
from services.finance import FinanceService
from services.exam import ExamService
from services.result import ResultService


class UniversityFacade:
    """
    Step 3:  Define the Facade class that will encapsulate multiple services.
    Meaning, here we are creating a Facade class named UniversityFacade.
    This class will provide a simplified interface to interact with various university services like
    admission, finance, exam, and result processing.
    """
    def __init__(
        self,
        settings: UniversitySettings | None = None,
        policy: GradingPolicy | None = None,
    ) -> None:
        """Initialize the Facade with configuration and create all services."""
        self.settings = settings or UniversitySettings()
        self.policy = policy or GradingPolicy()

        """
        Step 4: Initialize all the services that the Facade will manage.
        Each service is initialized with the appropriate configuration.
        The Facade holds references to these services as private attributes.
        """ 
        self._admission_service = AdmissionService(self.settings)
        self._finance_service = FinanceService(self.settings)
        self._exam_service = ExamService(self.policy)
        self._result_service = ResultService(self.policy)

        """
        Step 5: Here each methods of the Facade class provides a simplified interface
        to interact with the underlying services.
        Clients can call these methods without needing to know the details of each service.
      """
    def show_admission_info(self) -> str:
        return self._admission_service.show_info()

    def show_finance_info(self) -> str:
        return self._finance_service.show_info()

    def evaluate_exam(self, marks: float) -> dict:
        return self._exam_service.evaluate(marks)

    def generate_result(self, marks: float) -> str:
        return self._result_service.generate(marks)

    def get_complete_student_report(self, marks: float) -> dict:
        """
        Step 6: This is another convenience method provided by the Facade. Meaning, it combines
        multiple service calls into a single method to generate a complete student report.
        Clients can call this method to get a comprehensive report without needing to call
        each service individually.
        """
        return {
            "university": self.settings.university_name,
            "admission_info": self.show_admission_info(),
            "finance_info": self.show_finance_info(),
            "exam_evaluation": self.evaluate_exam(marks),
            "result": self.generate_result(marks),
        }
    
   #  def get_admission_finance_report(self) -> dict:

   #    """Report with only admission and finance info"""
   #    return {
   #       "university": self.settings.university_name,
   #       "admission_info": self.show_admission_info(),
   #       "finance_info": self.show_finance_info(),
   #    }

"""
        Now lets move back to main.py to see how are these individual methods and convinience methods are 
         used by the client.
"""
