# Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions.

## What this example shows

- **Violation**: `UniversityReportGenerator` creates a `StudentDatabase` directly, so it is locked to one data source and is hard to test.
- **Compliant**: `UniversityReportGenerator` depends on `StudentDataSource` (an abstraction) and receives a concrete implementation via constructor injection.

Run the demos separately:

```bash
python "SOLID Principles/DIP/violation.py"
python "SOLID Principles/DIP/compliant.py"
```

Compare the outputs to see how swapping data sources becomes easy in the compliant version.
