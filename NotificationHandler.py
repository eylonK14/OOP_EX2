from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User


#  notification handler implement the observer design pattern

def update(posted_by: User, followers: set[User]) -> None:
    for user in followers:
        user.add_notification(f"{posted_by.get_name()} has a new post")


def notify(user: User) -> None:
    update(user, user.get_followers())


class NotificationHandler:
    pass
