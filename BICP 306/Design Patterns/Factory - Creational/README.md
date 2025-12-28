# Singleton vs Factory Pattern: University Services

This project demonstrates two fundamental design patterns using a University Management System as the business case.

## Pattern Overview

### **Singleton Pattern** (`../Singleton/`)

Ensures **exactly one instance** of a class exists globally and provides a single access point.

### **Factory Pattern** (`./`)

Centralizes **object creation logic** and encapsulates how objects are instantiated and configured.

---

## Key Differences

### **1. Instantiation & Instance Management**

#### Singleton Approach

```python
# Config controls its own creation (self-managing)
class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.university_name = "Kathmandu University"
            cls._instance.fiscal_year = "2025/26"
        return cls._instance

# Usage: direct instantiation returns the same instance
c1 = UniversityConfig()
c2 = UniversityConfig()
print(c1 is c2)  # True - SAME instance (singleton guarantee)
```

**Characteristic**: One global instance shared everywhere.

#### Factory Approach

```python
# Factory controls creation logic (centralized)
class ServiceFactory:
    def __init__(self, settings=None, policy=None):
        self.settings = settings or UniversitySettings()
        self.policy = policy or GradingPolicy()

        self._registry = {
            "admission": lambda: AdmissionService(self.settings),
            "exam": lambda: ExamService(self.policy),
        }

    def create(self, service_type):
        return self._registry[service_type]()

# Usage: factory creates new instances on demand
factory = ServiceFactory()
admission = factory.create("admission")  # NEW instance
exam = factory.create("exam")            # NEW instance
```

**Characteristic**: Creates multiple instances, each properly configured.

---

### **2. Dependency Management**

#### Singleton: Tight Coupling

```python
# Services fetch their own dependencies (tightly coupled)
class AdmissionService:
    def show_info(self):
        config = UniversityConfig()  # ← Service instantiates its own dependency
        return f"Admissions at {config.university_name}"

class ExamService:
    def evaluate(self, marks):
        policy = GradingPolicy()  # ← Service instantiates its own dependency
        return {"percentage": policy.calculate_percentage(marks)}
```

**Issues**:

- Services hardcoded to specific classes
- Difficult to test (can't inject mocks)
- Changes to config propagate through all services

#### Factory: Loose Coupling (Dependency Injection)

```python
# Services receive dependencies via constructor (decoupled)
@dataclass
class AdmissionService:
    settings: UniversitySettings  # ← Dependency injected

    def show_info(self) -> str:
        return f"Admissions at {self.settings.university_name}"

@dataclass
class ExamService:
    policy: GradingPolicy  # ← Dependency injected

    def evaluate(self, marks: float) -> dict:
        return {"percentage": self.policy.calculate_percentage(marks)}

# Factory wires dependencies automatically
factory = ServiceFactory(settings=settings, policy=policy)
admission = factory.create("admission")  # settings injected
exam = factory.create("exam")            # policy injected
```

**Benefits**:

- Services don't know where dependencies come from
- Easy to test with mock objects
- Flexible configuration management

---

### **3. Configuration Structure**

#### Singleton: Hardcoded & Self-Contained

```python
class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.university_name = "Kathmandu University"  # hardcoded
            cls._instance.fiscal_year = "2025/26"
            cls._instance.pass_mark = 40
            cls._instance.max_mark = 100
        return cls._instance
```

**Problems**:

- Configuration embedded in class definition
- Cannot change values without modifying source code
- Singleton pattern logic mixed with business logic

#### Factory: Flexible & Data-Driven

```python
# Config is pure data (simple dataclass)
@dataclass(frozen=True)
class UniversitySettings:
    university_name: str = "Kathmandu University"
    fiscal_year: str = "2025/26"

@dataclass(frozen=True)
class GradingPolicy:
    pass_mark: int = 40
    max_mark: int = 100

    def calculate_percentage(self, marks: float) -> float:
        return (marks / self.max_mark) * 100

# Usage: easy to customize
custom_settings = UniversitySettings(
    university_name="Tribhuvan University",
    fiscal_year="2024/25"
)
factory = ServiceFactory(settings=custom_settings)

# Can load from environment or config files
from os import getenv
settings = UniversitySettings(
    university_name=getenv("UNIVERSITY_NAME", "Kathmandu University"),
    fiscal_year=getenv("FISCAL_YEAR", "2025/26")
)
```

**Benefits**:

- Configuration is easy to override
- Can load from environment variables, JSON, databases
- Configuration logic separate from creation logic

---

### **4. Main Usage Pattern**

#### Singleton Approach

```python
# Direct instantiation - tight coupling
def main():
    admission = AdmissionService()      # ← Must import concrete class
    finance = FinanceService()          # ← Class names hardcoded
    exam = ExamService()                # ← Difficult to swap implementations
    result = ResultService()

    # Services internally fetch shared singleton config
    print(admission.show_info())
    print(exam.evaluate(50))

if __name__ == "__main__":
    main()
```

**Code in**: `Design Patterns/Singleton/main.py`

#### Factory Approach

```python
# Factory-mediated instantiation - loose coupling
def demo():
    settings = UniversitySettings()
    policy = GradingPolicy()
    factory = ServiceFactory(settings=settings, policy=policy)

    admission = factory.create("admission")  # ← Factory decides what to create
    finance = factory.create("finance")      # ← Don't need to import service classes
    exam = factory.create("exam")            # ← Easy to swap by changing registry
    result = factory.create("result")

    print(f"{settings.university_name} - {settings.fiscal_year}")
    print(admission.show_info())
    print(exam.evaluate(50))

if __name__ == "__main__":
    demo()
```

**Code in**: `Design Patterns/Factory/main.py`

---

## Comparison Table

| Aspect             | **Singleton**                  | **Factory**                  |
| ------------------ | ------------------------------ | ---------------------------- |
| **Instances**      | Exactly 1, globally            | Many, created on demand      |
| **Control**        | Class controls itself          | External factory controls    |
| **Dependencies**   | Services fetch own             | Factory injects              |
| **Coupling**       | Tight (knows concrete classes) | Loose (knows only keys)      |
| **Configuration**  | Hardcoded in class             | Separate, configurable data  |
| **Testability**    | Hard (can't mock)              | Easy (inject test mocks)     |
| **Flexibility**    | Low (fixed at build time)      | High (changeable at runtime) |
| **Use Case**       | Shared immutable state         | Object creation variants     |
| **Adding Service** | Modify both class & callers    | Only update factory registry |

---

## Similarities

Both patterns manage object lifecycles and ensure consistency:

- Centralize object creation logic
- Avoid scattered instantiation across codebase
- Ensure consistent configuration throughout the app

---

## When to Use What

### Use **Singleton** when:

- You need exactly one instance (e.g., database connection, logger)
- State is immutable and truly global
- Access must be available everywhere
- Example: `UniversityConfig` in the Singleton demo

### Use **Factory** when:

- You need to create multiple instances with consistent wiring
- Object creation logic is complex
- You want loose coupling and easy testing
- You may have multiple implementations of the same interface
- Example: Creating different service types (admission, finance, exam, result)

---

## Running the Examples

### Singleton Pattern

```bash
cd ../Singleton
python3 main.py
```

Output:

```
Admissions at Kathmandu University
Finance Dept - Fiscal Year 2025/26
Same instance: True
{'percentage': 50.0, 'pass': True}
Result: PASS
```

### Factory Pattern

```bash
cd ./
python3 main.py
```

Output:

```
Kathmandu University - 2025/26

=== Services ===
Admissions at Kathmandu University
Finance Dept - Fiscal Year 2025/26

=== Exam & Result ===
Evaluation: {'percentage': 50.0, 'pass': True}
Final: Result: PASS
```

---

## Project Structure

```
Design Patterns/
├── Singleton/
│   ├── main.py
│   ├── config/
│   │   └── university_config.py
│   └── services/
│       ├── admission_service.py
│       ├── finance_service.py
│       ├── exam_service.py
│       ├── result_service.py
│       └── grading_policy.py
└── Factory/
    ├── main.py
    ├── config.py
    ├── factories/
    │   └── service_factory.py
    └── services/
        ├── admission.py
        ├── finance.py
        ├── exam.py
        └── result.py
```

---

## Key Takeaways

| Pattern       | Philosophy                                                               |
| ------------- | ------------------------------------------------------------------------ |
| **Singleton** | "There's only one version of this resource — access it directly"         |
| **Factory**   | "Create objects with consistent wiring — ask me, not the class directly" |

**Best Practice**: Use Factory to manage service creation and wiring, and optionally use Singleton within services for true globally-shared resources (like database connections).
