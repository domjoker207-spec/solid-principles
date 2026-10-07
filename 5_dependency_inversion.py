"""Dependency Inversion Principle: inject details behind an abstraction."""

from abc import ABC, abstractmethod


# Bad: report policy constructs a concrete database client, making the
# high-level report difficult to test or reuse with another storage system.
class MySQLDatabase:
    def save(self, report):
        print(f"Saving {report!r} to MySQL")


class BadReportService:
    def __init__(self):
        self.database = MySQLDatabase()

    def publish(self, report):
        self.database.save(report)


# Good: both the high-level service and storage implementations use this
# abstraction. The application supplies the adapter it needs.
class ReportRepository(ABC):
    @abstractmethod
    def save(self, report):
        """Persist a report."""


class MySQLReportRepository(ReportRepository):
    def save(self, report):
        print(f"Saving {report!r} to MySQL")


class MemoryReportRepository(ReportRepository):
    """A lightweight adapter useful for tests and local examples."""

    def __init__(self):
        self.reports = []

    def save(self, report):
        self.reports.append(report)


class ReportService:
    def __init__(self, repository):
        self.repository = repository

    def publish(self, report):
        self.repository.save(report)


if __name__ == "__main__":
    # A reporting application can swap storage adapters without changing
    # the business operation that publishes a report.
    BadReportService().publish("Quarterly sales")

    test_repository = MemoryReportRepository()
    ReportService(test_repository).publish("Quarterly sales")
    print(f"Stored by injected adapter: {test_repository.reports}")

    production_service = ReportService(MySQLReportRepository())
    production_service.publish("Quarterly sales")
