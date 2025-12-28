# Benefits of Facade Pattern

Simplified interface - Client only needs one object (university) instead of managing 4 separate services
Hides complexity - Client doesn't need to know which service needs settings vs policy
Single entry point - All university operations through one unified interface
Reduced coupling - Client code doesn't directly depend on individual service classes
Easier to use - No need to instantiate multiple services; Facade handles it internally
Convenience methods - High-level operations like get_complete_student_report() combine multiple services

# Limitation of Facade Pattern

Not OCP compliant - Adding new services requires modifying Facade's **init**
All services loaded - Even if client needs only one service, all 4 are initialized (overhead)
Tight coupling in Facade - Facade is tightly coupled to all 4 concrete service classes
Limited flexibility - Can't easily swap service implementations or use custom services
Single point of failure - If Facade breaks, all service access breaks
Potential over-simplification - May hide useful service features behind simplified methods
