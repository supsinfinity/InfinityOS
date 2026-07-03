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
