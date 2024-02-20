# this class represent the user calls in the social network implement the design
from __future__ import annotations
from collections import OrderedDict
from Factory import create_post


class User:

    def __init__(self, name: str, password: str):
        self.__following = set()
        self.__notifications = list()
        self.__followers = set()
        self.__name = name
        self.__password = password
        self.__num_of_posts = 0
        self.__is_logged = True

    def __str__(self):
        return ("User name: " + self.__name + ", Number of posts: " + str(self.__num_of_posts) + (", Number of "
                                                                                                  "followers: ") +
                str(len(self.__followers)))

    def follow(self, user: User) -> None:
        if user not in self.__following and self.__is_logged and self.get_name() != user.get_name():  # if the user isn't a follower add him
            self.__following.add(user)
            user.__followers.add(self)
            print(self.__name + " started following " + user.__name)

    def unfollow(self, user: User) -> None:
        if self.__following and self.__is_logged:  # if the set isn't empty delete the user
            self.__following.remove(user)
            user.__followers.remove(self)
            print(self.__name + " unfollowed " + user.__name)

    def publish_post(self, post_type: str, *args):
        if self.__is_logged:
            self.__num_of_posts += 1
            p = create_post(post_type, self, *args)
            for user in self.__followers:
                user.__notifications.append(f"{self.__name} has a new post")
            print(p)

            return p

    def print_notifications(self) -> None:  # print all the notifications
        if self.__is_logged:
            print(self.__name + "'s notifications:")
            for notify in self.__notifications:
                print(notify)

    def add_notification(self, notification: str) -> None:
        self.__notifications.append(notification)

    def get_name(self) -> str:
        return self.__name

    def get_pass(self) -> str:
        return self.__password

    def logged(self) -> bool:
        return self.__is_logged

    def set_logged(self, state: bool) -> None:
        self.__is_logged = state
