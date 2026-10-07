"""Interface Segregation Principle: prefer small, client-specific contracts."""

from abc import ABC, abstractmethod


# Bad: every worker must provide lunch behavior, even when the worker is a
# robot. Implementations end up with meaningless methods or runtime errors.
class BadWorker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat_lunch(self):
        pass


class BadRobot(BadWorker):
    def work(self):
        print("Robot is assembling a product")

    def eat_lunch(self):
        raise NotImplementedError("A robot does not eat lunch")


# Good: clients depend only on the capability they need.
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Lunchable(ABC):
    @abstractmethod
    def eat_lunch(self):
        pass


class HumanWorker(Workable, Lunchable):
    def work(self):
        print("Human is assembling a product")

    def eat_lunch(self):
        print("Human is taking a lunch break")


class Robot(Workable):
    def work(self):
        print("Robot is assembling a product")


def assign_work(worker):
    """A production scheduler only needs the work capability."""
    worker.work()


if __name__ == "__main__":
    # In a factory scheduler, humans and robots can both receive work, while
    # only people participate in lunch scheduling.
    try:
        BadRobot().eat_lunch()
    except NotImplementedError as error:
        print(f"Bad interface: {error}")

    assign_work(HumanWorker())
    assign_work(Robot())
    HumanWorker().eat_lunch()
