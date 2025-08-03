extends Node

var data: Dictionary = {}

func load_data(path: String) -> void:
    if not FileAccess.file_exists(path):
        push_error("Agent data file not found: %s" % path)
        return

    var file: FileAccess = FileAccess.open(path, FileAccess.READ)
    var text: String = file.get_as_text()
    file.close()

    var parsed: Variant = JSON.parse_string(text)
    if typeof(parsed) == TYPE_DICTIONARY:
        data = parsed
    else:
        push_error("Failed to parse agent data in %s" % path)
        data = {}

func decide_action() -> String:
    var actions: Dictionary = data.get("action_knowledge", {})
    for action_key in actions.keys():
        return action_key
    return "idle"
