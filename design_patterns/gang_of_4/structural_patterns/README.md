# Structural Design Patterns

Structural design patterns focus on how classes and objects are composed to form
larger structures. They help ensure that if one part of a system changes, the
entire structure doesn't need to change.

## Adopter Design Pattern

**What It Is**: A structural pattern that allows incompatible interfaces to work
together by wrapping an object with a new interface that translates between the
expected interface and the actual implementation.

**Purpose**: Solves the problem of integrating classes or systems that have
incompatible interfaces. Acts as a translator or converter, allowing you to use
existing code with new systems without modifying the original code.

**Benefits**:

* Enables integration of incompatible interfaces without modifying existing
  code.
* Promotes code reuse by adapting existing classes to new contexts.
* Supports the Single Responsibility Principle by separating interface
  conversion from business logic.
* Makes legacy code work with modern systems with minimal changes.
* Allows swapping implementations easily by changing the adapter rather than
  client code.
* Keeps client code clean and independent of specific implementations.

**Common Use Cases You've Seen**: Django's database backends (adapting different
databases to the ORM interface), payment gateway wrappers (adapting
Stripe/PayPal to your payment interface), and API client libraries that wrap
third-party APIs with a cleaner interface.

[Example in Python](examples/adopter.py)
