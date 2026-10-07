# SOLID Principles in Python

This repository is a practical introduction to five principles for designing
object-oriented software that is easier to change, test, and maintain. The
examples are intentionally small and use only the Python standard library.
Each example can be run directly with Python 3.

## The five principles

| Principle | Meaning | Example |
| --- | --- | --- |
| **S — Single Responsibility (SRP)** | A class should have one responsibility and one reason to change. | [1_single_responsibility.py](1_single_responsibility.py) |
| **O — Open/Closed (OCP)** | Software should allow new behavior through extension without repeated edits to stable code. | [2_open_closed.py](2_open_closed.py) |
| **L — Liskov Substitution (LSP)** | A subtype should be usable wherever its base type is expected without breaking behavior. | [3_liskov_substitution.py](3_liskov_substitution.py) |
| **I — Interface Segregation (ISP)** | Keep interfaces focused so clients only depend on operations they use. | [4_interface_segregation.py](4_interface_segregation.py) |
| **D — Dependency Inversion (DIP)** | High-level policy and low-level details should depend on abstractions, not on each other. | [5_dependency_inversion.py](5_dependency_inversion.py) |

## Getting started

Run an example from this directory:

```bash
python3 1_single_responsibility.py
```

Each file shows a problematic design, a more maintainable alternative, and a
small real-world scenario. The output is illustrative; the examples do not
connect to external services or require third-party packages.

For deeper explanations, benefits, and practical guidance, see
[PRINCIPLES.md](PRINCIPLES.md).
