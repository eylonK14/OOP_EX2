from __future__ import annotations
from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User


def create_post(post_type: str, *args):
    print(post_type)
    posts = {"Text": TextPost,
             "Image": ImagePost,
             "Sale": SalePost}
    return posts[post_type](*args)


class Factory:
    pass
