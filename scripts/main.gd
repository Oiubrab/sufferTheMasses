extends Node2D

var agent := preload("res://scripts/agent.gd").new()

func _ready() -> void:
    add_child(agent)
    agent.load_data("res://characters/karu.json")
    var action := agent.decide_action()
    print("Agent decided to:", action)
