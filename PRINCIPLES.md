# A Practical Guide to SOLID

SOLID is a set of design principles for object-oriented software. They are
guidelines rather than rigid rules: apply them when they make code easier to
change, understand, or test, and avoid adding abstractions that do not solve a
real problem.

## S — Single Responsibility Principle

**A class should have one reason to change.** A responsibility is a cohesive
reason for the class to change, not necessarily a single method or a tiny
class.

`1_single_responsibility.py` contrasts an order class that calculates prices,
saves data, and sends email with an order model, repository, and receipt
sender that each handle a distinct concern.

**Benefits**

- Changes to persistence or email do not risk changing order calculations.
- Individual responsibilities can be tested and reused independently.
- Classes and modules are easier to explain and maintain.

**Best practices**

- Group behavior that changes for the same reason.
- Separate business rules from infrastructure concerns such as databases,
  files, and messaging.
- Avoid splitting code into many tiny classes when the responsibilities are
  not actually independent.

**Real-world use:** In an e-commerce checkout, pricing rules, order storage,
and receipt delivery commonly change for different business or technical
reasons.

## O — Open/Closed Principle

**Software entities should be open for extension but closed for modification.**
New variations should be added through a stable extension point rather than
by repeatedly editing established decision-making code.

`2_open_closed.py` first uses a conditional that must be modified for every
discount type, then uses a discount contract and separate policy classes.

**Benefits**

- New behavior is less likely to break existing behavior.
- Extensions can be tested without changing a central conditional.
- Stable parts of a system need fewer risky edits.

**Best practices**

- Use a clear abstraction, strategy, or event hook where variation is likely.
- Prefer simple conditionals when the behavior is small and unlikely to grow;
  do not design speculative extension frameworks.
- Keep each extension's contract narrow and understandable.

**Real-world use:** An online shop can add seasonal promotions alongside
member pricing without modifying its checkout total calculation.

## L — Liskov Substitution Principle

**A subtype should be usable wherever its base type is expected without
changing the correctness of the program.** Subtypes must honor the promises,
preconditions, postconditions, and invariants of their base abstractions.

`3_liskov_substitution.py` demonstrates why a mutable square is not a safe
substitute for a rectangle when callers expect width and height to change
independently. The improved model gives each shape the behavior it can
honestly provide: calculating its area.

**Benefits**

- Polymorphic code behaves predictably for every implementation.
- Shared abstractions become reliable contracts instead of misleading names.
- Callers need fewer type checks and special cases.

**Best practices**

- Model contracts around behavior that all implementations can preserve.
- Do not override a method in a way that surprises callers or weakens its
  guarantees.
- Test implementations against the expectations of their base contract.

**Real-world use:** A graphics renderer can calculate areas for different
shapes through a common shape contract without assuming every shape has
rectangle-style dimensions.

## I — Interface Segregation Principle

**Clients should not be forced to depend on methods they do not use.** Several
focused interfaces are usually more useful than one broad interface.

`4_interface_segregation.py` shows a worker contract that makes a robot
implement an irrelevant lunch method, then separates work and lunch
capabilities.

**Benefits**

- Implementations contain fewer empty, unsupported, or exception-raising
  methods.
- A change to an unrelated capability is less likely to affect a client.
- Each contract is easier to understand and implement.

**Best practices**

- Define interfaces from the needs of their clients.
- Split contracts when distinct clients use distinct subsets of operations.
- Combine small interfaces when a real client needs both capabilities.

**Real-world use:** A factory scheduler may assign work to both humans and
robots, while lunch scheduling applies only to human workers.

## D — Dependency Inversion Principle

**High-level modules should not depend on low-level modules; both should
depend on abstractions. Abstractions should not depend on details; details
should depend on abstractions.**

`5_dependency_inversion.py` contrasts a report service that constructs a
concrete database client with a service that receives a repository contract
and can use different adapters.

**Benefits**

- Business policy is less coupled to databases and other infrastructure.
- Test doubles can replace external systems in focused tests.
- Implementations can be replaced without rewriting high-level behavior.

**Best practices**

- Put abstractions at boundaries where high-level policy needs a detail.
- Supply concrete implementations through constructors or a composition
  root.
- Keep abstractions based on meaningful application needs; avoid interfaces
  that merely mirror every concrete class.

**Real-world use:** A reporting service can use a database repository in
production and an in-memory repository in tests while keeping its publishing
workflow unchanged.

## How the principles work together

These principles reinforce one another. Focused responsibilities and
interfaces help keep abstractions small; abstractions make safe extension and
dependency injection practical; and substitutable implementations keep those
abstractions trustworthy. The goal is not to maximize the number of classes,
but to make likely changes local and low-risk.
