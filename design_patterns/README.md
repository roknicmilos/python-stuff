# Design Patterns

Design patterns are reusable solutions to common problems that appear over and
over in software development. They aren’t code you copy–paste, but proven ways
of structuring logic, objects, and interactions so your system stays easier to
understand, maintain, and extend. They give developers a shared vocabulary
(“factory,” “observer,” “adapter,” etc.) and help guide good design without
dictating exact implementation.

## Architectural Patterns

Architectural patterns are high-level, structural blueprints that shape how an
entire system is organized. They define how major components interact, how data
flows, and how responsibilities are separated across the whole application.
Unlike design patterns, which solve smaller, localized problems, architectural
patterns guide the overall structure, scalability, and behaviour of the system
from the top down.

## Design Patterns vs Architectural Patterns

_Many patterns sit somewhere in the middle._

**Design Patterns** = patterns inside components (local structure)

* Solve localized problems
* At the class / object level
* Very reusable
* Found in the Gang of Four (GoF) book
* Examples: Singleton, Factory, Strategy, Observer, Decorator, Adapter, Builder,
  etc.
* These don't define how your app is structured, only how individual objects
  interact.

**Architectural Patterns** = patterns of the system as a whole (global
structure)

* Describe the overall structure of an app
* Define layers, modules, flows
* Influence deployment, responsibilities, system boundaries
* Examples: MVC, MVVM, MVP, Clean Architecture, Hexagonal Architecture,
  Monolith, Microservices, Event-driven architecture, etc.
* These patterns shape how your whole application is organized.
