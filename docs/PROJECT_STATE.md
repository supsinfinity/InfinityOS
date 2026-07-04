# InfinityOS
# AI Project State & Development Handoff

Last Updated:
Genesis v0.1

Project Lead:
Aarav Gupta

---

# What is InfinityOS?

InfinityOS is a desktop environment currently being built in Python using GTK4.

The long-term goal is NOT to create another Linux distribution.

Instead, InfinityOS is intended to become a modern desktop experience that can eventually run on top of multiple desktop environments (GNOME, Hyprland, etc.) while maintaining its own identity.

During Genesis, desktop integration is NOT the priority.

The priority is building clean architecture.

---

# Philosophy

InfinityOS should feel:

- calm
- minimal
- intelligent
- adaptive
- distraction-free

The desktop should never overwhelm the user with information.

Instead it should surface only what is useful at the current moment.

This idea is called Context First Design.

---

# Core Philosophy

The biggest design decision already made is this:

The center of the Infinity Bar is NOT a music widget.

It is called the Context Engine.

Music is only one possible context.

Possible future contexts include:

• Music
• Focus Mode
• Navigation
• Calendar Events
• AI Assistant
• Timers
• Coding Status
• Notifications

The Context Engine chooses which module should be displayed.

This philosophy should be preserved.

---

# Focus Mode

Focus Mode is considered one of the signature features of InfinityOS.

It is NOT simply another desktop mode.

Eventually Focus Mode should:

Hide unnecessary information

Reduce distractions

Replace center content with:

Current task

Timer

Progress

Potentially dim or hide other modules.

Focus Mode changes behavior, not just colors.

---

# Development Strategy

The project intentionally follows a layered architecture.

Layer 1

Core

↓

Layer 2

Services

↓

Layer 3

Components

↓

Layer 4

Window/Layout

The window should know almost nothing.

Its only responsibility is placing components.

Application logic should never be added to window.py unless absolutely necessary.

---

# Current Architecture

src/

bar/

window.py

style.css

components/

clock.py

context.py

infinity.py

Future folders

core/

services/

launcher/

dashboard/

notifications/

focus/

---

# Component Philosophy

Every visual object should eventually become a component.

Example

ClockComponent

Owns:

widget

timer

updates

future interactions

ContextComponent

Owns:

current context display

future animations

future transitions

InfinityComponent

Owns:

Infinity button

future launcher

future menu

future command palette

Window simply assembles these.

---

# Why Components Exist

Components allow features to evolve independently.

For example:

ClockComponent may later gain

calendar popup

multiple time zones

timers

Pomodoro

without changing window.py.

---

# Services (Future)

Services provide data.

Examples

MusicService

WeatherService

CalendarService

SystemService

AIService

Services should never directly manipulate GTK widgets.

Instead:

Service

↓

Component

↓

Window

---

# Future Event System

Eventually components should communicate using events.

Example

Spotify changes song

↓

MusicService

↓

Event Bus

↓

ContextComponent updates

Another example

Focus Mode starts

↓

Event Bus

↓

Weather hides

Memory hides

Timer appears

Wallpaper changes

This architecture should be preferred over tightly coupling components together.

---

# UI Philosophy

The Infinity Bar has three logical regions.

LEFT

Identity

Infinity Button

Workspace

Launcher

CENTER

Context Engine

Dynamic

Only one primary context at a time.

RIGHT

System Status

Clock

Weather

Memory

CPU

Battery

Calendar

The center should remain flexible.

---

# Current Progress

Genesis Progress

Approximately 40%

Completed

✓ Repository initialized with Git

✓ Basic documentation created

✓ GTK4 application launches

✓ CSS loading works

✓ Live clock works

✓ Component architecture introduced

✓ Clock extracted into ClockComponent

✓ Context extracted into ContextComponent

✓ Infinity button extracted into InfinityComponent

✓ Window is becoming layout-only

---

# Important Decisions Already Made

Desktop integration has intentionally been postponed.

Instead of fighting GNOME now,

finish the architecture first.

Later:

GNOME Extension

Hyprland Layer Shell

Wayland integration

will be added.

This order should be preserved.

---

# Current Session

Current task

Build the Infinity dropdown menu.

The Infinity button should no longer print to the console.

It should instead open a small GTK dropdown.

This is only temporary.

Later it will evolve into the Infinity Launcher.

---

# Planned Evolution

Phase 1

Simple dropdown

↓

Phase 2

Modern popup

↓

Phase 3

Command Palette

↓

Phase 4

AI Launcher

The launcher should eventually resemble a command palette more than a traditional application menu.

---

# Coding Standards

Follow PEP8.

Keep files short.

Prefer many small files over one giant file.

Avoid putting feature logic inside window.py.

Keep components reusable.

Prefer readable code over clever code.

Explain architectural decisions when introducing major changes.

---

# Current Roadmap

Genesis v0.2

Infinity Menu

Rounded floating panel

Improved styling

Genesis v0.3

Weather

Music

Memory

CPU

Genesis v0.4

Focus Mode

Dashboard

Launcher

Context switching

Genesis Complete

Theme engine

Services layer

Settings

Event system

---

# Long-Term Vision

InfinityOS should eventually become a desktop platform rather than a single application.

Major future features:

Infinity Bar

Launcher

Dashboard

Focus Mode

Context Engine

AI Assistant

Workspace Manager

Plugin System

Theme Engine

Adaptive UI

The project should feel professionally engineered while remaining understandable to beginners.

---

# Instructions for Future AI Sessions

When continuing this project:

Understand the existing architecture before suggesting changes.

Do not redesign components without a clear benefit.

Preserve the Context Engine philosophy.

Preserve the separation between:

Core

Services

Components

Window

Prefer incremental improvements.

When suggesting new features:

Explain WHY the architecture should change.

Avoid quick hacks.

Keep the project maintainable.

Treat this project as if it will eventually become a real open-source desktop environment.
