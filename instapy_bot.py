from instapy import InstaPy


class InstaPyBot:
    def __init__(self, username, password):
        self.session = InstaPy(username=username, password=password)

    def login(self):
        self.session.login()
