from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User


class Post(ABC):

    @abstractmethod
    def __init__(self, posted_by: User):
        self.posted_by = posted_by  # the user who made the post
        self.comments = []
        self.liked_by = set()  # all the users who liked the post
        self.likes = 0

    @abstractmethod
    def like(self, user: User):
        if user not in self.liked_by and user.logged():
            self.liked_by.add(user)  # add the user who liked to the set
            self.likes += 1  # increase the likes by 1
            print(
                "notification to " + self.posted_by.get_name() + " : " + user.get_name() + " liked your post")
        self.posted_by.add_notification(user.get_name() + " liked your post")

    @abstractmethod
    def comment(self, user: User, comment: str):
        if user.logged():
            self.comments += comment
            print(
                "notification to " + self.posted_by.get_name() + " : " + user.get_name()
                + " commented on your post: " + comment)
            self.posted_by.add_notification(user.get_name() + " commented on your post")
        self.posted_by.add_notification(user.get_name() + " commented on your post")
