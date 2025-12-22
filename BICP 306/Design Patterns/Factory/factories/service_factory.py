from typing import Dict, Callable

from config import UniversitySettings, GradingPolicy
from services.admission import AdmissionService
from services.finance import FinanceService
from services.exam import ExamService
from services.result import ResultService


class ServiceFactory:
    """Standalone factory for creating University services."""
    def __init__(
        self,
        settings: UniversitySettings | None = None,
        policy: GradingPolicy | None = None,
    ) -> None:
        self.settings = settings or UniversitySettings()
        self.policy = policy or GradingPolicy()

        self._registry: Dict[str, Callable[[], object]] = {
            "admission": lambda: AdmissionService(self.settings),
            "finance": lambda: FinanceService(self.settings),
            "exam": lambda: ExamService(self.policy),
            "result": lambda: ResultService(self.policy),
        }

    def create(self, service_type: str):
        key = service_type.strip().lower()
        try:
            return self._registry[key]()
        except KeyError:
            raise ValueError(
                f"Unknown service type: {service_type}. "
                f"Choose from {', '.join(self._registry.keys())}."
            )

    def available(self):
        return list(self._registry.keys())
