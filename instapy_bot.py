from instapy import InstaPy


class InstaPyBot:
    def __init__(self, username, password):
        self.session = InstaPy(username=username, password=password)

    def login(self):
        self.session.login()

    def like_by_tag(self, tags, amount=5):
        self.session.like_by_tags(tags, amount)

    def follow(self, percentage):
        self.session.set_do_follow(True, percentage)

    def block_tags(self, tags):
        self.session.set_dont_like(tags)