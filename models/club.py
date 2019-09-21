class Club:
    def __init__(self, name, description, tags):
        self.name = name
        self.description = description if description is not None else ""
        self.tags = tags if tags is not None else []

    def get_safe_data(self):
        return {
            "name": self.name,
            "description": self.description,
            "tags": self.tags
        }
