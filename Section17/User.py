class User:
    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

    def print(self):
        print(f"ID: {self.id}\n"
              f"Username: {self.user_name}")