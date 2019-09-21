class User:
    def __init__(self, username, password, favorites):
        self.username = username
        self.password = password
        self.favorites = favorites if favorites is not None else []

    def get_safe_data(self):
        return {
            "username": self.username,
            "favorites": self.favorites
        }
