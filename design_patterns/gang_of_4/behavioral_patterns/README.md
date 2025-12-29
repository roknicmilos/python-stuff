# Behavioral Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of
responsibilities between objects. They describe patterns of communication
between objects.

---

## Observer Design Pattern

**What It Is**: A behavioral pattern that defines a one-to-many dependency
between objects, where when one object (the subject) changes state, all
dependent objects (observers) are automatically notified and updated.

**Purpose**: Solves the problem of keeping multiple objects synchronized without
tight coupling. It lets objects subscribe to events happening in another object
without the subject needing to know concrete observer implementations.

**Benefits**:

* Promotes loose coupling between subjects and observers.
* Supports dynamic subscription — observers can be added or removed at runtime.
* Enables broadcast communication: one change notifies many observers.
* Follows the Open/Closed Principle — add new observers without modifying the
  subject.
* Simplifies event-driven and reactive architectures where UI or other systems
  update automatically when data changes.

**Common Use Cases You've Seen**: Django signals (post_save, pre_delete), event
listeners in JavaScript, pub/sub messaging systems, real-time notifications, and
reactive frameworks where UI updates automatically when underlying data changes.

[Example in Python](examples/observer.py)
