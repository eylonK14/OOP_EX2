from __future__ import annotations
from User import User
from Post import Post


class SocialNetwork:
    __instance = None
    __is_init = False

    # init map of names, so we won't have any name  more than once

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        if self.__is_init:
            return
        self.__name = name
        self.__users = []

        self.__is_init = True
        print(f"The social network {self.__name} was created!")

    def __str__(self):
        print(f"{self.__name} social network:")
        for user in self.__users:
            print(user)

    def sign_up(self, name: str, password: str) -> User:
        if not len(password) in range(4, 9) or self.__users.__contains__():  # TODO
            user = User(name, password)
            return user

    def log_in(self, user: User):
        if not user.logged():
            user.set_logged(True)
            print(user.get_name() + " connected")

    def log_out(self, user: User):
        if user.logged():
            user.set_logged(False)
            print(user.get_name() + " disconnected")
