# InfinityOS Architecture

## Overview

InfinityOS is a modular, service-oriented desktop platform built around a small set of core architectural principles.

Every subsystem has a single responsibility and communicates through well-defined interfaces. This keeps the codebase maintainable, testable, and independent of any specific desktop environment.

---

# Core Architecture

```
                InfinityCore
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     EventBus   ServiceManager   Application
                      │
        ┌─────────────┴─────────────┐
        │                           │
 WeatherService              SystemService
        │                           │
 Weather Backend             SystemBackend
        │                           │
     Operating System / APIs
```

User interface components never access the operating system directly.

Instead, all data flows through the service layer.

```
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

---

# Principles

## Principle 1 — Separation of Responsibilities

Each layer has one responsibility.

* Core manages application infrastructure.
* Services provide application logic.
* Backends communicate with the operating system.
* Components display information.
* Windows arrange components.

No layer should assume another layer's responsibilities.

---

## Principle 2 — Service-Oriented Design

Components never communicate directly with each other.

All shared state and application logic belongs inside services.

Services act as the single source of truth.

---

## Principle 3 — Event-Driven Communication

Services never update widgets directly.

Instead, services publish events through the EventBus.

Components subscribe to the events they care about and refresh themselves.

This keeps services completely independent from the user interface.

---

## Principle 4 — Desktop Independence

Application logic should not depend on GNOME, KDE, Hyprland, or any other desktop environment.

Desktop-specific implementation belongs inside the backend layer.

This allows InfinityOS to support multiple desktop environments without changing application logic.

---

## Principle 5 — Replaceable Modules

Every module should be replaceable without requiring changes elsewhere.

Examples:

* Replace the weather provider.
* Replace the system backend.
* Replace a UI component.
* Replace a service implementation.

If replacing a module requires widespread changes, the architecture should be reconsidered.

---

## Principle 6 — Single Responsibility

Every class should have one clear purpose.

Examples:

* WeatherService manages weather data.
* SystemBackend retrieves operating system information.
* CPUComponent displays CPU usage.
* StatusArea arranges right-side widgets.

---

## Principle 7 — Explicit Dependencies

Objects should receive their dependencies instead of creating unnecessary hidden dependencies.

The dependency graph should remain simple and easy to understand.

---

# Layer Responsibilities

## Core

Responsible for application infrastructure.

Owns:

* EventBus
* ServiceManager
* Application lifecycle

Core contains no GTK code.

---

## Services

Services contain business logic.

Responsibilities include:

* Managing application state
* Caching backend data
* Publishing events
* Providing data to components

Services never manipulate GTK widgets.

---

## Backends

Backends communicate directly with the operating system.

Responsibilities include:

* Reading system information
* Accessing desktop APIs
* Platform-specific integration

Backends never know about services or components.

---

## Components

Components display information.

Responsibilities include:

* Creating GTK widgets
* Reading data from services
* Responding to events
* Updating the interface

Components never communicate directly with the operating system.

---

## Window

The window owns layout.

Responsibilities include:

* Positioning components
* Creating containers
* Managing visual hierarchy

Windows should contain no application logic.

---

# Data Flow

InfinityOS follows a one-way flow of information.

```
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

Data should never skip layers.

---

# Design Philosophy

InfinityOS prioritizes architecture over features.

Every new feature should integrate naturally into the existing architecture instead of introducing special-case code.

The goal is to build a desktop platform that remains understandable, modular, and maintainable as it grows.

