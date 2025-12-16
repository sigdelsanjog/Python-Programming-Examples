from abc import ABC, abstractmethod

class UniversityRole(ABC):

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def perform_duty(self):
        pass

    @abstractmethod
    def calculate_pay(self):
        pass


class Teacher(UniversityRole):
    def get_details(self):
        return "Role: Teacher, Dept: Computer Science"

    def perform_duty(self):
        return "Teaching AI course."

    def calculate_pay(self):
        return 60000  # monthly


class AdminStaff(UniversityRole):
    def get_details(self):
        return "Role: Admin Staff, Dept: Exam Section"

    def perform_duty(self):
        return "Managing exam schedules."

    def calculate_pay(self):
        return 45000


class UniversitySystem:
    def __init__(self, role: UniversityRole):
        self.role = role

    def show_role_info(self):
        print(self.role.get_details())
        print(self.role.perform_duty())
        print("Pay:", self.role.calculate_pay())


def main():
    # Create a Teacher instance
    teacher = Teacher()
    
    # Pass it to UniversitySystem
    system = UniversitySystem(AdminStaff())
    system.perform_duty()
    # Execute all methods
    system.show_role_info()

    print("\n---\n")


if __name__ == "__main__":
    main()
