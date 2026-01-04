from abc import ABC, abstractmethod

# ISP compliant: smaller interfaces so clients depend only on what they use
class TranscriptService(ABC):
    @abstractmethod
    def request_transcript(self) -> None:
        ...


class FeePaymentService(ABC):
    @abstractmethod
    def pay_fees(self) -> None:
        ...

    def calculate_late_fee(self, days_late: int) -> float:
        return 0.0


class ResearchApprovalService(ABC):
    @abstractmethod
    def approve_research(self) -> None:
        ...


class StudentPortal(TranscriptService, FeePaymentService):
    def request_transcript(self) -> None:
        print("Transcript emailed to student")

    def pay_fees(self) -> None:
        print("Student fees processed")

    def calculate_late_fee(self, days_late: int) -> float:
        return max(0, days_late) * 5.0


class ResearchOffice(ResearchApprovalService):
    def approve_research(self) -> None:
        print("Research proposal approved by research office")


class Cashier(FeePaymentService):
    def pay_fees(self) -> None:
        print("Payment recorded by cashier")



def send_transcript(service: TranscriptService) -> None:
    service.request_transcript()


def collect_payment(service: FeePaymentService) -> None:
    service.pay_fees()

def calculate_late_fee(service: FeePaymentService, days_late: int) -> float:
    return service.calculate_late_fee(days_late)


def approve_project(service: ResearchApprovalService) -> None:
    service.approve_research()


def run_compliant() -> None:
    print("ISP compliant example:")
    student_portal = StudentPortal()
    research_office = ResearchOffice()
    cashier = Cashier()

    send_transcript(student_portal)
    collect_payment(student_portal)
    collect_payment(cashier)
    late_fee = calculate_late_fee(student_portal, days_late=3)
    print(f"Late fee (3 days): {late_fee}")
    approve_project(research_office)



if __name__ == "__main__":
    run_compliant()
