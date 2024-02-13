from __future__ import annotations
from User import User
from  Post import Post

class SocialNetwork:
    users = []  # iniat map of names so we won't have any name  more than once

    def sign_up(self, name: str, password: str) -> User:
        key = name + ", " + password
        if (not len(password) in range(4, 9) or self.users.__contains__()):  # TODO
            user = User(name, password)
            return user
    def log_in(self, user : User):
        if not user.logged():
            self.users.append(user)