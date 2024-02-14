from Post import Post
from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost
from User import User


class Factory:
    def create_post(self, post_type: str, *args):
        posts = {"Text": TextPost,
                 "Image": ImagePost,
                 "Sale": SalePost}
        return posts[post_type](*args)
