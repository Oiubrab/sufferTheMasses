extends Node

var data: Dictionary = {}

func load_data(path: String) -> void:
    var file := FileAccess.open(path, FileAccess.READ)
    if file:
        var text := file.get_as_text()
        data = JSON.parse_string(text)
        file.close()

func decide_action() -> String:
    var actions := data.get("action_knowledge", {})
    for action_key in actions.keys():
        return action_key
    return "idle"
