# this class represent the user calls in the social netwerk implement the design
from __future__ import annotations
from Post  import  post

class User:
    def __init__(self, name: str, password: str):
        self.__following = set
        self.__notifications = []
        self.__name = name
        self.__password = password
        self.__followers = 0
        self.__num_of_posts = 0
        self.__is_logged = True

    def __str__(self):
        print(
            "User name: " + self.__name + ", Number of posts: " + self.__num_of_post + ", Number of followers: " + self.__followers)

    def follow(self, user: User) -> None:
        if user not in self.__following and user.__is_logged:  # if the user isn't a follower add him
            self.__following.add(user)
            user.__followers += 1
            print(self.__name + " started following " + user.__name)

    def unfollow(self, user: User) -> None:
        if self.__following and self.__is_logged:  # if the set isnt empty delete the user
            self.__following.remove(user)
            user.__followers -= 1
            print(self.__name + " unfollowed " + user.__name)

    def publish_post(self, post_type: str,*args):
        if self.__is_logged:
            return Factory.create_post(post_type, *args)

    def print_notifications(self) -> None:  # print all the notifications
        if self.__is_logged:
            print(self.__name + "'s notifications:")
            for notif in self.notifications:
                print(notif)

    def add_notification(self, notification: str) -> None:
        self.__notifications += notification

    def get_name(self) -> str:
        return self.__name

    def get_pass(self) -> str:
        return self.__password

    def logged(self) -> str:
        return self.__is_logged

    def set_logged(self, state : bool) -> None:
        self.__is_logged = state