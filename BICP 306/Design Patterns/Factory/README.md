# Factory Pattern for University Services

This implements a simple Factory to create service objects that internally rely on the Singleton configuration and grading policy already defined in `Singleton/`.

## Structure

- `factories/service_factory.py`: Creates `AdmissionService`, `FinanceService`, `ExamService`, `ResultService`.
- `main.py`: Demo script to show factory usage.

## Run

From the `Design Patterns/Factory` directory:

```bash
python3 main.py
```

The script prints information using the shared `UniversityConfig` singleton and evaluates sample marks via `GradingPolicy` singleton.
