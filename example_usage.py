from simulation import (
    load_agent_from_file,
    save_agent_to_file,
    initialize_world,
    WorldObject,
)

# Load Karu from the JSON file
agent = load_agent_from_file("characters/karu.json")

world = initialize_world(5, 5)

# Example of modifying the agent and saving it back
agent.physiological_needs.hunger = 0.5
save_agent_to_file(agent, "characters/karu.json")

# place agent on a tile
world.get_tile(1, 0).agents_present.append(agent.id)

# place a couple objects
world.get_tile(1, 0).objects.append(
    WorldObject(id="obj_001", name="twisted branch", material="wood", properties=["flexible", "sharp_end"])
)
world.get_tile(1, 0).objects.append(
    WorldObject(id="obj_002", name="red clusters", material="flesh", properties=["soft", "juicy", "sweet_smell"])
)

print("Agent:", agent)
print("Tile (1,0):", world.get_tile(1, 0))

