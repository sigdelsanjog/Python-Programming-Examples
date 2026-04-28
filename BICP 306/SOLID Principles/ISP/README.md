# Interface Segregation Principle (ISP)

A client should not be forced to depend on methods it does not use.

## What this example shows

- **Violation**: `UniversityPortal` has unrelated responsibilities. `ResearchDepartment` and `FinanceOffice` must implement `request_transcript`, `pay_fees`, and `approve_research` even though each only needs one of them. Calling the unused methods leads to `NotImplementedError`.
- **Compliant**: Split into small interfaces (`TranscriptService`, `FeePaymentService`, `ResearchApprovalService`). Each client implements only what it needs, so no unused methods or placeholder exceptions.

Run the demos separately:

```bash
python "SOLID Principles/ISP/violation.py"
python "SOLID Principles/ISP/compliant.py"
```

Each script prints only the scenario it demonstrates, so you can compare the outputs side by side.
