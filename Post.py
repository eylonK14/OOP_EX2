from __future__ import annotations
from User import User
from abc import ABC, abstractclassmethod


class Post(ABC):

    @abstractclassmethod
    def __init__(cls, posted_by: User):
        cls.posted_by = posted_by  # the user who made the post
        cls.comments = []
        cls.liked_by = set  # all the users who liked the post
        cls.likes = 0

    @abstractclassmethod
    def like(cls, user: User):
        if user not in cls.liked_by and user.logged():
            cls.liked_by += user  # add the user who liked to the set
            cls.likes += 1  # increase the likes by 1
            print(
                "notification to " + cls.posted_by.get_name() + " : " + user.get_name() + " liked your post")
        cls.posted_by.add_notification(user.get_name() + " liked your post")

    @abstractclassmethod
    def comment(cls, user: User, comment: str):
        if user.logged():
            cls.comments += comment
            print(
                "notification to " + cls.posted_by.get_name() + " : " + user.get_name()
                + " commented on your post: " + comment)
            cls.posted_by.add_notification(user.get_name() + " commented on your post")
        cls.posted_by.add_notification(user.get_name() + " commented on your post")
