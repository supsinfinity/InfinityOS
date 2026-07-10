InfinityOS

A context-aware desktop platform built around services, events, and intelligent interaction.

![Infinity Bar](docs/images/infinity-bar.png)

What is InfinityOS?

InfinityOS is an experimental desktop platform designed around one core idea:

The computer should understand context instead of forcing the user to manage windows and applications.

Unlike traditional desktop environments, InfinityOS is being built from a clean, modular architecture where every subsystem communicates through services instead of direct dependencies.

The long-term goal is not to create another Linux distribution.

Instead, InfinityOS aims to become a modern desktop platform that can eventually run on top of multiple desktop environments while maintaining its own identity and user experience.

Current Status

Genesis v0.3 — Complete

Current features:

GTK4 desktop bar
Modular component architecture
Event-driven updates
Backend abstraction layer
Service architecture
Weather service
CPU monitoring
Memory monitoring
Battery monitoring
Launcher menu
Logging system
Screenshots
Infinity Bar

Launcher

![Launcher](docs/images/launcher.png)

Architecture

![Architecture](docs/images/architecture.png)

InfinityOS follows a layered architecture:

GTK Window
     │
     ▼
 Components
     │
     ▼
 Services
     │
     ▼
 Backends
     │
     ▼
 Operating System

Every layer has exactly one responsibility.

Components never communicate directly.

Everything flows through services and the EventBus.

Project Structure

![Project Structure](docs/images/project-structure.png)

Example:

backends/
components/
core/
services/
window.py
app.py
main.py
Design Principles
Context-first design
Desktop-independent core
Modular architecture
Replaceable components
Event-driven communication
Clean separation of responsibilities
Technologies
Python 3
GTK4
PyGObject
psutil
Running InfinityOS

Clone the repository:

git clone https://github.com/supsinfinity/InfinityOS.git

Enter the project:

cd InfinityOS/src/bar

Install dependencies:

pip install psutil

Run:

python3 main.py
Roadmap
Genesis v0.1
Project foundation
Genesis v0.2
Initial UI components
Genesis v0.3
Services
Backends
Event system
Architecture refactor
Genesis v0.4 (In Progress)
Context Engine
Better launcher
Settings improvements
Dynamic desktop information
Contributing

Contributions are welcome.

See CONTRIBUTING.md for development guidelines.

Documentation
ARCHITECTURE.md
DECISIONS.md
CONTRIBUTING.md
PROJECT_STATE.md
License

MIT License.

Project Vision

InfinityOS is an attempt to rethink the desktop from the perspective of context rather than applications.

Traditional desktop environments organize work around windows, icons, and applications. As a result, users spend much of their time managing software instead of focusing on the task they are trying to accomplish.

InfinityOS takes a different approach.

Instead of asking, "What application should I open?", InfinityOS asks, "What is the user trying to do?"

Every part of the system is designed to understand context and surface the most relevant information, actions, and tools at the appropriate time. The desktop should feel calm, adaptive, and intelligent without becoming distracting or intrusive.

To support this vision, InfinityOS is being built around a modular, event-driven architecture with clearly defined layers. Components communicate through services, services interact with replaceable backends, and the core remains independent of any specific desktop environment.

The long-term goal is not to build another Linux distribution.

Instead, InfinityOS aims to become a portable desktop platform capable of running across multiple Linux desktop environments while providing a consistent, context-aware experience.

Genesis focuses entirely on building that foundation. Future releases will build intelligent features on top of the architecture established during Genesis.
Development Timeline

Genesis v0.1 — Foundation

The first milestone established the project's direction and initial user interface.

Highlights:

Created the first GTK4 Infinity Bar
Built the initial component system
Implemented the clock
Established project structure
Defined the long-term vision
Genesis v0.2 — Modular UI

The second milestone focused on separating the interface into reusable components.

Highlights:

Modular component architecture
Launcher menu
Context area
Weather component
Status area
Improved styling
Better code organization
Genesis v0.3 — Core Architecture

Genesis v0.3 transformed InfinityOS from a user interface into a software platform.

Highlights:

EventBus
ServiceManager
BackendManager
Backend abstraction
SystemService
WeatherService
SettingsService
Dependency injection
Logging framework
Event-driven updates
CPU monitoring
Memory monitoring
Battery monitoring
Documentation overhaul
Architecture standardization

Genesis v0.3 marks the completion of the architectural foundation of InfinityOS.

Genesis v0.4 — Context Platform (Current)

Planned objectives include:

Expand the Context Engine
Richer launcher interactions
Settings persistence
Improved desktop integration
More backend implementations
Additional system information
Performance optimizations
Begin preparing for intelligent desktop behavior
Long-Term Roadmap

After Genesis, InfinityOS will enter larger development phases focused on delivering the original vision.

Future goals include:

Context-aware workspace management
AI-powered desktop assistance
Adaptive launcher
Intelligent notifications
Focus modes
Calendar and productivity integration
Music awareness
Navigation awareness
Cross-desktop compatibility
Eventually, support for multiple desktop environments while maintaining a unified InfinityOS experience

