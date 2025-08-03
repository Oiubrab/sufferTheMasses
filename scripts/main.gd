extends Node2D

@onready var character_popup: AcceptDialog = $UI/CharacterPopup
var character_scene: PackedScene = preload("res://scenes/character.tscn")

func _ready() -> void:
    _spawn_character("res://characters/karu.json", Vector2(200, 200))
    _spawn_character("res://characters/mino.json", Vector2(400, 400))

func _spawn_character(data_path: String, position: Vector2) -> void:
    var character: Node2D = character_scene.instantiate()
    character.position = position
    character.data_path = data_path
    character.clicked.connect(_on_character_clicked)
    add_child(character)

func _on_character_clicked(data: Dictionary) -> void:
    character_popup.display(data)
