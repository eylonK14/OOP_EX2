from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from Post import Post

if TYPE_CHECKING:
    from User import User


class SalePost(Post):
    def __init__(self, posted_by: User, des: str, pr: int, loc: str):
        super().__init__(posted_by)
        self.description = des
        self.price = pr
        self.location = loc
        self.is_available = True

    def __str__(self):
        to_print = self.posted_by.get_name() + " posted a product for sale:\n"
        if not self.is_available:
            to_print += "Sold! "
        to_print += self.description + " , price: " + str(self.price) + ", pickup from: " + self.location
        return to_print

    def discount(self, percentage: float, password: str) -> None:
        if password == self.posted_by.get_pass() and self.is_available and self.posted_by.logged():  # only a logged
            # in user can make a discount
            self.price -= (self.price * percentage) / 100  # change the price
            print(f"Discount on {self.posted_by.get_name()} product! the new price is: {self.price}")

    def sold(self, password: str):
        if password == self.posted_by.get_pass() and self.posted_by.logged():  # only the user who made the post + if
            # he's logged
            self.is_available = False
            print(f"{self.posted_by.get_name()}'s product is sold")

    def like(self, user: User):
        super().like(user)

    def comment(self, user: User, comment: str):
        super().comment(user, comment)
