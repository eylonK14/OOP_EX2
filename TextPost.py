from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from Post import Post

if TYPE_CHECKING:
    from User import User


class TextPost(Post):
    def __init__(self, posted_by: User, text: str):
        super().__init__(posted_by)
        self.text = text  # the text

    def __str__(self):
        return self.posted_by.get_name() + " published a post: \n" + "\"" + str(self.text) + "\"\n"

    def like(self, user: User):
        super().like(user)

    def comment(self, user: User, comment: str):
        super().comment(user, comment)
