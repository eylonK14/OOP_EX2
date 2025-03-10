from __future__ import annotations
from User import User
import importlib
# the social network implement the singleton design pattern
importlib.import_module('User')


class SocialNetwork:
    __instance = None
    __is_init = False

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        if self.__is_init:
            return
        self.__name = name
        self.__users: dict[str, User] = {}

        self.__is_init = True
        print(f"The social network {self.__name} was created!")

    def __str__(self) -> str:
        users = ""
        print(f"{self.__name} social network:")
        for user in self.__users.values():
            users += str(user) + "\n"
        return users[:-1]

    def sign_up(self, name: str, password: str) -> User:    # password is legal only if its between 4 and 9 and username
        # is unique
        if not len(password) in range(4, 9) or not self.__users.keys().__contains__(name):
            user = User(name, password)
            self.__users[name] = user
            return user

    def log_in(self, username: str, password: str) -> None:     # if user isn't logged and the pass is correct
        if not self.__users[username].logged() and self.__users[username].get_pass() == password:
            self.__users[username].set_logged(True)
            print(self.__users[username].get_name() + " connected")

    def log_out(self, username: str):
        if self.__users[username].logged():     # if user is logged
            self.__users[username].set_logged(False)
            print(self.__users[username].get_name() + " disconnected")
