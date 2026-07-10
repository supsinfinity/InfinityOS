# InfinityOS Design Decisions

This document records important architectural and implementation decisions made during development.

The purpose is to preserve the reasoning behind decisions so they are not unintentionally reversed in future revisions.

---

# Decision 1 — Use `Gtk.MenuButton` as the launcher anchor

**Status:** Accepted

## Decision

The Infinity button uses `Gtk.MenuButton`, which owns and displays a `Gtk.Popover`.

## Rationale

GTK already provides the behavior required for launcher menus.

Using the built-in widget provides:

* keyboard navigation
* accessibility support
* correct focus management
* automatic popover positioning
* native GTK behavior

Avoid reinventing behavior already provided by the toolkit.

---

# Decision 2 — Use GTK's built-in popover behavior

**Status:** Accepted

## Decision

Use `Gtk.MenuButton`'s built-in behavior instead of manually opening and closing popovers.

## Rationale

Manual state management increases complexity and duplicates functionality already implemented by GTK.

Prefer framework features over custom implementations whenever they satisfy project requirements.

---

# Decision 3 — Keep constructors focused on initialization

**Status:** Accepted

## Decision

`__init__()` methods should initialize object state only.

## Rationale

Constructors should avoid complex logic, lengthy computations, or application behavior.

Initialization should be predictable and easy to understand.

---

# Decision 4 — Adopt a service-oriented architecture

**Status:** Accepted

## Decision

Application logic belongs in services.

Components obtain information exclusively through services.

## Rationale

Services become the single source of truth for application state.

This separates business logic from the user interface and simplifies testing and maintenance.

---

# Decision 5 — Use an EventBus for communication

**Status:** Accepted

## Decision

Services communicate with components through the EventBus.

Components subscribe to events and refresh themselves.

## Rationale

Services should never manipulate GTK widgets directly.

An event-driven architecture keeps services independent from the presentation layer.

---

# Decision 6 — Isolate operating system access

**Status:** Accepted

## Decision

All operating system interactions belong inside the backend layer.

## Rationale

Services should not depend on desktop-specific APIs.

This improves portability and allows future support for multiple desktop environments.

---

# Decision 7 — Prefer composition over tightly coupled components

**Status:** Accepted

## Decision

Large interface sections should own smaller components rather than implementing all functionality themselves.

Example:

```text id="gq33s9"
StatusArea
├── WeatherComponent
├── CPUComponent
├── MemoryComponent
├── BatteryComponent
└── ClockComponent
```

## Rationale

Composition improves modularity and allows individual components to evolve independently.

---

# Decision 8 — One-way data flow

**Status:** Accepted

## Decision

Application data flows in one direction.

```text id="2yjlwm"
Operating System
        ↓
Backend
        ↓
Service
        ↓
EventBus
        ↓
Component
        ↓
Window
```

## Rationale

Each layer has a single responsibility.

Skipping layers increases coupling and makes debugging more difficult.

---

# Decision 9 — Architecture before features

**Status:** Accepted

## Decision

Prioritize building reusable architecture before implementing large numbers of features.

## Rationale

A stable foundation makes future features easier to implement and reduces the need for large refactors.

---

# Decision 10 — Keep modules replaceable

**Status:** Accepted

## Decision

Every major module should be replaceable with minimal changes elsewhere.

## Rationale

Loose coupling improves maintainability and supports future expansion, including new backends, services, or desktop environments.

---

# Decision 11 — Use explicit dependencies

**Status:** Accepted

## Decision

Dependencies should be passed explicitly rather than hidden behind global state or implicit lookups.

## Rationale

Explicit dependencies make the architecture easier to understand, debug, and test.

---

# Decision 12 — Refactor only when abstraction provides clear value

**Status:** Accepted

## Decision

Avoid introducing new abstractions unless they significantly reduce duplication or improve maintainability.

## Rationale

Additional classes, managers, or inheritance hierarchies should solve a real problem rather than exist for theoretical flexibility.

Simplicity is preferred over premature abstraction.

