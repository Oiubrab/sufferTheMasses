# sufferTheMasses

Building a Strategy Game that more accurately represents real politics and economics.

The project now includes a minimal **Godot** setup alongside the early Python
prototype. Open `project.godot` in Godot to experiment with the scene and see
how character data from `characters/karu.json` can drive simple actions.

## Godot Usage
1. Install Godot 4.
2. Open this repository folder in the Godot editor.
3. Run the project. The console will print the action chosen for Karu based on
   the JSON definition.

## Python Prototype
The `simulation.py` module contains dataclasses for agents and world tiles, plus
helpers to build a sparse world grid. `example_usage.py` demonstrates loading an
agent, updating state, and executing a stubbed simulation tick.