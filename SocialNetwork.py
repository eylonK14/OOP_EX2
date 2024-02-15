from __future__ import annotations
from User import User
from Post import Post


class SocialNetwork:
    __instance = None
    __is_init = False
    __name = str
    __users = []  # iniat map of names so we won't have any name  more than once

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, name)
        return cls.__instance

    def __init__(self, name: str):
        if not self.__is_init:
            self.__is_init = True
            cls.__name = name
            return self.__new__(self)
        return self.__instance

    def __str__(self):
        print(f"{self.__name} social network:")
        for user in self.__users:
            print(user)

    def sign_up(self, name: str, password: str) -> User:
        if (not len(password) in range(4, 9) or self.users.__contains__()):  # TODO
            user = User(name, password)
            return user

    def log_in(self, user: User):
        if not user.logged():
            user.set_logged(True)
            print(user.get_name() + " connected")
    def log_out(self, user: User):
        if user.logged():
            user.set_logged(False)
            print(user.get_name()+ " disconnected")