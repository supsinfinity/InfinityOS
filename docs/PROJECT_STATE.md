InfinityOS
AI Project State & Development Handoff

Last Updated:
Genesis v0.2 (Complete)

Project Lead:
Aarav Gupta

What is InfinityOS?

InfinityOS is a context-aware desktop platform currently implemented as a GTK4 desktop environment, currently being built in Python using GTK4.

The long-term goal is NOT to create another Linux distribution.

Instead, InfinityOS aims to become a modern desktop platform that can eventually run on top of multiple desktop environments (GNOME, Hyprland, etc.) while maintaining its own identity.

During Genesis, desktop integration is intentionally postponed.

The priority is building a clean, maintainable architecture that future features can be built upon.

# Why InfinityOS Exists

InfinityOS began as a learning project to teach professional software engineering through building a real desktop environment.

The project has two equally important goals:

1. Learn software architecture, Python, GTK, Git, and desktop technologies by building a real application.

2. Create a desktop experience that adapts to the user's current task instead of forcing the user to adapt to the computer.

While both goals are important, creating a context-aware desktop experience is the project's primary long-term objective.

InfinityOS is intended to become more than a desktop bar. It should eventually become an intelligent workspace that helps users focus, multitask, and reduce distractions through context-aware interfaces.

Philosophy

InfinityOS should feel:

calm
minimal
intelligent
adaptive
distraction-free

The desktop should never overwhelm the user with information.

Instead, it should surface only what is useful at the current moment.

This idea is called Context First Design.

Core Philosophy

The center of the Infinity Bar is NOT a music widget.

It is called the Context Engine.

Music is only one possible context.

Possible future contexts include:

Music
Focus Mode
Navigation
Calendar Events
AI Assistant
Timers
Coding Status
Notifications

Only one primary context should be displayed at a time.

The Context Engine chooses which module is most relevant.

This philosophy should be preserved.

Focus Mode

Focus Mode is one of the signature features of InfinityOS.

It is not simply another desktop mode.

Eventually Focus Mode should:

Hide unnecessary information
Reduce distractions
Display only the current task
Display timer/progress
Hide or dim less important modules
Modify desktop behavior rather than only changing colors

Focus Mode changes behavior, not appearance.

Development Strategy

InfinityOS follows a layered architecture.

Core
    ↓
Services
    ↓
Components
    ↓
Window / Layout

Each layer should only communicate downward whenever possible.

window.py should remain almost entirely responsible for layout.

Business logic should never live inside window.py unless absolutely necessary.

# Version History

Genesis v0.1
- GTK application
- Component architecture
- Clock
- Context Engine foundation

Genesis v0.2
- Infinity Launcher
- LauncherMenu component
- Floating launcher styling
- Quit action

Current Version
Genesis v0.2

# Development Workflow

Every session should follow this order:

1. Decide the feature.
2. Explain why it belongs in the architecture.
3. Implement one small step at a time.
4. Keep the application runnable after each step.
5. Refactor only when necessary.
6. Commit working milestones with Git.

# Architectural Decisions Already Made

These decisions should not be revisited unless there is a strong reason.

- The center of the bar is the Context Engine, not a permanent music widget.
- Architecture is more important than adding features quickly.
- Desktop integration is postponed until after Genesis.
- Components should remain small and reusable.
- window.py is responsible for layout only.
- Services will provide data.
- Components display data.
- Future communication should occur through an Event Bus.
- InfinityOS should support GNOME first while keeping future Hyprland compatibility.

Current Architecture
src/

bar/
    window.py
    style.css

components/
    clock.py
    context.py
    infinity.py
    launcher_menu.py

Current Repository Sructure: 

InfinityOS/

docs/

src/

bar/

components/

clock.py

context.py

infinity.py

launcher_menu.py

window.py

style.css

README.md

LICENSE

.gitignore

# Current Known Limitations

These are expected during Genesis.

- Running as a normal GTK window instead of a Layer Shell panel.
- No desktop integration yet.
- No Services layer.
- No Event Bus.
- No Theme Engine.
- Context Engine currently displays placeholder information.

Future

core/
services/
dashboard/
notifications/
focus/
Component Philosophy

Every visible feature should eventually become its own component.

Examples:

ClockComponent

Owns:

Widget
Timer
Clock updates
Future calendar popup
Future timers
ContextComponent

Owns:

Current context display
Context switching
Future animations
InfinityComponent

Owns:

Infinity button
Launcher attachment
LauncherMenu

Owns:

Launcher UI
Menu layout
Launcher actions
Future command palette
Future AI launcher

Window simply assembles components.

Why Components Exist

Components allow features to evolve independently.

Example:

ClockComponent may eventually include:

Calendar
Multiple time zones
Timers
Pomodoro

without modifying window.py.

Services (Next Phase)

Services provide data.

Examples:

WeatherService
MusicService
CalendarService
SystemService
AIService

Services should never manipulate GTK widgets directly.

Architecture:

Service
    ↓
Component
    ↓
Window

The Services layer will be introduced during Genesis v0.3 before building Weather or system monitoring.

Future Event System

Eventually components should communicate using an Event Bus.

Example:

Spotify changes song

↓

MusicService

↓

Event Bus

↓

ContextComponent updates

Another example:

Focus Mode starts

↓

Event Bus

↓

Weather hides

Memory hides

Timer appears

Wallpaper changes

Components should never become tightly coupled.

UI Philosophy

The Infinity Bar has three logical regions.

LEFT

Identity

Infinity Button
Workspace
Launcher
CENTER

Context Engine

Dynamic.

Only one primary context should appear at any time.

RIGHT

System Status

Clock
Weather
Memory
CPU
Battery
Calendar

The center should remain flexible.

Project Principles

• Architecture before features.
• Learn before optimize.
• Small components over large files.
• Maintainability over shortcuts.
• Build one working step at a time.
• Every feature should support the long-term vision.

## Git Workflow

Use Git as part of the normal development process.

- Do not commit after every small change.
- Commit only when a feature or milestone is complete and the application is working.
- Before suggesting a commit, ensure the project builds and runs correctly.
- Suggest clear, descriptive commit messages following the current project version.

## Refactoring Policy

Avoid large rewrites unless they provide a significant architectural benefit.

Prefer incremental improvements that preserve existing functionality.

Keep the application runnable after every development session.

Examples:

Genesis v0.2: Infinity launcher and component architecture

Genesis v0.3: Introduce Services layer

Genesis v0.4: Focus Mode foundation

The assistant should remind the user to commit after completing a meaningful milestone but should not interrupt development with unnecessary commits.

Current Progress

Genesis Progress

Approximately 60% Complete

Completed

✓ Git repository initialized
✓ Documentation created
✓ GTK4 application launches
✓ CSS loading
✓ Live clock
✓ Component architecture
✓ ClockComponent
✓ ContextComponent
✓ InfinityComponent
✓ LauncherMenu component
✓ Layout-only window architecture
✓ Infinity Launcher (Genesis version)
✓ Styled floating launcher
✓ Working Quit action
✓ GTK CSS architecture improvements
Important Architectural Decisions
Desktop integration is postponed

Architecture comes before platform integration.

Later phases will add:

GNOME Extension
Wayland Layer Shell
Hyprland integration
Desktop services
Launcher Architecture

The launcher is implemented using:

Gtk.MenuButton
        ↓
Gtk.Popover
        ↓
LauncherMenu

GTK manages popup behavior.

LauncherMenu owns launcher contents.

InfinityComponent owns only the Infinity button.

Constructor Philosophy

Constructors (__init__) should remain small.

UI construction belongs inside helper methods such as:
F
_build_ui()
Component Responsibility

Each component should have one primary responsibility.

Example:

InfinityComponent

owns button

LauncherMenu

owns launcher

Window

owns layout
Current Session Status

Genesis v0.2 is complete.

The next milestone is beginning the Services layer.

The first task should be creating the base Service architecture before implementing Weather, Music, CPU, or Memory.

Planned Evolution

Launcher

Simple Dropdown
        ↓
Styled Launcher
        ↓
Command Palette
        ↓
AI Launcher

The launcher should eventually resemble a command palette rather than a traditional application menu.

Coding Standards
Follow PEP8
Keep files short
Prefer many small files
Avoid business logic inside window.py
Components should remain reusable
Prefer readability over cleverness
Refactor regularly to remove duplication
Explain architectural decisions before implementing them
Current Roadmap
Genesis v0.3

Introduce Services layer

Base Service class
WeatherService
MusicService
SystemService
Begin right-side status modules
Genesis v0.4

Focus Mode

Dashboard

Context switching

Launcher improvements

Genesis Complete
Theme Engine
Settings
Event Bus
Service architecture
Desktop integration preparation
Future Phases
Exodus (v1.x)

Desktop Integration

GNOME Extension
Wayland Layer Shell
IPC
DBus
Autostart
Notifications
Existing desktop integration
Infinity (v2.x)

Desktop Platform

Potential long-term features:

Workspace Manager
Window Management / Wayland compositor research
Plugin System
AI Assistant
Adaptive UI
Theme Engine
Full desktop platform
Long-Term Vision

InfinityOS should eventually become a desktop platform rather than a single GTK application.

Every architectural decision made during Genesis should make future expansion easier rather than harder.

The project should feel professionally engineered while remaining understandable to beginners.

Instructions for Future AI Sessions

When continuing this project:

Understand the current architecture before suggesting changes.
Preserve the Context Engine philosophy.
Preserve the layered architecture:
Core
    ↓
Services
    ↓
Components
    ↓
Window
Prefer incremental improvements over large rewrites.
Explain architectural changes before implementing them.
Avoid quick hacks.
Keep the project maintainable.
Treat InfinityOS as if it will eventually become a real open-source desktop platform.
AI Collaboration Preferences

These instructions are important.

The user is learning software engineering while building InfinityOS.

The goal is not just to finish the project.

The goal is to understand how and why the software is designed.

When helping:

Give ONE step at a time.
Keep explanations short and focused.
If two small steps naturally belong together, combine them.
Wait for the user to finish before continuing.
Explain why before how.
Assume the user is still learning Python and GTK.
Clearly state:
which file to open,
exactly where code goes,
what to replace or add.
Avoid introducing many new concepts at once.
Act as a mentor rather than only generating code.
Refactor toward clean architecture instead of adding quick fixes.
End development sessions with a working application whenever possible.
Assume development sessions typically last 30–60 minutes, and pace work accordingly.

InfinityOS Architecture

InfinityOS is built as a collection of independent layers.

Each layer has a single responsibility.

Higher layers should never bypass lower layers.

Whenever possible, communication flows through well-defined interfaces instead of direct dependencies.

Backends
      │
      ▼
Services
      │
      ▼
Event Bus
      │
      ▼
Components
      │
      ▼
Window / Layout

This architecture allows each layer to evolve independently while keeping the project maintainable.

Layer Responsibilities
Backends

Backends communicate directly with the operating system.

Examples include:

psutil
DBus
NetworkManager
Wayland
GNOME APIs
Filesystem
Audio APIs

Backends never contain business logic.

Their responsibility is simply to retrieve or modify system information.

Examples:

SystemBackend

WeatherBackend

MediaBackend

BatteryBackend

NetworkBackend

Backends should remain platform-specific.

If InfinityOS eventually supports multiple desktop environments, only the backend layer should require significant changes.

Services

Services provide application logic.

A service owns data.

A service decides:

when to update
how to process data
when to notify the rest of the application

Services never manipulate GTK widgets.

Examples:

WeatherService

SystemService

SettingsService

MediaService

NotificationService

Services receive information from backends and expose it through clean APIs.

Example:

SystemBackend
        ↓
reads CPU

↓

SystemService
stores CPU usage

↓

CPUComponent
displays CPU usage
Event Bus

The Event Bus provides communication between services and components.

Instead of components constantly polling for updates, services announce when something changes.

Example:

SystemService

↓

SYSTEM_CHANGED

↓

CPUComponent refreshes

MemoryComponent refreshes

BatteryComponent refreshes

Another example:

WeatherService

↓

WEATHER_CHANGED

↓

WeatherComponent refreshes

Events notify.

Services provide data.

Components never depend directly on other components.

Loose coupling is one of the core architectural goals of InfinityOS.

InfinityCore

InfinityCore is the application's central infrastructure object.

It owns the systems that make the application function.

Responsibilities include:

EventBus
ServiceManager
BackendManager

InfinityCore does not own UI.

InfinityCore does not build widgets.

InfinityCore exists to initialize and coordinate the application's backend architecture.

Example:

InfinityCore

├── EventBus

├── BackendManager

└── ServiceManager

Every component receives a reference to InfinityCore.

Through InfinityCore, components can safely access services without needing to know how they were created.

BackendManager

BackendManager owns every backend.

Responsibilities:

Register backends
Initialize backends
Shut down backends
Provide access to registered backends

Example:

BackendManager

├── SystemBackend

├── WeatherBackend

├── NetworkBackend

└── MediaBackend

Adding a new backend should require only registration with BackendManager.

ServiceManager

ServiceManager owns every service.

Responsibilities:

Register services
Start services
Stop services
Provide service lookup

Example:

ServiceManager

├── WeatherService

├── SystemService

├── SettingsService

└── NotificationService

Window code should never manually create services.

Everything should flow through ServiceManager.

Base Classes

InfinityOS uses base classes to establish consistent behavior throughout the project.

Backend

Every backend inherits from:

Backend

Responsibilities:

initialize()
shutdown()

Provides a consistent lifecycle for every backend.

Service

Every service inherits from:

Service

Responsibilities:

start()
stop()

Provides a common lifecycle and shared functionality.

Component

Every UI component inherits from:

Component

Responsibilities:

Own a GTK widget
Automatically subscribe to events (when applicable)
Access services through InfinityCore
Display data

Components should never own business logic.

Component Philosophy

Each visible feature should eventually become its own component.

Examples:

ClockComponent

WeatherComponent

CPUComponent

MemoryComponent

BatteryComponent

ContextComponent

InfinityComponent

NotificationComponent

Each component owns only one responsibility.

Example

ClockComponent owns:

Clock widget
Timer updates
Future calendar popup
Future timers

WeatherComponent owns:

Weather display
Weather formatting

CPUComponent owns:

CPU display

ContextComponent owns:

Current context
Future context animations
Future context transitions

InfinityComponent owns:

Infinity button
Launcher attachment

LauncherMenu owns:

Launcher interface
Command execution
Future command palette
Future AI launcher

Window simply assembles components.

Current Repository Structure
InfinityOS/
│
├── docs/
│
├── src/
│   └── bar/
│
│       ├── app.py
│       ├── main.py
│       ├── window.py
│       ├── style.css
│       │
│       ├── core/
│       │   ├── application.py
│       │   ├── constants.py
│       │   ├── logger.py
│       │   ├── version.py
│       │   └── events/
│       │
│       ├── backends/
│       │   ├── backend.py
│       │   ├── backend_manager.py
│       │   └── system_backend.py
│       │
│       ├── services/
│       │   ├── service.py
│       │   ├── service_manager.py
│       │   ├── weather_service.py
│       │   ├── system_service.py
│       │   └── settings_service.py
│       │
│       └── components/
│           ├── base/
│           ├── launcher/
│           ├── context/
│           ├── layout/
│           ├── information/
│           ├── system/
│           └── clock/
│
├── README.md
├── LICENSE
└── .gitignore

The repository is organized by responsibility rather than feature size.

As InfinityOS grows, new functionality should fit naturally into the existing structure rather than requiring large reorganizations.

Architectural Decisions

The following decisions are considered foundational.

They should not be revisited unless there is a compelling architectural reason.

The center of the Infinity Bar is the Context Engine, not a permanent music widget.
Desktop integration is postponed until Genesis architecture is complete.
Business logic never belongs inside GTK widgets.
Components display data.
Services own data.
Backends interact with the operating system.
Events notify; they do not transport application state.
Managers own object lifecycles.
Window is responsible only for layout.
Architecture is prioritized over rapid feature development.
Components should remain small and reusable.
Prefer composition over inheritance when practical.
Refactor repeated patterns into reusable abstractions instead of duplicating code.

Version History

InfinityOS is being developed in phases named Genesis.

Genesis is focused on building a professional software architecture before introducing advanced desktop functionality.

Every Genesis milestone should leave the project in a working state.

Genesis v0.1

Objective

Establish the first working Infinity Bar.

Completed:

GTK4 application
Initial window
CSS loading
Clock component
Context component
Component architecture
Basic project structure
Git repository initialization

Lessons Learned:

Components are easier to maintain than large window files.
GTK layout should remain separate from business logic.
Genesis v0.2

Objective

Introduce reusable UI architecture.

Completed:

Infinity launcher
LauncherMenu
Gtk.MenuButton launcher
Floating launcher styling
Quit action
Improved CSS architecture
Cleaner component organization

Architectural Decisions:

Launcher uses Gtk.MenuButton
Launcher contents belong to LauncherMenu
Constructors remain small
Window owns layout only
Genesis v0.3

Objective

Build the application's backend architecture.

Completed:

InfinityCore
EventBus
Backend layer
BackendManager
Service layer
ServiceManager
WeatherService
SystemService
Base Backend class
Base Service class
Base Component class
Automatic component event subscription
SystemBackend
CPU monitoring
Weather updates
Repository reorganization
Documentation overhaul

Major Architectural Changes:

Business logic removed from UI
Components now display data only
Services own application state
Backends own operating system interaction
Events became notifications instead of data containers
InfinityCore became the application's infrastructure object

Genesis v0.3 represents the transition from "GTK application" to "desktop platform architecture."

Current Progress

Genesis Progress

Approximately 95% Complete

Completed

✓ Professional repository structure
✓ GTK4 application
✓ CSS architecture
✓ Component architecture
✓ Backend architecture
✓ Service architecture
✓ EventBus
✓ BackendManager
✓ ServiceManager
✓ InfinityCore
✓ Base Backend
✓ Base Service
✓ Base Component
✓ Weather system
✓ CPU monitoring
✓ Status Area
✓ Launcher
✓ Documentation
✓ Git workflow
✓ Coding standards

Remaining

□ Context Engine implementation
□ Settings interface
□ Theme engine foundation
□ Final architecture cleanup
□ Genesis release documentation
Development Workflow

Every development session should follow the same process.

Step 1

Choose one feature.

Never attempt multiple unrelated features simultaneously.

Step 2

Explain why the feature belongs in the architecture.

Questions to answer:

Why is it needed?
Which layer owns it?
How does it fit into InfinityOS?
Step 3

Implement one small step.

The application should continue running after every change.

Step 4

Test immediately.

Never continue building on broken code.

Step 5

Refactor if duplication appears.

Architecture should improve continuously.

Step 6

Commit only after reaching a meaningful milestone.

Git Workflow

Git is considered part of the development process.

Guidelines:

Do not commit every small change.
Commit only when the project builds successfully.
Every commit should represent a completed milestone.
Use descriptive commit messages.

Example:

Genesis v0.3

Introduce Backend architecture

• Added BackendManager
• Added SystemBackend
• Connected SystemService
• Refactored application startup

Tags should mark completed Genesis milestones.

Example:

git tag genesis-v0.3
git push origin genesis-v0.3
Coding Standards

InfinityOS follows several coding standards.

General
Follow PEP 8.
Prefer readability over cleverness.
Keep functions short.
Keep files focused.
Components

Components display information.

Components should never own business logic.

Services

Services own application state.

Services should never manipulate GTK widgets.

Backends

Backends communicate with the operating system.

Backends should remain platform-specific.

Window

Window owns layout only.

Business logic should never live inside window.py.

Constructors

Constructors should remain lightweight.

Initialization belongs inside helper methods when complexity increases.

Duplication

If a pattern appears multiple times, consider refactoring it into a shared abstraction.

Examples include:

Base classes
Helper methods
Managers
Utilities
Refactoring Policy

Refactoring is encouraged when it:

Improves readability
Removes duplication
Strengthens architecture
Simplifies future development

Avoid refactoring solely for stylistic reasons.

Prefer small, incremental improvements over large rewrites.

Current Roadmap
Genesis v0.4

Focus shifts from infrastructure to platform features.

Planned work:

Context Engine
Context selection logic
Dashboard foundation
Launcher evolution
Notification Center
Settings UI

The architecture should remain largely stable during this phase.

Genesis Complete

Architecture goals:

Backend layer
Service layer
EventBus
Theme Engine
Settings
Desktop integration preparation
Exodus (v1.x)

Desktop integration.

Examples:

Wayland Layer Shell
GNOME integration
DBus
Notifications
Autostart
Existing desktop interoperability
Infinity (v2.x)

Desktop platform.

Possible long-term goals:

Plugin system
AI Assistant
Adaptive desktop
Intelligent Context Engine
Workspace manager
Advanced launcher
Theme engine
Window management research
AI Collaboration Guidelines

InfinityOS is also a learning project.

Future AI sessions should teach software engineering rather than simply generate code.

Development should follow these principles:

Explain why before how.
Introduce one concept at a time.
Build one working step at a time.
Keep the project runnable.
Avoid quick hacks.
Refactor toward cleaner architecture.
Preserve existing design decisions.
Keep explanations concise and focused.

When providing implementation instructions:

Specify the file to open.
Explain exactly what to add or replace.
Explain how the change fits into the architecture.
Wait for implementation before introducing the next step.

The goal is not only to finish InfinityOS.

The goal is to understand why professional software is designed the way it is.

Long-Term Vision

InfinityOS should ultimately become more than a desktop bar.

It should become a modern desktop platform built around context awareness, modular architecture, and intelligent interfaces.

Every architectural decision made during Genesis should support that future.

The project should remain approachable to new contributors while demonstrating professional engineering practices.

Success is measured not only by the number of features, but by the quality of the architecture that enables them.

Final Development Principles

These principles summarize the philosophy of InfinityOS.

Architecture before features.
Context before clutter.
Simplicity before complexity.
Maintainability before shortcuts.
One responsibility per class.
Services own data.
Components display data.
Backends access the operating system.
Events notify.
Managers own lifecycle.
Window owns layout.
Keep the application runnable after every step.
Learn continuously through building.
Design for the future without overengineering the present.

End of Document
