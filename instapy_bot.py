from instapy import InstaPy


class InstaPyBot:
    def __init__(self, username, password):
        self.session = InstaPy(username=username, password=password)

    def login(self):
        self.session.login()

    def like_by_tag(self, tags, amount=5):
        self.session.like_by_tags(tags, amount)
