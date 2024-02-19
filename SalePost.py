from Post import Post
import matplotlib as plt
import matplotlib.image as mpimg


class SalePost(Post):
    def __init__(self, posted_by: str, is_available: bool, *args):
        super().__init__(posted_by)
        self.description = args[0]
        self.price = args[1]
        self.location = args[2]
        self.is_available = args[3]

    def __str__(self):
        print(self.posted_by.get_name() + "posted a product for sale:")
        if not self.is_available:
            print("Sold!", end=' ')
        print(self.description + ", price: " + self.price + ", pickup from: " + location)

    def discount(self, precentage: float, password: str) -> None:
        if password == self.posted_by.get_pass() and self.is_available and self.posted_by.logged():
            self.price -= (self.price * precentage) / 100
            print("Discount on " + self.posted_by.get_name() + " product! the new price is: " + self.price)

    def sold(self, password: str):
        if password == self.posted_by.get_pass() and self.posted_by.logged():
            self.is_available = False
            print(self.posted_by.get_name + "'s product is sold")
