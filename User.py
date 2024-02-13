# this class represent the user calls in the social netwerk implement the design
class User:
    def __init__(self, name: str, password: str):
        self.__following = set
        self.__notifications = []
        self.__name = name
        self.__password = password
        self.__followers = 0
        self.__num_of_posts = 0

    def __str__(self):
        print(
            "User name: " + self.__name + ", Number of posts: " + self.__num_of_post + ", Number of followers: " + self.__followers)

    def follow(self, user: User) -> None:
        if (user not in self.__following):  # if the user isn't a follower add him
            self.__following.add(user)
            user.__followers += 1
            print(self.__name + " started following " + user.__name)

    def unfollow(self, user: User) -> None:
        if self.__following:  # if the set isnt empty delete the user
            self.__following.remove(user)
            user.__followers -= 1
            print(self.__name + " unfollowed " + user.__name)

    def print_notifications(self) -> None:  # print all the notifications
        print(self.__name + "'s notifications:")
        for notif in self.notifications:
            print(notif)

    def add_notification(self, notification: str) -> None:
        self.__notifications += notification

    def get_name(self) -> str:
        return self.__name
    def get_pass(self) -> str:
        return  self.__password