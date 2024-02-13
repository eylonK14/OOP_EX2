import User
import matplotlib as plt
import matplotlib.image as mpimg


class Post:
    def __init__(self, posted_by: User):
        self.posted_by = posted_by  # the user who made the post
        self.comments = []
        self.liked_by = set  # all the users who liked the post
        self.likes = 0

    def like(self, user: User):
        if (user not in self.liked_by):
            self.liked_by += user  # add the user who liked to the set
            self.likes += 1  # increse the likes by 1

    def comment(self, user: User, comment: str) -> None:
        self.comments += comment
        print(
            "notification to " + self.posted_by.get_name() + " : " + user.get_name() + " commented on your post: " + comment)
        self.posted_by.add_notification(user.get_name() + " commented on your post")


class TextPost(Post):
    def __init__(self, posted_by: User, text: str):
        super().__init__(posted_by)
        self.text = text

    def __str__(self):
        print(self.posted_by.get_name() + "published a post:")
        print("\"{text}\"".format(text=self.text))


class ImagePost(Post):
    def __init__(self, posted_by: User, path: str):
        super().__init__(posted_by)
        self.path = path

    def __str__(self):
        print(self.posted_by.get_name() + "posted a picture")

    def display(self) -> None:
        file = mpimg.imreadpath
        imgplot = plt.imshow(self.path)
        plt.show()


class SalePost(Post):
    def __init__(self, posted_by: User, description: str, price: float, location: str, is_available: bool):
        super().__init__(posted_by)
        self.description = description
        self.price = price
        self.location = location
        self.is_available = is_available

    def __str__(self):
        print(self.posted_by.get_name() + "posted a product for sale:")
        if self.is_available:
            print("Sold!", end=' ')
        print(self.description + ", price: " + self.price + ", pickup from: " + location)

    def discount(self, precentage: float, password: str) -> None:
        if (password == self.posted_by.get_pass() and self.is_available):
            self.price -= (self.price * precentage) / 100

    def sold(self, password: str):
        if (password == self.posted_by.get_pass()):
            self.is_available = False
            print(self.posted_by.get_name + "'s product is sold")

