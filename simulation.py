import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Optional
# comment test

@dataclass
class EmotionalTraits:
    fear: float
    inquisitiveness: float
    courage: float
    libido: float
    risk_tolerance: float
    bonding_desire: float
    solitude_desire: float


@dataclass
class PhysicalTraits:
    sex: str
    height_cm: int
    weight_kg: int
    strength: float
    flexibility: float
    dexterity: float
    fertility: float


@dataclass
class PhysiologicalNeeds:
    hunger: float
    thirst: float
    fatigue: float
    temperature_stress: float
    pain: float


@dataclass
class Concept:
    confidence: float
    emotional_association: Dict[str, float]
    action_affinity: List[str]


@dataclass
class ActionKnowledge:
    effort: float
    requires: List[str]
    effects: List[str]


@dataclass
class MemoryEvent:
    event_signature: List[str]
    emotional_tone: Dict[str, float]
    result: str
    salience: float
    inferred_link: Optional[str] = None


@dataclass
class Agent:
    id: str
    name: str
    age: int
    physical_traits: PhysicalTraits
    emotional_traits: EmotionalTraits
    physiological_needs: PhysiologicalNeeds
    concept_knowledge: Dict[str, Concept]
    action_knowledge: Dict[str, ActionKnowledge]
    memory: List[MemoryEvent] = field(default_factory=list)


@dataclass
class WorldObject:
    id: str
    name: str
    material: str
    properties: List[str]


@dataclass
class Tile:
    id: str
    position: Tuple[int, int]
    biome: str = ""
    elevation: float = 0.0
    temperature: float = 0.0
    objects: List[WorldObject] = field(default_factory=list)
    agents_present: List[str] = field(default_factory=list)


class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: Dict[Tuple[int, int], Tile] = {}
        for x in range(width):
            for y in range(height):
                tile_id = f"tile_{x}_{y}"
                self.grid[(x, y)] = Tile(id=tile_id, position=(x, y))

    def get_tile(self, x: int, y: int) -> Tile:
        return self.grid[(x, y)]



def agent_from_dict(data: Dict) -> Agent:
    physical = PhysicalTraits(**data["physical_traits"])
    emotional = EmotionalTraits(**data["emotional_traits"])
    physiological = PhysiologicalNeeds(**data["physiological_needs"])

    concepts = {
        k: Concept(**v) for k, v in data.get("concept_knowledge", {}).items()
    }
    actions = {
        k: ActionKnowledge(**v) for k, v in data.get("action_knowledge", {}).items()
    }
    memory = [MemoryEvent(**m) for m in data.get("memory", [])]
    return Agent(
        id=data["id"],
        name=data["name"],
        age=data["age"],
        physical_traits=physical,
        emotional_traits=emotional,
        physiological_needs=physiological,
        concept_knowledge=concepts,
        action_knowledge=actions,
        memory=memory,
    )


def load_agent_from_file(path: str) -> Agent:
    """Load an Agent definition from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return agent_from_dict(data)


def agent_to_dict(agent: Agent) -> Dict:
    """Convert an Agent dataclass to a dictionary suitable for JSON."""
    return asdict(agent)


def save_agent_to_file(agent: Agent, path: str) -> None:
    """Serialize an Agent to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(agent_to_dict(agent), f, indent=2)


def initialize_world(width: int, height: int) -> World:
    """Create a world grid with empty tiles."""
    return World(width, height)

# --- Inference Cycle Stubs -------------------------------------------------

def update_physiological_drives(agent: Agent, hunger_rate: float = 0.01) -> None:
    """Very simple placeholder for increasing drives over time."""
    needs = agent.physiological_needs
    needs.hunger = min(needs.hunger + hunger_rate, 1.0)


def retrieve_relevant_memories(agent: Agent, context: List[str]) -> List[MemoryEvent]:
    """Return memories containing any of the context labels."""
    return [m for m in agent.memory if any(tag in context for tag in m.event_signature)]


def evaluate_memory_salience(memories: List[MemoryEvent]) -> Optional[MemoryEvent]:
    """Pick the most salient memory as a placeholder."""
    if not memories:
        return None
    return max(memories, key=lambda m: m.salience)


def modify_emotional_state(agent: Agent, memory: Optional[MemoryEvent]) -> None:
    """Adjust fear slightly based on a remembered event."""
    if memory:
        agent.emotional_traits.fear = min(
            1.0,
            max(0.0, agent.emotional_traits.fear + memory.emotional_tone.get("fear", 0)),
        )


def decide_action(agent: Agent) -> Optional[str]:
    """Choose the first known action. Real logic would be far richer."""
    if agent.action_knowledge:
        return next(iter(agent.action_knowledge))
    return None


def execute_action(agent: Agent, action: Optional[str], world: World) -> str:
    """Placeholder action execution."""
    if action is None:
        return "idle"
    return f"{agent.name} performs {action}"


def log_memory(agent: Agent, result: str, context: List[str]) -> None:
    """Record the result of an action as a new memory."""
    agent.memory.append(
        MemoryEvent(
            event_signature=context,
            emotional_tone={},
            result=result,
            salience=0.1,
        )
    )


def run_simulation_tick(agent: Agent, world: World, context: List[str]) -> str:
    """Run a simplified inference cycle for a single agent."""
    update_physiological_drives(agent)
    memories = retrieve_relevant_memories(agent, context)
    salient = evaluate_memory_salience(memories)
    modify_emotional_state(agent, salient)
    action = decide_action(agent)
    result = execute_action(agent, action, world)
    log_memory(agent, result, context)
    return result
