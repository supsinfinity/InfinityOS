# InfinityOS Architecture

InfinityOS is composed of modules.

Modules never depend directly on one another.

Everything communicates through services.

Example

Music Widget
        ↓
 Music Service
        ↓
 Music Player

# InfinityOS Architecture

## Principle 1

Widgets never communicate directly.

Everything goes through services.

## Principle 2

Core logic is desktop-independent.

## Principle 3

Desktop-specific code lives in `/backends`.

## Principle 4

Every module should be replaceable without affecting the rest of the system.
