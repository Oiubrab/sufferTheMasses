extends AcceptDialog

func display(data: Dictionary) -> void:
    var details := ""
    details += "Name: %s\n" % data.get("name", "Unknown")
    details += "Age: %s\n" % str(data.get("age", "?"))
    var traits: Dictionary = data.get("physical_traits", {})
    if traits:
        details += "Height: %s cm\n" % str(traits.get("height_cm", "?"))
        details += "Weight: %s kg" % str(traits.get("weight_kg", "?"))
    dialog_text = details
    popup_centered()
