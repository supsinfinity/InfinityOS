# Contributing to InfinityOS

Thank you for contributing to InfinityOS.

InfinityOS is designed as a long-term desktop platform. Code quality, consistency, and architecture are valued more highly than adding features quickly.

Please read this document before making changes.

---

# Development Philosophy

InfinityOS follows a simple rule:

> **Architecture first. Features second.**

Every new feature should fit naturally into the existing architecture.

Avoid adding shortcuts or special cases simply to make a feature work.

---

# Project Structure

```text
src/
├── bar/
│   ├── backends/
│   ├── components/
│   ├── core/
│   ├── services/
│   ├── window.py
│   ├── app.py
│   └── main.py
│
├── utils/
```

Each directory has a single responsibility.

---

# Responsibilities

## Core

Responsible for application infrastructure.

Owns:

* EventBus
* ServiceManager
* Application lifecycle

Core should never contain GTK user interface code.

---

## Services

Services contain application logic.

Services:

* manage state
* cache information
* communicate with backends
* emit events

Services never update GTK widgets directly.

---

## Backends

Backends communicate with the operating system.

Examples:

* psutil
* D-Bus
* system commands
* desktop APIs

Backends should never import components.

---

## Components

Components display information.

Components:

* create GTK widgets
* subscribe to events
* read data from services

Components should never access the operating system directly.

---

## Window

The window is responsible only for layout.

It should arrange components without containing application logic.

---

# Coding Standards

## Keep classes small

Every class should have one responsibility.

If a class begins doing multiple unrelated jobs, split it.

---

## Prefer explicit code

Readable code is preferred over clever code.

Good:

```python
temperature = weather_service.get_temperature()
```

Avoid unnecessary abstraction.

---

## Use descriptive names

Good:

```text
WeatherService
SystemBackend
StatusArea
BatteryComponent
```

Avoid abbreviations unless universally understood.

---

## Keep methods focused

Methods should perform one task.

Large methods should be divided into smaller helper methods.

---

## Avoid duplication

If the same pattern appears several times, consider whether it belongs in a shared base class or helper.

Do not abstract prematurely—only extract common behavior that provides clear value.

---

## Comments

Comments should explain **why**, not **what**.

Good:

```python
# Refresh every two seconds to avoid excessive CPU usage.
```

Avoid comments that simply repeat the code.

---

# EventBus Guidelines

Services emit events.

Components subscribe to events.

Services must never manipulate UI objects directly.

Example:

```text
SystemBackend
        ↓
SystemService
        ↓
EventBus
        ↓
CPUComponent
```

---

# Service Guidelines

Every service should:

* inherit from `Service`
* expose public getter methods
* own application state
* emit events when state changes

Services should never depend on UI components.

---

# Backend Guidelines

Backends should be thin wrappers around operating system functionality.

They should not cache state or implement business logic.

Business logic belongs in services.

---

# Component Guidelines

Components should:

* display information
* retrieve data from services
* refresh when events occur

Components should not perform heavy computation or interact directly with the operating system.

---

# Imports

Group imports in this order:

1. Standard library
2. Third-party libraries
3. InfinityOS modules

Separate each group with a blank line.

Example:

```python
from pathlib import Path

from gi.repository import Gtk

from services.weather_service import WeatherService
```

---

# Formatting

* Use 4 spaces for indentation.
* Follow PEP 8 where practical.
* Use meaningful whitespace to improve readability.
* Prefer multiple short lines over long lines.

---

# Before Opening a Pull Request

Verify that:

* The project runs without errors.
* Existing functionality still works.
* New code follows the architecture.
* New classes have docstrings.
* New modules are placed in the correct directory.
* Dead code and debug prints have been removed.

---

# Design Principles

Every contribution should improve at least one of the following:

* readability
* maintainability
* modularity
* consistency
* extensibility

Avoid introducing complexity without a clear architectural benefit.

---

# Long-Term Vision

InfinityOS is intended to become a modern, modular desktop platform.

Every contribution should move the project toward software that is:

* modular
* desktop-independent
* maintainable
* event-driven
* service-oriented
* easy to understand

When in doubt, choose the solution that keeps the architecture simpler.

