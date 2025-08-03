# sufferTheMasses

Building a Strategy Game that more accurately represents real politics and economics.

The project now includes a minimal **Godot** setup that spawns sample
characters on a top-down map. Click the red squares to view basic features
loaded from JSON definitions.

## Godot Usage
1. Install Godot 4.
2. Open this repository folder in the Godot editor.
3. Run the project. You should see a green ground with two red character
   sprites.
4. Click a character to open a popup showing their name, age, height and
   weight.

## Python Prototype
The `simulation.py` module contains dataclasses for agents and world tiles, plus
helpers to build a sparse world grid. `example_usage.py` demonstrates loading an
agent, updating state, and executing a stubbed simulation tick.

