from abc import ABC, abstractmethod

# ISP violation: bulky interface forces clients to depend on unused methods
class UniversityPortal(ABC):
    @abstractmethod
    def request_transcript(self) -> None:
        ...

    @abstractmethod
    def pay_fees(self) -> None:
        ...

    @abstractmethod
    def approve_research(self) -> None:
        ...


class ResearchDepartment(UniversityPortal):
    def request_transcript(self) -> None:
        raise NotImplementedError("Research office does not handle transcripts")

    def pay_fees(self) -> None:
        raise NotImplementedError("Research office does not take payments")

    def approve_research(self) -> None:
        print("Research proposal approved by research office")


class FinanceOffice(UniversityPortal):
    def request_transcript(self) -> None:
        raise NotImplementedError("Finance office does not handle transcripts")

    def pay_fees(self) -> None:
        print("Fees paid at finance office")

    def approve_research(self) -> None:
        raise NotImplementedError("Finance office cannot approve research")


def run_violation() -> None:
    print("ISP violation example:")
    portals: list[UniversityPortal] = [ResearchDepartment(), FinanceOffice()]
    for portal in portals:
        try:
            portal.pay_fees()
        except NotImplementedError as exc:
            print(f"  {portal.__class__.__name__} broke: {exc}")


if __name__ == "__main__":
    run_violation()
