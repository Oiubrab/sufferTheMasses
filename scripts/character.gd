extends Node2D

signal clicked(data: Dictionary)

@export var data_path: String

var data: Dictionary = {}

@onready var sprite: Sprite2D = $Sprite2D
@onready var area: Area2D = $Area2D

func _ready() -> void:
    _load_data()
    area.input_pickable = true
    area.connect("input_event", _on_area_input_event)

func _load_data() -> void:
    if FileAccess.file_exists(data_path):
        var file: FileAccess = FileAccess.open(data_path, FileAccess.READ)
        var text: String = file.get_as_text()
        file.close()
        var parsed: Variant = JSON.parse_string(text)
        if typeof(parsed) == TYPE_DICTIONARY:
            data = parsed
        else:
            push_error("Failed to parse character data at %s" % data_path)
    else:
        push_error("Character data file not found: %s" % data_path)

func _on_area_input_event(viewport: Viewport, event: InputEvent, shape_idx: int) -> void:
    if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
        emit_signal("clicked", data)
