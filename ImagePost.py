from matplotlib import image as mpimg
from Post import Post
from User import User
import matplotlib.pyplot as plt


class ImagePost(Post):
    def __init__(self, posted_by: str, *args):
        super().__init__(posted_by)
        self.path = args[0]

    def __str__(self):
        print(self.posted_by.get_name() + "posted a picture")

    def display(self) -> None:
        if self.posted_by.logged():
            file = mpimg.imread(self.path)
            imgplot = plt.imshow(self.path)
            plt.show()
