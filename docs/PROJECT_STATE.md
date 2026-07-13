InfinityOS
AI Project State & Development Handoff

Last Updated:
Genesis v0.3 (Complete)

Project Lead:
Aarav Gupta

What is InfinityOS?

InfinityOS is a context-aware desktop platform currently being built in Python using GTK4.

The long-term goal is not to create another Linux distribution.

Instead, InfinityOS aims to become an intelligent desktop platform capable of running on top of multiple Linux desktop environments while maintaining its own identity, behavior, and user experience.

The defining idea behind InfinityOS is:

The desktop should understand what the user is doing, not just what applications are open.

Rather than organizing work around applications, InfinityOS organizes the desktop around context.

Examples of future contexts include:

Music
Navigation
Focus Mode
Calendar
Coding
Meetings
AI Assistant
Timers
System Alerts

The center of the Infinity Bar is reserved for the Context Engine, which will dynamically determine the most relevant information to present.

Current Project Status

Genesis v0.3 is complete.

This milestone focused entirely on establishing a scalable software architecture before introducing advanced features.

The project now has:

Modular architecture
Event-driven communication
Service layer
Backend abstraction
Dependency injection
Logging
Documentation
GitHub release pipeline
Public repository

Future development should focus primarily on capabilities rather than infrastructure.

Repository Structure
InfinityOS/
│
├── .github/
│   └── workflows/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   ├── DECISIONS.md
│   ├── DESIGN.md
│   ├── MANIFESTO.md
│   ├── PROJECT_STATE.md
│   ├── TODO.md
│   ├── VISION.md
│   └── images/
│
├── src/
│   └── bar/
│       ├── app.py
│       ├── main.py
│       ├── window.py
│       ├── style.css
│       │
│       ├── core/
│       ├── services/
│       ├── backends/
│       └── components/
│
├── README.md
├── LICENSE
└── CHANGELOG.md
Current Architecture
                InfinityCore
                     │
      ┌──────────────┼──────────────┐
      │              │              │
  EventBus     BackendManager   ServiceManager
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                   WeatherService      SystemService
                         │                     │
                         └──────────┬──────────┘
                                    │
                              GTK Components
                                    │
                             Infinity Window

Every layer has a single responsibility.

Architectural Philosophy

InfinityOS follows several strict design principles.

Components

Components are responsible only for displaying data.

Components never contain business logic.

Components never communicate directly with each other.

Components only respond to events.

Services

Services own application state.

Services retrieve information from backends.

Services emit events whenever state changes.

Services never manipulate GTK widgets.

Backends

Backends communicate with the operating system.

Examples include:

psutil
Weather APIs
Network APIs

Backends contain no application logic.

EventBus

The EventBus provides loose coupling between every major subsystem.

Instead of calling components directly:

Service

↓

EventBus

↓

Component refreshes itself

This architecture allows new functionality to be added without increasing coupling.

Core Infrastructure

Current infrastructure includes:

InfinityCore

Owns:

EventBus
BackendManager
ServiceManager

Responsible for initializing and coordinating the application.

EventBus

Provides event-driven communication.

Current events include:

WEATHER_CHANGED
SYSTEM_CHANGED

Future events will include:

CONTEXT_CHANGED
SETTINGS_CHANGED
MUSIC_CHANGED
ServiceManager

Responsible for:

Registering services
Starting services
Stopping services
Providing service lookup
BackendManager

Responsible for:

Registering backends
Returning backend instances
Supporting dependency injection
Existing Services

Current services:

WeatherService
SystemService
SettingsService

Future services:

ContextService
MusicService
NotificationService
AIService
WorkspaceService
Existing Backends

Current:

SystemBackend

Future:

WeatherBackend
AudioBackend
BluetoothBackend
NetworkBackend
CalendarBackend
Existing Components

Current UI includes:

Infinity button
Context area
Clock
Weather
CPU
Memory
Battery
Status area
Launcher

All components inherit from the shared Component base class.

# Development Principles

When adding new features:

1. Extend the architecture instead of bypassing it.
2. Keep every commit small and focused.
3. Never sacrifice architecture for short-term convenience.
4. Build reusable systems before feature-specific code.
5. If a feature requires multiple hacks, redesign it.
6. Prefer readability over cleverness.
7. The project should remain runnable after every commit.

# Known Technical Debt

Current architectural debt is intentionally minimal.

Future improvements:

- Unit tests
- CI automation
- Theme system
- Plugin architecture (future)
- Configuration persistence
- Packaging

# Definition of Done

A feature is considered complete when:

✓ Architecture reviewed
✓ Code implemented
✓ Logging added
✓ Docstrings written
✓ No print() debugging
✓ README updated if needed
✓ Documentation updated
✓ Git committed
✓ GitHub pushed
✓ Project still runs without errors

# Commit Style

Prefer descriptive commits.

Examples:

feat(context): add ContextService

refactor(core): introduce BackendManager

docs: update architecture

fix(weather): correct event subscription

Avoid generic commits like:

update

changes

fix stuff

working

# Versioning

Genesis milestones represent architectural phases.

Major milestones:

Genesis v0.1
Genesis v0.2
Genesis v0.3
Genesis v0.4

Each Genesis release should:

- receive a Git tag
- have GitHub Release notes
- update CHANGELOG.md
- update PROJECT_STATE.md

# Future Direction

InfinityOS should become increasingly data-driven.

Future features should be implemented as new Services, Providers, or Backends rather than expanding existing classes.

# Performance Philosophy

InfinityOS should remain lightweight.

Guidelines:

- Minimize background work.
- Prefer event-driven updates over polling.
- Avoid blocking the GTK main thread.
- Keep UI refreshes inexpensive.
- Cache data when appropriate.

# Security Philosophy

- Never hardcode secrets.
- Read API keys from environment variables or configuration files.
- Never commit credentials.
- Validate external input.

# User Experience Principles

InfinityOS should feel:

- Calm
- Intentional
- Predictable
- Minimal
- Responsive

The interface should never compete for attention.

Information should appear because it is useful, not because it is available.

Animation should communicate state rather than decorate the interface.

When in doubt:

Architecture > Features

Maintainability > Cleverness

Context > Widgets

Quality > Speed

Consistency > Customization


Infinity Bar
The primary desktop interface.

Context
The single highest-priority piece of information the user should see.

Provider
A class capable of supplying context.

Service
Owns application state and business logic.

Backend
Interfaces with the operating system or external APIs.

Component
Displays data only.

Manager
Coordinates lifecycle and object ownership.

Future Milestones:

Genesis v0.4
Context Engine

Genesis v0.5
Launcher

Genesis v0.6
Desktop Integration

Genesis v0.7
Notifications

Genesis v0.8
AI Integration

Genesis v0.9
Performance

Genesis v1.0
Daily-driver capable

main

Always stable.

genesis-v0.x

Development branch for the current milestone.

Feature branches

Optional for larger work.


Release Checklist:

Update CHANGELOG

Update PROJECT_STATE

Update README screenshots

Verify documentation

Run application

Commit

Tag release

Publish GitHub Release


Genesis Timeline
Genesis v0.1

Completed.

Introduced:

Initial GTK application
Infinity Button
Live Clock
Basic component architecture
Genesis v0.2

Completed.

Introduced:

Launcher
UI modularization
Improved styling
Context placeholder
Layout improvements
Genesis v0.3

Completed.

Introduced:

EventBus
ServiceManager
BackendManager
Dependency injection
WeatherService
SystemService
SettingsService
SystemBackend
Logging
Automatic event subscriptions
Complete documentation
GitHub releases
Public repository

Genesis v0.3 represents the architectural foundation of InfinityOS.

Coding Standards

Every class should include a descriptive docstring.

Every service should inherit from Service.

Every backend should inherit from Backend.

Every component should inherit from Component.

Logging should use the shared logger.

Avoid print statements.

Use type hints where practical.

Follow PEP 8.

Constructors should remain lightweight.

Keep one responsibility per class.

Non-Negotiable Design Decisions

The center of the Infinity Bar belongs exclusively to the Context Engine.

Business logic belongs only in services.

Components display data.

Services own data.

Backends retrieve data.

Managers coordinate objects.

GTK widgets should remain as lightweight as possible.

Architecture is more important than adding features quickly.

Development Workflow

Every feature should follow this order:

Architecture

↓

Discussion

↓

Implementation

↓

Testing

↓

Git Commit

↓

Git Push

↓

GitHub Release (for milestone completion)

Avoid large commits.

Prefer many small commits.

AI Collaboration Guidelines

Future AI assistants should:

Preserve existing architecture.
Explain architectural reasoning before implementation.
Avoid quick fixes that increase coupling.
Favor composition over inheritance.
Keep the project runnable.
Build incrementally.
Continue teaching software engineering principles rather than only providing code.
Encourage terminal-first workflows whenever practical.
Lessons Learned During Genesis

Architecture should stabilize before rapid feature development.

Dependency injection significantly reduced coupling.

The EventBus simplified communication between services and components.

Small, focused classes improved maintainability.

Public releases encourage cleaner engineering practices.

Documentation should evolve alongside the codebase.

Genesis v0.4 Roadmap

The next milestone shifts from infrastructure to platform intelligence.

Primary objective:

Build the Context Engine.

Development order:

ContextService
ContextProvider base interface
Provider registration
Context priority system
CONTEXT_CHANGED events
ContextComponent integration
Placeholder providers
Initial dynamic context switching

The Context Engine will become the defining feature of InfinityOS.



Long-Term Vision

InfinityOS should feel:

Calm
Minimal
Intelligent
Adaptive
Context-aware
Distraction-free

The desktop should proactively surface relevant information while remaining unobtrusive.

The ultimate goal is not to build another desktop environment, but to rethink how users interact with their computers by making context, rather than applications, the primary organizing principle.
