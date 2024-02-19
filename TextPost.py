from Post import Post


class TextPost(Post):
    def __init__(self, posted_by: str, *args):
        super().__init__(posted_by)
        self.text = args[0]

    def __str__(self):
        print(self.posted_by.get_name() + "published a post:")
        print("\"{text}\"".format(text=self.text))
