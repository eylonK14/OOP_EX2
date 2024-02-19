from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from Post import Post

from PIL import Image

if TYPE_CHECKING:
    from User import User


class ImagePost(Post):
    def __init__(self, posted_by: User, path: str):
        super().__init__(posted_by)
        self.path = path

    def __str__(self):
        return self.posted_by.get_name() + " posted a picture\n"

    def display(self) -> None:  # this func display the image
        if self.posted_by.logged():
            image = Image.open(self.path)
            image.show()

    def like(self, user: User):
        super().like(user)

    def comment(self, user: User, comment: str):
        super().comment(user, comment)



